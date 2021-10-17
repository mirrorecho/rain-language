import abjad
import rain
from rain.score import meters

# --------------------------------------------------------------------

class Score(rain.MachineTree): 

    # TODO this is NASY TO INCLUDE AT THE SCORE LEVEL!
    meter: str = meters.METER_4_4 #TODO: better to save as string so it can be written to data store natively
    # accidental_style: str = "neo-modern-cautionary"

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
                
                
                # accidental_style_command = abjad.LilyPondCommand("accidentalStyle " + self.accidental_style, "before")
                # abjad.attach(accidental_style_command, staff_machine.notation_object[0])

                if self.meter is meters.METER_4_4:
                    print("ATTACHING 4/4")
                    time_signature = abjad.TimeSignature((4, 4))
                    abjad.attach(time_signature, staff_machine.notation_object[0], context="Score")
                elif self.meter is meters.METER_6_8:
                    print("ATTACHING 6/8")
                    time_signature = abjad.TimeSignature((6, 8))
                    abjad.attach(time_signature, staff_machine.notation_object[0], context="Score")
                else:
                    print("METER NOT FOUND!!!!!")
            except:
                print("WARNING: can't attach time signature or clef since staff is empty")
        elif isinstance(staff_machine, rain.MachineTree):
            for s in staff_machine:
                self.prep_staves(s)

    
    def render(self, name="", stylesheets=[], as_midi=False):

        self.prep_staves(self)

        block = abjad.Block(name="score")
        block.items.append(self.notation_object)
        # block.items.append(r"\accidentalStyle dodecaphonic")
        abjad.override(block).Beam.positions = "#'(-2 . -2)"
        ly = abjad.LilyPondFile(items=[block], 
            includes=["./rain-language/rain/score/stylesheets/stylesheet.ily"] + stylesheets
                )
                
        abjad.show(ly,
            output_directory="./rain-language/rain/out/scores/", 
            should_open=False,
            render_prefix=self.key + "_" + name,
        )

        if as_midi:
            abjad.play(
                self.notation_object, 
                output_directory="./rain-language/rain/out/scores/midi/",
                render_prefix=self.key + "_" + name,
                )
