from typing import Any, Iterable, Iterator

import rain


# --------------------------------------------------------------------

def transpose(pitches, value:int=0):
    try:
        return [transpose(p, value) for p in pitches]  
    except:
        return pitches + value

# --------------------------------------------------------------------

class AlterPattern(rain.Pattern): 
    """represents an alteration directly to a pattern"""

    is_alter:bool = True
    is_meddle_alter:bool = False

    def __post_init__(self):
        super().__post_init__()
        self._altered_pattern = None

    @property
    def simultaneous(self) -> bool:
        return self.altered_pattern.simultaneous
    
    @property
    def meddle_chain(self) -> Iterator["AlterPattern"]:
        if self.is_meddle_alter:
            yield self
            alters_pattern = self.alters_pattern
            if alters_pattern.is_alter and alters_pattern.is_meddle_alter:
                yield from alters_pattern.meddle_chain

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

#TODO: very similar to AlterPatternTagVeins ...DRY!
class AlterPatternTagNoteVeins(AlterPattern):
    """
    """

    tags: Iterable[Iterable[str]] = ()
    
    def get_next_tags(self):
        yield from self.tags

    def update_vein(self, vein_dict: dict) -> dict:
        if vein_dict.get("degree", None) is not None:
            return_dict = {}
            return_dict.update(vein_dict)
            tag_list = list(return_dict.get("tags", []))
            new_tags = next(self.next_tags_generator, ())
            tag_list.extend(new_tags)
            return_dict["tags"] = tag_list
            return return_dict
        else:
            return vein_dict

    def __post_init__(self):
        super().__post_init__()
        self.next_tags_generator = self.get_next_tags()
        self.vein_hooks = [lambda s, v: self.update_vein(v)]

# --------------------------------------------------------------------

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

# @dataclass
# # TODO: would be ideal to make this work by index (not every 0 or 1)
# class CutAlterPattern(AlterPattern): #TODO: rename to something more specific?
#     """
#     """

#     cuts: Iterable = None
#     _cuts_iters = None

#     def cut_me(self, vein_dict: dict) -> dict:
#         return_dict = {}
#         return_dict.update(vein_dict)
#         cut_value = next(self._cuts_iters, False)
#         if not cut_value:
#             return(vein_dict)

#         return return_dict

#     def __post_init__(self):
#         super().__post_init__()
#         self._cuts_iters = iter(self.cuts)
#         self.vein_hooks = [lambda s, v: self.cut_me(v)]

# --------------------------------------------------------------------
class MeddleHelper(rain.AlterableMixin):
    key: str
    index: int = 0
    _alter_patterns = ()

    def alter(self, alter_pattern:AlterPattern):
        alter_pattern.is_meddle_alter = True
        alter_pattern.save()
        if len(self._alter_patterns) > 0:
            cue = rain.Cue.create()
            rain.Alters.create(source=alter_pattern, target=cue)
            rain.Cues.create(source=cue, target=self._alter_patterns[-1])
        self._alter_patterns.append(alter_pattern)
        return self

    def connect_alters(self, meddle_pattern:"Meddle"):
        cue = meddle_pattern.find_cue(self.key, self.index)
        rain.MeddleConnectAlter.create(source=meddle_pattern, target=self._alter_patterns[-1])
        rain.Alters.create(source=self._alter_patterns[0], target=cue)

    def __post_init__(self):
        self._alter_patterns = []

class Meddle(AlterPattern): 
    """YO!"""

    # TODO MAYBE: this would be redundant, but might help caching the key for performance reasons
    # alters_key: str = ""

    @property 
    def connected_alters(self) -> Iterable[AlterPattern]:
        yield from self.r("->", "MEDDLE_CONNECT_ALTER").n()

    # def _get_final_cue(self, connected_alter:AlterPattern):
    #     if connected_alter.is_meddle_alter:
    #         return self._get_final_cue(connected_alter.alters_pattern)
    #     else:
    #         return connected_alter.alters_cue

    @property 
    def connected_alters_cues(self) -> rain.Cue:
        for connected_alter in self.connected_alters:
            yield list(connected_alter.meddle_chain)[-1].alters_cue


#TODO: ditto as above, can't represent this natively in a graph ... OK?
class AddDegree(AlterPattern):
    """
    """

    degree: Iterable = ()
    _degree_iter = ()

    def add_degrees(self, vein_dict: dict) -> dict:
        return_dict = {}
        return_dict.update(vein_dict)

        current_degree = next(self._degree_iter, None)

        if current_degree is not None:
            existing_degree = return_dict["degree"]
            if existing_degree is None:
                return_dict["degree"] = current_degree
            else:
                return_dict["degree"] = rain.listify(existing_degree, current_degree)
        return return_dict

    def __post_init__(self):
        super().__post_init__()
        self._degree_iter = iter(self.degree)
        self.vein_hooks = [lambda s, v: self.add_degrees(v)]


#TODO: ditto as above, can't represent this natively in a graph ... OK?
class AddChordDegree(AlterPattern):
    """
    """

    degree: Iterable = ()
    _degree_iter = ()

    def add_degrees(self, vein_dict: dict) -> dict:
        return_dict = {}
        return_dict.update(vein_dict)

        current_degree = next(self._degree_iter, None)

        if current_degree is not None:
            existing_degree = return_dict["degree"]
            if existing_degree is None:
                return_dict["degree"] = current_degree
            else:
                return_dict["degree"] = [existing_degree] + [existing_degree + d for d in rain.listify(current_degree)]
        return return_dict

    def __post_init__(self):
        super().__post_init__()
        self._degree_iter = iter(self.degree)
        self.vein_hooks = [lambda s, v: self.add_degrees(v)]

# =========================================================================

#TODO: ditto as above, can't represent this natively in a graph ... OK?
class Mask(AlterPattern):
    """
    """

    _mask_attrs = ("degree",)
    _mask_iter = ()

    masking: Iterable[bool] = ()

    def mask_me(self, vein_dict: dict) -> dict:
        current_mask = next(self._mask_iter, True)

        if current_mask:
            return vein_dict
        else:
            return_dict = {}
            return_dict.update(vein_dict)           
            for attr in self._mask_attrs:
                return_dict[attr] = None
            return return_dict

    def __post_init__(self):
        super().__post_init__()
        self._mask_iter = iter(self.masking)
        self.vein_hooks = [lambda s, v: self.mask_me(v)]


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
