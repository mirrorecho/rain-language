import rain


# --------------------------------------------------------------------

# TO CONSIDER... is this class necessary? or just a function of a Pattern?
# ASSUME YES, WORTH IT
# ALSO TO CONSIER... inherit from Context???
# PURPOSE IS TO "READ" IN THE "CORRECT" order .
# ... restrict to only use with CellTree patterns?
class PatternReader(rain.LanguageBase):
    def __init__(self, _pattern:rain.Pattern, _palette:rain.Palette = None):
        self._palette = _palette or rain.Palette()
        self._pattern = _pattern
        self.reset()

    def reset(self):
        self.current_time = 0
        self.total_dur = 0
        self._triggers = {}

    def add_trigger(self, time:float, properties:dict):
        if time not in self._triggers:
            self._triggers[time] = []
        self._triggers[time].append(properties)

    @property
    def palette(self) -> rain.Palette:
        return self._palette

    @property
    def pattern(self) -> rain.Pattern:
        return self._pattern

    def read_pattern(self, pattern:rain.Pattern, pattern_time=0):
        # if isinstance(pattern, Parallel):
        #     pass
        # elif isinstance(pattern, Sequence):
        #     pass
        # elif isinstance(pattern, Combo):
        #     pass

        # TODO: handle context relationships for ANY node here

        if not pattern.is_leaf:
            max_branch_end_time = pattern_time

            for branch in pattern.branches:

                branch_end_time = self.read_pattern(branch, pattern_time)
                if pattern.simultaneous:
                    if branch_end_time > max_branch_end_time:
                        max_branch_end_time = branch_end_time
                else:
                    pattern_time = branch_end_time

            
            if isinstance(pattern, rain.Parallel):
                pattern_time = max_branch_end_time

        else:
            for vein in pattern.veins:
                self.add_trigger(pattern_time, vein)
                pattern_time += vein["dur"]
        
        return pattern_time


    def read(self):
        self.read_pattern(self._pattern)

        pattern_keys = sorted(self._triggers.keys())

        for p in pattern_keys:
            v_list = self._triggers[p]
            print(p, v_list)
            for v_dict in v_list:
                if machine_name := v_dict.pop("machine"):
                    self.palette[machine_name].trigger(p, **v_dict)
