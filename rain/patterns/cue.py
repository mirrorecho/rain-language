from typing import Tuple

import rain

class Cue(rain.Node): 
    
    @property 
    def cues_pattern(self) -> rain.Pattern:
        pattern = self.r("->", "CUES").n().first
        return pattern

        # TODO: would this be used?
        # if alter_node := self.altered_by:
        #     return alter_node.alter(pattern)
        # else: 
        #     return pattern

    # TODO: would this be used?
    # @property
    # def altered_by(self) -> Tuple["rain.AlterCue"]:
    #     return tuple(self.r("<-", "ALTERS").n())


# --------------------------------------------------------------------
class Contains(rain.Relationship): pass

# --------------------------------------------------------------------

class Cues(rain.Relationship): pass

# --------------------------------------------------------------------

class CueNext(rain.Relationship): pass

# --------------------------------------------------------------------

class CueFirst(rain.Relationship): pass 

# --------------------------------------------------------------------

class CueLast(rain.Relationship): pass 

# --------------------------------------------------------------------

# TO DO: better name for this?
class Context(rain.Relationship): pass
