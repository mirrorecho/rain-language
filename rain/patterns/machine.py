from dataclasses import dataclass

import rain


@dataclass
class Machine(rain.Pattern):

    # #TO CONSIDER: something like this could be used to standardaze the instantiating
    # machine "output types" (e.g. creating an abjad.Staff from a rain.Staff object)
    # def make(self, alias:str, **kwargs) -> "Machine":
    #     # fancy machine types would override make and do fancy things
    #     return self._machine_type(self, alias, **kwargs)

    def reset(self):
        raise NotImplementedError()

    def render(self):
        raise NotImplementedError()

    def trigger(self, delta=0, **kwargs):
        raise NotImplementedError()


# --------------------------------------------------------------------

@dataclass
class Printer(Machine): pass

    # def trigger(self, machine:"Machine", event:"Event"):
    #     print(machine.alias, event)

# --------------------------------------------------------------------

# # TODO... keep in python codebase or move?
# @dataclass
# class SynthDefMaker(Machine): pass
