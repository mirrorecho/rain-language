
import rain

class Cue(rain.Node): 
    
    @property 
    def cues_pattern(self) -> rain.Pattern:
        pattern = self.r("->", "CUES").n().first
        if alter_node := self.altered_by:
            return alter_node.alter(pattern)
        else: 
            return pattern

    # NOTE: only a single alter is handled with this implementation ... 
    # TODO: implement an ORDERED iterable of alters
    @property
    def altered_by(self) -> "rain.AlterCue":
        return self.r("<-", "ALTERS").n().first


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
