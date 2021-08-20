from dataclasses import dataclass
from typing import Any, Iterable, Callable

import rain

@dataclass
class AlterCue(rain.Node): 
    """represents an alteration to a cued pattern or patterns"""

    alter: Callable[["rain.Pattern"], "rain.Pattern"] = None

    @property 
    def alters_cue(self) -> "rain.Cue":
        return self.r("->", "ALTERS").n().first

    @property 
    def alters_pattern(self) -> "rain.Pattern":
        return self.alters_cue.cues_pattern

# --------------------------------------------------------------------


@dataclass
class AlterPattern(rain.Pattern): 
    """represents an alteration directly to a pattern"""

    alter: Callable[["rain.Pattern"], "rain.Pattern"] = None

    # TODO: needed?
    @property 
    def simultaneous(self) -> bool:
        return getattr(self, "simultaneous", None)

    #TODO: this is a bit confusing as a propery (since each call creates a new object)
    # make it a vanilla method instead?
    @property 
    def alters_pattern(self) -> "rain.Pattern":
        return self.r("->", "ALTERS").n().first

    @property 
    def altered_pattern(self) -> "rain.Pattern":
        return self.alter(self.alters_pattern)

    @property
    def is_leaf(self):
        return self.altered_pattern.is_leaf 

    @property
    def branches(self) -> Iterable["rain.Pattern"]:
        yield from self.altered_pattern.branches

    @property
    def leaves(self) -> Iterable["rain.Pattern"]:
        yield from self.altered_pattern.leaves

    @property
    def nodes(self) -> Iterable["rain.Pattern"]:
        yield from self.altered_pattern.nodes

    @property
    def veins(self) -> Iterable[Any]:
        yield from self.altered_pattern.veins


# --------------------------------------------------------------------


@dataclass
#TODO: can't represent this natively in a graph ... OK?
class AlterPatternAttrs(AlterPattern):
    """
    """
    # alter: Callable[[Pattern], Pattern] = {
    #     return 
    #     }

    alter_attrs: dict = None

    @property 
    def altered_pattern(self) -> "rain.Pattern":
        ap = self.alters_pattern
        if self.alter_attrs:
            for n,v in self.alter_attrs.items():
                setattr(ap, n, v)
        return ap

    def setup_attrs(self, **kwargs):
        self.alter_attrs = kwargs
        self.save()


# --------------------------------------------------------------------
class Alters(rain.Relationship): pass
# relationship from AlterCue to the Cue it alters, or from AlterPattern to the Pattern it alters
