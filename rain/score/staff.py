from dataclasses import dataclass, field

import abjad
from abjad.get import duration, pitches

import rain
from rain.score import tagging, meters

# --------------------------------------------------------------------


@dataclass
class Staff(rain.Machine): 
    short_name = ""
    meter: abjad.Meter = meters.METER_4_4 #TODO: better to save as string so it can be written to data store natively

    clef: str = "treble"

    def __post_init__(self):
        super().__post_init__()
        self.reset()

    def reset(self):
        self.notation_object = abjad.Staff(name=self.name)
        abjad.setting(self.notation_object).pedalSustainStyle = "#'mixed"
        
        # TODO: this doesn't work
        # abjad.setting(self.notation_object).accidentalStyle = "neo-modern-cautionary"
        self.total_dur = 0
        self.rests_dur = 0
        self.current_meter_node = self.meter.root_node

    # TODO MAYBE: shouldn't need to pass node around as param ... just reset self.current_meter_node
    def meter_next_sibling_or_aunt(self, node):
        rel_node = node.root
        if not rel_node:
            # iff node is already root, than node.root is None
            # so just return node
            return node

        graph_order = node.graph_order
        ancestor_index = -1
        while node.parent is not None:
            node = node.parent
            sibling_index = graph_order[ancestor_index] + 1
            if len(node) > sibling_index:
                rel_node = node[sibling_index]
                break
            ancestor_index -= 1
        return rel_node

    def render(self):
        abjad.show(self.notation_object)


    def trigger_lt(self, dur, pitch, leaf_durs=None, pitch_spell=None, tags=(), **kwargs):

        def meter_node_dur(node):
            meter_pair = node.duration.pair 
            return meter_pair[0]/meter_pair[1]*4

        # TODO: consider moving this to the tagging module
        def tag_leaf(leaf, tag_name):
            attachment = tagging.get_attachment(tag_name)
            if attachment:
                if callable(attachment):
                    attachment(leaf)
                elif isinstance(attachment, (list, tuple)):
                    for m in attachment:
                        abjad.attach(m, leaf)
                else:
                    # TODO MAYBE: stem tremolos should be auto-attached to every leaf in logical tie...
                    abjad.attach(attachment, leaf)

        if leaf_durs:
            if isinstance(leaf_durs, (list, tuple)):
                durs = leaf_durs
            else:
                durs = [leaf_durs]
            mm_rest_durs = [False for d in durs]
        else:
            durs = []
            mm_rest_durs = []
        dur_remaining = dur

        while dur_remaining > 0:

            while meter_node_dur(self.current_meter_node) > dur_remaining \
                    and isinstance(self.current_meter_node, abjad.rhythmtrees.RhythmTreeContainer):
                self.current_meter_node = self.current_meter_node[0]
            
            dur_meter = meter_node_dur(self.current_meter_node)

            # TODO: could probalby come up with a better way
            # to figure out MM rests ... (this check runs even for non-rests)
            # print(self.current_meter_node, self.current_meter_node.root)
            if self.current_meter_node == self.meter.root_node:
                mm_rest_durs.append(True)
            else:
                mm_rest_durs.append(False)

            if dur_meter >= dur_remaining:
                if not leaf_durs:
                    durs.append(dur_remaining)
                # current_meter_offset = dur_remaining # needed?
                dur_remaining = 0

            else:
                if not leaf_durs:
                    durs.append(dur_meter)
                dur_remaining -= dur_meter
                # current_meter_offset = 0 # needed?
            
            # if current_meter_offset == 0:
            self.current_meter_node = self.meter_next_sibling_or_aunt(self.current_meter_node)

        leaves = []

        if pitch is not None:  
            for d in durs:
                if isinstance(pitch, int):
                    leaf = abjad.Note.from_pitch_and_duration(pitch, d/4)
                elif isinstance(pitch, (list, tuple)):
                    leaf = abjad.Chord()
                    leaf.written_duration = d/4
                    leaf.written_pitches = pitch
                if pitch_spell:
                    if pitch_spell == "FLAT":
                        abjad.iterpitches.respell_with_flats(leaf)
                    elif pitch_spell == "SHARP":
                        abjad.iterpitches.respell_with_sharps(leaf)
                leaves.append(leaf)
            if len(leaves) > 1:
                abjad.tie(leaves)
        else:
            for d, mm in zip(durs, mm_rest_durs):
                if mm:
                    leaves.append(abjad.MultimeasureRest(d/4))
                else:
                    leaves.append(abjad.Rest(d/4))

        if leaves and tags:
            for tag_thingy in tags:
                if isinstance(tag_thingy, str):
                    tag_name = tag_thingy
                    if tag_name in tagging.end_leaf_inventory:
                        leaf = leaves[-1]
                    elif tag_name in tagging.stem_tremolos_inventory:
                        for leaf in leaves:
                            tag_leaf(leaf, tag_name)
                    else:
                        leaf = leaves[0]
                    tag_leaf(leaf, tag_name)
                elif isinstance(tag_thingy, (tuple, list)):
                    for leaf, tag_name in zip(leaves, tag_thingy):
                        if tag_name:
                            tag_leaf(leaf, tag_name)


        self.notation_object.extend(leaves)


    def trigger(self, 
        start_dur=0,
        dur=1,
        pitch=None,
        pitch_spell = None,
        leaf_durs = None,
        tags=(),
        **kwargs,
        ):

        leaf = None
        delta = start_dur - self.total_dur 
        self.rests_dur += delta

        # TO DO: encapsulate all of this into something that writes to an abjad container

        if dur > 0:
            if pitch is None and not tags and not leaf_durs:
                # TODO: handle force_dur / tags for rests here
                self.rests_dur += dur
            else:
                if self.rests_dur > 0:
                    self.trigger_lt(dur=self.rests_dur, pitch=None, leaf_durs=None, **kwargs)
                    self.rests_dur = 0
                self.trigger_lt(dur=dur, pitch=pitch, pitch_spell=pitch_spell, 
                    leaf_durs=leaf_durs, tags=tags, **kwargs)
            
        self.total_dur = self.total_dur + delta + dur
        
        