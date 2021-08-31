from dataclasses import dataclass, field

import abjad
import rain
from rain.score import meters

# --------------------------------------------------------------------

@dataclass
class Score(rain.MachineTree): 

    # TODO this is NASY TO INCLUDE AT THE SCORE LEVEL!
    meter: abjad.Meter = meters.METER_4_4 #TODO: better to save as string so it can be written to data store natively

    def reset(self):
        self.notation_object = abjad.Score(name=self.name)
        for staff_thingy in self.branches:
            staff_thingy.reset()
            self.notation_object.append(staff_thingy.notation_object)

    #TODO: this is TOTALLY NASTY!
    #TODO: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def set_time_signature(self, staff_thingy):
        if isinstance(staff_thingy, abjad.Staff):
            if self.meter is meters.METER_4_4:
                try:
                    time_signature = abjad.TimeSignature((4, 4))
                    abjad.attach(time_signature, staff_thingy[0], context="Score")
                except:
                    print("WARNING: can't attach time signature since staff is empty")
            elif self.meter is meters.METER_6_8:
                try:
                    time_signature = abjad.TimeSignature((6, 8))
                    abjad.attach(time_signature, staff_thingy[0], context="Score")
                except:
                    print("WARNING: can't attach time signature since staff is empty")
            else:
                print("METER NOT FOUND!!!!!")
        elif isinstance(staff_thingy, (abjad.Score, abjad.StaffGroup)):
            for s in staff_thingy:
                self.set_time_signature(s)

    def render(self):

        self.set_time_signature(self.notation_object)

        abjad.show(self.notation_object,
            output_directory="./rain-language/rain/out/scores/", 
            should_open=False,
            render_prefix="material_mama",
        )