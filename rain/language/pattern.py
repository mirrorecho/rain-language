from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Iterable, Iterator, Callable
from itertools import cycle, repeat

import rain

# TO CONSIDER: should this be a node in the graph after all?
# (with relationships to all the nodes the pallete contains)
# ... assume no, but think about it
# ... could also create PaletteNode for specific uses
class Palette(rain.LanguageBase):
    """
    a wrapper around a dictionary of nodes
    """

    def __init__(self, *nodes):
        """
        a cool thing here is that it's easy to create a palette from a selection
        """
        self._nodes = {}
        self.extend(*nodes)

    def add(self, node:rain.Node):
        self._nodes[node.key] = node

    def extend(self, *nodes):
        for n in nodes:
            self.add(n)

    def add_key(self, key:str):
        self._node[key] = None

    def extend_keys(self, *keys):
        for k in keys:
            self.add_key(k)

    def __getitem__(self, key) -> rain.Node:
        if (my_node := self._nodes[key]) is None:
            my_node = self.context.new_by_key(key)
            self._nodes[key] = my_node
        return my_node

# --------------------------------------------------------------------
@dataclass
class Pattern(rain.Node): 
    # a node that represents an iterable over a group nodes ... each of which is connected
    # to this node, in a "pattern"

    @property
    def is_leaf(self):
        return True

    @property
    def branches(self) -> Iterable["Pattern"]:
        yield from ()

    @property
    def leaves(self) -> Iterable["Pattern"]:
        yield self

    @property
    def nodes(self) -> Iterable["Pattern"]:
        yield self

    @property
    def veins(self) -> Iterable[Any]:
        yield self

    def get_palette(self):
        return Palette(*self.leaves)

    def __iter__(self) -> Iterator[Any]:
        yield from self.veins



# --------------------------------------------------------------------
# # LET'S NOT TAKE THIS APPROACH ... instead, see Meter node definition below
# @dataclass
# class CellMixin: 
#     meter:tuple = None
#     meter_durations:tuple = None

#     def __post_init__(self):
#         super().__post_init__()
#         self._iterate_exclude_fields = ("name", "meter", "meter_durations")
#         self._iterate_keys = tuple(k for k in self._properties_keys if k not in self._iterate_exclude_fields)


@dataclass
class Meter(rain.Node): 
    meter: tuple = (4, 4)
    meter_durations: tuple = (2,)

# --------------------------------------------------------------------

@dataclass
class Cell(Pattern):
    """
    each cell property value would be one of:
    int, float, str, or an iterable of one of those types (or nested iterable)
    """
    dur: Iterable = ()
    machine: Iterable = ()
    # simultaneous: bool = False

    @property
    def veins(self) -> Iterable[dict]:
        keys, values = zip(*(
            (k, getattr(self, k))
            for k in self._properties_keys if k!= "name"
            ))
        for zipped_values in zip(*values):
            yield {k:v for k, v in zip(keys, zipped_values)}

    # def cyclize(self, obj):
    #     if isinstance(obj, (tuple, list, cycle)):
    #         return obj
    #     else:
    #         return 

    
# --------------------------------------------------------------------

class Cue(rain.Node): 
    
    @property 
    def cues_pattern(self) -> Pattern:
        pattern = self.r("->", "CUES").n().first
        if alter_node := self.altered_by:
            return alter_node.alter(pattern)
        else: 
            return pattern

    # NOTE: only a single alter is handled with this implementation ... 
    # TODO: implement an ORDERED iterable of alters
    @property
    def altered_by(self) -> "AlterCue":
        return self.r("<-", "ALTERS").n().first

# --------------------------------------------------------------------
@dataclass
class AlterCue(rain.Node): 
    """represents an alteration to a cued pattern or patterns"""

    alter: Callable[[Pattern], Pattern] = None

    @property 
    def alters_cue(self) -> Cue:
        return self.r("->", "ALTERS").n().first

    @property 
    def alters_pattern(self) -> Pattern:
        return self.alters_cue.cues_pattern

