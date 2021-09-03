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
#TODO: can't represent this natively in a graph ... OK?
class AlterPatternLeaves(AlterPattern):
    """
    """

    alter_attrs: dict = None
    alter_lambdas: dict = None

    def update_leaf(self, pattern: rain.Pattern) -> dict:
        for n,v in self.alter_attrs.items():
            setattr(pattern, n, v)
        for n, l in self.alter_lambdas.items():
            pattern = l(pattern)
        return pattern

    def __post_init__(self):
        super().__post_init__()
        self.leaf_hooks = [lambda s, l: self.update_leaf(l)]

# --------------------------------------------------------------------

@dataclass
#TODO: ditto as above, can't represent this natively in a graph ... OK?
class AlterPatternVeins(AlterPattern):
    """
    """

    alter_attrs: dict = None
    alter_lambdas: dict = None

    def update_vein(self, vein_dict: dict) -> dict:
        return_dict = {}
        return_dict.update(vein_dict)
        return_dict.update(self.alter_attrs)
        for n, l in self.alter_lambdas.items():
            return_dict[n] = l(self, return_dict)
        return return_dict

    def __post_init__(self):
        super().__post_init__()
        self.vein_hooks = [lambda s, v: self.update_vein(v)]

# --------------------------------------------------------------------

@dataclass
#TODO: ditto as above, can't represent this natively in a graph ... OK?
class AlterPatternTagVeins(AlterPattern):
    """
    """

    tags: Iterable[Iterable[str]] = ()
    
    def get_next_tags(self):
        yield from self.tags

    def update_vein(self, vein_dict: dict) -> dict:
        return_dict = {}
        return_dict.update(vein_dict)
        tag_list = list(return_dict.get("tags", []))
        new_tags = next(self.next_tags_generator, ())
        tag_list.extend(new_tags)
        return_dict["tags"] = tag_list
        return return_dict

    def __post_init__(self):
        super().__post_init__()
        self.next_tags_generator = self.get_next_tags()
        self.vein_hooks = [lambda s, v: self.update_vein(v)]

# --------------------------------------------------------------------

@dataclass
#TODO: ditto as above, can't represent this natively in a graph ... OK?
class Change(AlterPattern): #TODO: rename to something more specific?
    """
    """

    change_attrs: dict = None
    _change_attrs_iters = None

    def change_me(self, vein_dict: dict) -> dict:
        return_dict = {}
        return_dict.update(vein_dict)
        for n, v in self._change_attrs_iters.items():
            change_value = next(v, False)
            if change_value is not False:
                return_dict[n] = change_value

        return return_dict

    def __post_init__(self):
        super().__post_init__()
        self._change_attrs_iters = {}
        for n, v in self.change_attrs.items():
            self._change_attrs_iters[n] = iter(v)
        self.vein_hooks = [lambda s, v: self.change_me(v)]

# --------------------------------------------------------------------

# TODO: reimplement according to above method IF NECESSARY
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
class Alters(rain.Relationship): pass
# relationship from AlterCue to the Cue it alters, or from AlterPattern to the Pattern it alters
