from dataclasses import dataclass, field

import abjad
import rain

# --------------------------------------------------------------------

@dataclass
class Score(rain.MachineTree): 
    def reset(self):
        self.notation_object = abjad.Score(name=self.name)
        for staff_thingy in self.branches:
            staff_thingy.reset()
            self.notation_object.append(staff_thingy.notation_object)

    def render(self):
        abjad.show(self.notation_object,
            output_directory="./rain-language/rain/out/scores/", 
            should_open=False,
            render_prefix="material_mama",
        )