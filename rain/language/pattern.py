from abc import ABC, abstractmethod
from typing import Any
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

    def __get__(self, key) -> rain.Node:
        if (my_node := self._node[key]) is None:
            my_node = self.context.new_by_key(key)
            self._node[key] = my_node
        return my_node


# --------------------------------------------------------------------

class Blueprint(rain.Node):
    """
    A blueprint is a node in the graph that describes how 
    to make a machine (it's a factory for Machine objects).
    """

    def make(self, alias:str, **kwargs) -> "MachineInterface":
        # fancy machine types would override make and do fancy things
        return self._machine_type(self, alias, **kwargs)

    def trigger(self, machine:"Machine", event:"Event"):
        raise NotImplementedError()

# --------------------------------------------------------------------

class Printer(Blueprint): 

    def trigger(self, machine:"Machine", event:"Event"):
        print(machine.alias, event)


# --------------------------------------------------------------------

class StaffPrinter(Blueprint): pass

# --------------------------------------------------------------------

class SynthDefMaker(Blueprint): pass


# --------------------------------------------------------------------

class Machine(rain.LanguageBase):
    def __init__(self, blueprint:Blueprint, alias:str, **kwargs):
        self._blueprint = blueprint
        self.properties = kwargs
        self.alias = alias

    @property
    def blueprint(self) -> Blueprint: 
        return self.blueprint

    def trigger(self, event: "Event"): 
        self._blueprint.trigger(self, event)


# --------------------------------------------------------------------

# TO CONSIDER... is this class necessary? or just a function of a Pattern?
# OR TO CONSIER... inherit from Context???
class PatternReader(rain.LanguageBase):
    def __init__(self, blueprints:Palette = None):
        self._blueprints = blueprints or Palette()

    @property
    def blueprints(self) -> Palette:
        return _blueprints

    def play(pattern_node:"Pattern", realtime=False):

        for e in pattern_node:
            e.

# --------------------------------------------------------------------

# TO DO: is an event even needed? should the PatternReader just call the
# machine's trigger method with arguments?
class Event(object):
    dur: float = 0
    machine: str = "" # TO CONSIDER... maybe this is actually an instance of machine

    def __str__(self):
        return

# --------------------------------------------------------------------

class PatternInterface(ABC):
    @abstractmethod
    def next(self) -> Event:
        pass

    @abstractmethod
    def get_machines(self) -> tuple:
        pass

# --------------------------------------------------------------------

class Pattern(rain.Node, PatternInterface):
    pass

# --------------------------------------------------------------------

@dataclass
class Cell(Pattern):
    """
    each cell property value would be one of:
    int, float, str, or an iterable of one of those types (or nested iterable)
    """

    def cyclize(self, obj):
        if isinstance(obj, (tuple, list, cycle)):
            return obj
        else:
            return 


    def get_properties(self):
        return {k:getattr(self,k) for k in self.__dataclass_fields__.keys() if k not in self._properties_exclude_fields}



    def next(self) -> Event:
        pass

# --------------------------------------------------------------------

@dataclass
class SimpleMusicCell(Cell):
    pitch: Any = ()
    dur: Any = ()
    instrument: Any = None


c = SimpleMusicCell(
    pitch=(0,2,5,4),
    dur=(1,2,2,6),
    # instrument=rain.infinite("flute"),
)

print("----------------------------------------------------")

# c2 = 
# print(c2[44])

print(type(cycle(("YO",))))

print(
    list(zip(
        c.pitch, 
        c.dur,
        cycle(("YO","ha"))
        ))
    )