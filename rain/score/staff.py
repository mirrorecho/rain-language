from dataclasses import dataclass, field

import abjad
from abjad.get import duration

import rain
from rain.score import tagging

# --------------------------------------------------------------------

@dataclass
class Staff(rain.Machine): 
    short_name = ""

    def __post_init__(self):
        super().__post_init__()
        self.reset()

    def reset(self):
        self.notation_object = abjad.Staff(name=self.name)
        self.total_dur = 0

    def render(self):
        abjad.show(self.notation_object)

    def trigger(self, 
        start_dur=0,
        dur=1,
        pitch=None,
        tags=(),
        **kwargs,
        ):

        leaf = None
        delta = start_dur - self.total_dur 

        # TO DO: encapsulate all of this into something that writes to an abjad container

        if delta > 0:
            # TO DO 1: convert to assignable durations and handle metrical re-division
            try:
                self.notation_object.append(abjad.Rest(written_duration=delta/4))
            except:
                print("NON-ASSIGNABLE DURATION", delta)
        if dur > 0:
            
            # ditto TO DO 1
            if pitch is not None:
                if isinstance(pitch, int):
                    try:
                        # print(self.notation_object)
                        leaf = abjad.Note.from_pitch_and_duration(pitch, dur/4)
                    except:
                        print("NON-ASSIGNABLE DURATION", dur)
                elif isinstance(pitch, (list, tuple)):
                    leaf = abjad.Chord()
                    leaf.written_duration = dur/4
                    leaf.written_pitches = pitch
            else:
                # ditto TO DO 1
                leaf = abjad.Rest(written_duration=dur/4)
           
            if leaf is not None:
                if tags: # TODO: condition needed?
                    for tag_name in tags:
                        attachment = tagging.get_attachment(tag_name)
                        if attachment:
                            if callable(attachment):
                                attachment(leaf)
                            else:
                                # TODO MAYBE: stem tremolos should be attached to every leaf in logical tie...
                               
                                abjad.attach(attachment, leaf)

                self.notation_object.append(leaf)
            
        self.total_dur = self.total_dur + delta + dur
        
        