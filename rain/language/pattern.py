from abc import ABC, abstractmethod
from typing import Any, Iterable, Iterator
from dataclasses import dataclass, field
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
@dataclass
class Cell(Pattern):
    """
    each cell property value would be one of:
    int, float, str, or an iterable of one of those types (or nested iterable)
    """
    dur: Iterable = ()
    machine: Iterable = ()

    @property
    def veins(self) -> Iterable[Any]:
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

class Cue(rain.Node): pass

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
@dataclass
class TreePattern(Pattern): 

    # TO CONSIDER: this is all perfectly fine for a local graph, but would
    # generate lots of queries to a graph DB ... how to optimize?   
    # ALSO TO CONSIDER... would be MUCH COOLER! if this returned a Select
    @property
    def branches(self) -> Iterable[Pattern]:
        if child_cue := self.r("->", "CUE_FIRST").n().first:
            yield child_cue.r("->", "CUES").n().first
            while child_cue := child_cue.r("->", "CUE_NEXT").n().first:
                yield child_cue.r("->", "CUES").n().first

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
class MachineTree(TreePattern): pass

# --------------------------------------------------------------------

@dataclass
class Machine(Pattern):

    #TODO: what is the MEANING of this?
    def make(self, alias:str, **kwargs) -> "Machine":
        # fancy machine types would override make and do fancy things
        return self._machine_type(self, alias, **kwargs)

    def trigger(self, **kwargs):
        raise NotImplementedError()

# --------------------------------------------------------------------

@dataclass
class Printer(Machine): pass

    # def trigger(self, machine:"Machine", event:"Event"):
    #     print(machine.alias, event)

# --------------------------------------------------------------------

@dataclass
class Staff(Machine): 
    short_name = ""

    def trigger(self, **kwargs):
        print(self.key, kwargs)

# --------------------------------------------------------------------

@dataclass
class Score(MachineTree): pass

# --------------------------------------------------------------------

@dataclass
class StaffGroup(MachineTree): pass

# --------------------------------------------------------------------

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
class PatternReader(rain.LanguageBase):
    def __init__(self, _palette:Palette = None):
        self._palette = _palette or Palette()

    @property
    def palette(self) -> Palette:
        return self._palette

    def read(self, pattern:Pattern):
        for v_dict in pattern.veins:
            if machine_name := v_dict.pop("machine"):
                self.palette[machine_name].trigger(**v_dict)

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
class NotatedMusicCell(Cell):
    pitch: Iterable = ()
    tags: Iterable = ()

# TO DO: move this... 
rain.context.register_types(Pattern, MachineTree, Cell, NotatedMusicCell,
    Cue, CueNext, CueFirst, CueLast, Cues, Contains,
    Staff, StaffGroup, Score, 
    )


print("========================================================")

# print(rain.context._language_type_registry)

c1 = NotatedMusicCell.create(
    key="C1",
    pitch=(0,2,5,4),
    dur=cycle((1,2,)),
    machine=cycle(("VIOLA",)),
    tags = cycle((None,)),
)
c2 = NotatedMusicCell.create(
    key="C2",
    pitch=(7,0,9,0),
    dur=(2,2,3,3),
    machine=cycle(("VIOLIN1", "VIOLIN2"),),
    tags = cycle((None,)),
)

c_pattern = TreePattern.create().extend(c1, c2, c1)

# mp = Palette()
# mp.extend(Machine())


# for d in pa:
#     # d.read()
#     print(d)

violin1 = Staff.create("VIOLIN1", "Violin 1")
violin2 = Staff.create("VIOLIN2", "Violin 2")
viola = Staff.create("VIOLA", "Viola")
cello = Staff.create("CELLO", "Cello")

violins = StaffGroup().create("VIOLINS").extend(
    violin1,
    violin2,
)

quartet_score = Score().create("STRING_QUARTET").extend(
    violins,
    viola,
    cello,
)

# print(quartet_score)
# for x in quartet_score.nodes:
#     print(x)

pr = PatternReader(quartet_score.get_palette())
pr.read(c_pattern)