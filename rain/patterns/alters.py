from dataclasses import dataclass
from typing import Any, Iterable, Callable

import rain


# --------------------------------------------------------------------

def transpose(pitches, value:int=0):
    try:
        return [transpose(p, value) for p in pitches]  
    except:
        return pitches + value

# --------------------------------------------------------------------

@dataclass
class AlterPattern(rain.Pattern): 
    """represents an alteration directly to a pattern"""

    def __post_init__(self):
        super().__post_init__()
        self._altered_pattern = None

    #TODO same method as on TreePattern ... DRY!
    def set_hooks(self, branch: rain.Pattern):
        if self.leaf_hooks:
            if not branch.leaf_hooks:
                branch.leaf_hooks = []
            branch.leaf_hooks.extend(self.leaf_hooks)
        if self.vein_hooks:
            if not branch.vein_hooks:
                branch.vein_hooks = []
            branch.vein_hooks.extend(self.vein_hooks)
        return branch

    # TODO: needed?
    @property 
    def simultaneous(self) -> bool:
        return self.altered_pattern.simultaneous

    #TODO: this is a bit confusing as a property (since each call creates a new object)
    # make it a vanilla method instead?
    @property 
    def altered_pattern(self) -> "rain.Pattern":
        if self._altered_pattern is None:
            self._altered_pattern = self.set_hooks(self.r("->", "ALTERS").n().first)
        return self._altered_pattern

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


# @dataclass
# class AlterPattern(rain.Pattern): 
#     """represents an alteration directly to a pattern"""

#     alter: Callable[["rain.Pattern"], "rain.Pattern"] = None

#     def __post_init__(self):
#         super().__post_init__()
#         self._altered_pattern = None

#     # TODO: needed?
#     @property 
#     def simultaneous(self) -> bool:
#         return self.altered_pattern.simultaneous

#     #TODO: this is a bit confusing as a propery (since each call creates a new object)
#     # make it a vanilla method instead?
#     @property 
#     def alters_pattern(self) -> "rain.Pattern":
#         if self._altered_pattern is None:
#             self._altered_pattern = self.r("->", "ALTERS").n().first
#         return self._altered_pattern

#     @property 
#     def altered_pattern(self) -> "rain.Pattern":
#         return self.alter(self.alters_pattern)

#     @property
#     def is_leaf(self):
#         return self.altered_pattern.is_leaf 

#     @property
#     def branches(self) -> Iterable["rain.Pattern"]:
#         yield from self.altered_pattern.branches

#     @property
#     def leaves(self) -> Iterable["rain.Pattern"]:
#         yield from self.altered_pattern.leaves

#     @property
#     def nodes(self) -> Iterable["rain.Pattern"]:
#         yield from self.altered_pattern.nodes

#     @property
#     def veins(self) -> Iterable[Any]:
#         yield from self.altered_pattern.veins


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
    alter_lambdas: dict = None

    def update_vein(self, vein_dict: dict) -> dict:
        return_dict = {}
        return_dict.update(vein_dict)
        return_dict.update(self.alter_attrs)
        for n, l in self.alter_lambdas.items():
            return_dict[n] = l(return_dict.get(n, None))
        return return_dict

    def __post_init__(self):
        super().__post_init__()
        self.vein_hooks = [lambda s, v: self.update_vein(v)]

    # @property 
    # def altered_pattern(self) -> "rain.Pattern":
    #     ap = self.alters_pattern
    #     for l in ap.leaves:
    #         if self.alter_attrs:
    #             for n,v in self.alter_attrs.items():
    #                 setattr(l, n, v)
    #     return ap

    # @property
    # def leaves(self) -> Iterable["rain.Pattern"]:
    #     for l in self.altered_pattern.leaves:
    #         if self.alter_attrs:
    #             for n,v in self.alter_attrs.items():
    #                 setattr(l, n, v)
    #         yield l

    # def setup_attrs(self, **kwargs):
    #     self.alter_attrs = kwargs
    #     self.save()


# --------------------------------------------------------------------
class Alters(rain.Relationship): pass
# relationship from AlterCue to the Cue it alters, or from AlterPattern to the Pattern it alters