# --------------------------------------------------------------------
@dataclass
class AlterPattern(Pattern): 
    """represents an alteration directly to a pattern"""

    alter: Callable[[Pattern], Pattern] = None

    @property 
    def alters_pattern(self) -> Pattern:
        return self.r("->", "ALTERS").n().first

    @property 
    def altered_pattern(self) -> Pattern:
        return self.alter(self.alters_pattern)

    @property
    def is_leaf(self):
        return self.alters_pattern.is_leaf 

    @property
    def branches(self) -> Iterable["Pattern"]:
        yield from self.altered_pattern.branches

    @property
    def leaves(self) -> Iterable["Pattern"]:
        yield from self.altered_pattern.leaves

    @property
    def nodes(self) -> Iterable["Pattern"]:
        yield from self.altered_pattern.nodes

    @property
    def veins(self) -> Iterable[Any]:
        yield from self.altered_pattern.veins

# --------------------------------------------------------------------
class Alters(rain.Relationship): pass
# relationship from AlterCue to the Cue it alters, or from AlterPattern to the Pattern it alters

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

# --------------------------------------------------------------------
@dataclass
class TreePattern(Pattern): 

    def __post_init__(self):
        super().__post_init__()
        self._cached_branches = None

    @property
    def is_leaf(self):
        return False

    # TO DO: THIS CACHING IS REALLY HOOKY!!!!
    @property
    def branches(self) -> Iterable[Pattern]:
        if self._cached_branches is None:
            self._cached_branches = list(self.get_branches())
        return self._cached_branches

    # TO CONSIDER: this is all perfectly fine for a local graph, but would
    # generate lots of queries to a graph DB ... how to optimize?   
    # ALSO TO CONSIDER... would be MUCH COOLER! if this returned a Select
    def get_branches(self):
        if child_cue := self.r("->", "CUE_FIRST").n().first:
            yield child_cue.cues_pattern
            while child_cue := child_cue.r("->", "CUE_NEXT").n().first:
                yield child_cue.cues_pattern

    # DITTO... would be much cooler as a Select
    @property
    def leaves(self) -> Iterable[Pattern]:
        for branch in self.branches:
            yield from branch.leaves

    # DITTO... 
    @property
    def nodes(self) -> Iterable[Pattern]:
        yield self
        for branch in self.branches:
            yield from branch.nodes

    @property
    def veins(self) -> Iterable[Any]:
        for leaf in self.leaves:
            yield from leaf.veins

    def extend(self, *patterns):
        cue_p_first = Cue.create()
        Cues.create(source=cue_p_first, target=patterns[0])

        if not self.r("->", "CUE_FIRST").first:
            CueFirst.create(source=self, target=cue_p_first)
            
        if cue_last := self.r("->", "CUE_LAST").first:
            CueNext.create(source=cue_last.target, target=cue_p_first)
            cue_last.delete()

        # FIRST, create all the cues, then iterate over them, pairwise
        cue_nodes = [cue_p_first] + [Cue.create() for p in patterns[1:]]

        for p, c, c_next in zip(patterns, cue_nodes, cue_nodes[1:]+[None]):
         
            Contains.create(source=self, target=c)
            Cues.create(source=c, target=p)

            if c_next:
                CueNext.create(source=c, target=c_next)
            else:
                CueLast.create(source=self, target=c)
        return self

    def append(self, pattern):
        raise NotImplementedError()

    def insert(self, index, pattern):
        raise NotImplementedError()



# --------------------------------------------------------------------
@dataclass
class CellTree(TreePattern): pass

    # @property
    # def branches(self) -> Iterable[Pattern]:
    #     for branch in super().branches:
    #         yield branch

# --------------------------------------------------------------------
@dataclass
class Sequence(CellTree): pass

# --------------------------------------------------------------------
@dataclass
class Parallel(CellTree): pass

# --------------------------------------------------------------------
@dataclass
class Combo(CellTree): pass

# --------------------------------------------------------------------

@dataclass
class Machine(Pattern):

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
class MachineTree(TreePattern): pass

# --------------------------------------------------------------------

@dataclass
class Printer(Machine): pass

    # def trigger(self, machine:"Machine", event:"Event"):
    #     print(machine.alias, event)

# --------------------------------------------------------------------

# TO DO... keep in python codebase or move?
@dataclass
class SynthDefMaker(Machine): pass

# --------------------------------------------------------------------

