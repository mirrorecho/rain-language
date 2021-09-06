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
    def prep_staves(self, staff_machine):
        if isinstance(staff_machine, rain.Staff):
            try:
                clef = abjad.Clef(staff_machine.clef)
                abjad.attach(clef, staff_machine.notation_object[0])
                if self.meter is meters.METER_4_4:
                    time_signature = abjad.TimeSignature((4, 4))
                    abjad.attach(time_signature, staff_machine.notation_object[0], context="Score")
                elif self.meter is meters.METER_6_8:
                    time_signature = abjad.TimeSignature((6, 8))
                    abjad.attach(time_signature, staff_machine.notation_object[0], context="Score")
                else:
                    print("METER NOT FOUND!!!!!")
            except:
                print("WARNING: can't attach time signature or clef since staff is empty")
        elif isinstance(staff_machine, rain.MachineTree):
            for s in staff_machine:
                self.prep_staves(s)

    
    def render(self):

        self.prep_staves(self)

        abjad.show(self.notation_object,
            output_directory="./rain-language/rain/out/scores/", 
            should_open=False,
            render_prefix="material_mama",
        )