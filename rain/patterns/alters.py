from dataclasses import dataclass
from typing import Any, Iterable, Callable, Tuple

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

    # TODO: needed?
    @property 
    def simultaneous(self) -> bool:
        return self.altered_pattern.simultaneous

    #TODO: this is a bit confusing as a property (since each call creates a new object)
    # make it a vanilla method instead?
    @property 
    def altered_pattern(self) -> "rain.Pattern":
        if self._altered_pattern is None:
            self._altered_pattern = rain.pattern_set_branch_hooks(self, self.alters_pattern, self.alters_cue)
        # print("ALTERED PATTERN", self._altered_pattern.key)
        return self._altered_pattern

    @property 
    def alters_cue(self) -> "rain.Cue":
        return self.r("->", "ALTERS").n().first

    @property 
    def alters_pattern(self) -> "rain.Pattern":
        return self.alters_cue.r("->", "CUES").n().first

    @property
    def is_leaf(self):
        return False

    @property
    def branches(self) -> Iterable["rain.Pattern"]:
        yield self.altered_pattern

    @property
    def leaves(self) -> Iterable["rain.Pattern"]:
        yield from self.altered_pattern.leaves

    @property
    def nodes(self) -> Iterable["rain.Pattern"]:
        yield self
        yield from self.altered_pattern.nodes

    @property
    def veins(self) -> Iterable[Any]:
        yield from self.altered_pattern.veins

    def get_child_cues(self) -> rain.Cue:
        yield self.alters_cue

    def get_descendant_cues(self):
        yield self.alters_cue
        yield from self.alters_pattern.get_descendant_cues()

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
        if self.alter_attrs is None:
            self.alter_attrs = {}
        if self.alter_lambdas is None:
            self.alter_lambdas = {}
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
@dataclass
class MeddleHelper(rain.AlterableMixin):
    key: str
    index: int = 0
    _alter_pattern = None

    def alter(self, alter_pattern:AlterPattern):
        self._alter_pattern = alter_pattern
        return self

    def connect_alter(self, meddle_pattern:"Meddle"):
        cue = meddle_pattern.find_cue(self.key, self.index)
        rain.MeddleConnectAlter.create(source=meddle_pattern, target=self._alter_pattern)
        rain.Alters.create(source=self._alter_pattern, target=cue)


@dataclass
class Meddle(AlterPattern): 
    """YO!"""

    # TODO MAYBE: this would be redundant, but might help caching the key for performance reasons
    # alters_key: str = ""

    @property 
    def connected_alter(self) -> AlterPattern:
        return self.r("->", "MEDDLE_CONNECT_ALTER").n().first

    @property 
    def connected_alter_cue(self) -> rain.Cue:
        return self.connected_alter.r("->", "ALTERS").n().first



        
# --------------------------------------------------------------------

# TODO MAYBE: reimplement according to above method IF NECESSARY
# @dataclass
# class AlterCue(rain.Node): 
#     """represents an alteration to a cued pattern or patterns"""

#     @property 
#     def alters_cues(self) -> Tuple["rain.Cue"]:
#         return tuple(self.r("->", "ALTERS").n())

#     @property 
#     def alters_patterns(self) -> Tuple["rain.Pattern"]:
#         return tuple(c.cues_pattern for c in self.alters_cues)


# --------------------------------------------------------------------
class Alters(rain.Relationship): pass
# relationship from AlterCue to the Cue it alters, or from AlterPattern to the Pattern it alters

class MeddleConnectAlter(rain.Relationship): pass
# relationship from Meddle to the Alter node that describes the alteration and in turn
# has an ALTERS relationship to the cue of a descendant node to be "meddled with"
