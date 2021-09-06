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


    def trigger_lt(self, dur, pitch, force_durs=None, pitch_spell=None, tags=(), **kwargs):

        def meter_node_dur(node):
            meter_pair = node.duration.pair 
            return meter_pair[0]/meter_pair[1]*4

        if force_durs:
            durs = force_durs
        else:
            durs = []
            dur_remaining = dur

            while dur_remaining > 0:

                while meter_node_dur(self.current_meter_node) > dur_remaining \
                        and isinstance(self.current_meter_node, abjad.rhythmtrees.RhythmTreeContainer):
                    self.current_meter_node = self.current_meter_node[0]
                
                dur_meter = meter_node_dur(self.current_meter_node)

                if dur_meter >= dur_remaining:
                    durs.append(dur_remaining)
                    # current_meter_offset = dur_remaining # needed?
                    dur_remaining = 0

                else:
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
            for d in durs:
                leaves.append(abjad.Rest(d/4))

        if leaves and tags:
            leaf = leaves[0]
            for tag_name in tags:
                attachment = tagging.get_attachment(tag_name)
                if attachment:
                    if callable(attachment):
                        attachment(leaf)
                    else:
                        # TODO MAYBE: stem tremolos should be attached to every leaf in logical tie...
                        abjad.attach(attachment, leaf)

        self.notation_object.extend(leaves)


    def trigger(self, 
        start_dur=0,
        dur=1,
        pitch=None,
        pitch_spell = None,
        force_durs = None,
        tags=(),
        **kwargs,
        ):

        leaf = None
        delta = start_dur - self.total_dur 
        self.rests_dur += delta

        # TO DO: encapsulate all of this into something that writes to an abjad container

        if dur > 0:
            if pitch is None:
                # TODO: handle force_dur / tags for rests here
                self.rests_dur += dur

            else:
                if self.rests_dur > 0:
                    self.trigger_lt(dur=self.rests_dur, pitch=None, force_durs=None, **kwargs)
                    self.rests_dur = 0
                self.trigger_lt(dur=dur, pitch=pitch, pitch_spell=pitch_spell, 
                    force_durs=force_durs, tags=tags, **kwargs)
            
        self.total_dur = self.total_dur + delta + dur
        
        