# class Machine(rain.LanguageBase):
#     def __init__(self, 
#         # blueprint:Blueprint, 
#         alias:str, **kwargs
#         ):
        
#         # self._blueprint = blueprint
#         self.properties = kwargs
#         self.alias = alias

#     # @property
#     # def blueprint(self) -> Blueprint: 
#     #     return self.blueprint

#     def trigger(self, event: "Event"): 
#         self._blueprint.trigger(self, event)


# --------------------------------------------------------------------

# TO CONSIDER... is this class necessary? or just a function of a Pattern?
# ASSUME YES, WORTH IT
# ALSO TO CONSIER... inherit from Context???
# PURPOSE IS TO "READ" IN THE "CORRECT" order .
# ... restrict to only use with CellTree patterns?
class PatternReader(rain.LanguageBase):
    def __init__(self, _pattern:Pattern, _palette:Palette = None):
        self._palette = _palette or Palette()
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
    def palette(self) -> Palette:
        return self._palette

    @property
    def pattern(self) -> Pattern:
        return self._pattern

    def read_pattern(self, pattern:Pattern, pattern_time=0):
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
                if isinstance(pattern, Sequence):
                    pattern_time = branch_end_time
                elif isinstance(pattern, Parallel):
                    if branch_end_time > max_branch_end_time:
                        max_branch_end_time = branch_end_time
            
            if isinstance(pattern, Parallel):
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
            for v_dict in v_list:
                if machine_name := v_dict.pop("machine"):
                    self.palette[machine_name].trigger(p, **v_dict)

        # for p in pattern_keys:
        #     print(p)
        #     for vein in self._triggers[p]:
        #         print(vein)

        # for v_dict in self._pattern.veins:

        #     if machine_name := v_dict.pop("machine"):
        #         dur = v_dict[dur]
        #         self.palette[machine_name].trigger(self.total_dur, **v_dict)

    # def __init__(self, blueprints:Palette = None):
    #     self._blueprints = blueprints or Palette()

    # @property
    # def blueprints(self) -> Palette:
    #     return self._blueprints

    # def play(pattern_node:"Pattern", realtime=False):

    #     for e in pattern_node:
    #         e.

# --------------------------------------------------------------------

# # TO DO: is an event even needed? should the PatternReader just call the
# # machine's trigger method with arguments?
# class Event(object):
#     dur: float = 0
#     machine: str = "" # TO CONSIDER... maybe this is actually an instance of machine

#     def __str__(self):
#         return


# --------------------------------------------------------------------

@dataclass
class MusicCell(Cell):
    pitch: Iterable = ()
    tags: Iterable = ()

# TO DO: move this... 
# rain.context.register_types(Pattern, MachineTree, Cell, NotatedMusicCell,
#     Cue, CueNext, CueFirst, CueLast, Cues, Contains,
#     # Staff, StaffGroup, Score, 
#     )


# print("========================================================")

# # print(rain.context._language_type_registry)

# c1 = NotatedMusicCell.create(
#     key="C1",
#     pitch=(0,2,5,4),
#     dur=cycle((1,2,)),
#     machine=cycle(("VIOLA",)),
#     tags = cycle((None,)),
# )
# c2 = NotatedMusicCell.create(
#     key="C2",
#     pitch=(7,0,9,0),
#     dur=(2,2,3,3),
#     machine=cycle(("VIOLIN1", "VIOLIN2"),),
#     tags = cycle((None,)),
# )

# c_pattern = TreePattern.create().extend(c1, c2, c1)

# mp = Palette()
# mp.extend(Machine())


# for d in pa:
#     # d.read()
#     print(d)

# violin1 = Staff.create("VIOLIN1", "Violin 1")
# violin2 = Staff.create("VIOLIN2", "Violin 2")
# viola = Staff.create("VIOLA", "Viola")
# cello = Staff.create("CELLO", "Cello")

# violins = StaffGroup().create("VIOLINS").extend(
#     violin1,
#     violin2,
# )

# quartet_score = Score().create("STRING_QUARTET").extend(
#     violins,
#     viola,
#     cello,
# )

# print(quartet_score)
# for x in quartet_score.nodes:
#     print(x)

# pr = PatternReader(quartet_score.get_palette())
# pr.read(c_pattern)