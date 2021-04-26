from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import inspect

import rain


# TO DO: make this a mixin
@dataclass
class Language(rain.GraphableInterface):
    """
    an implementation of GraphableInterface using a simple python dataclass
    - this is the base class for all language nodes and relationships
    """

    key: str = field(default_factory = rain.auto_key)
    name: str = ""

    def __post_init__(self):
        self._context = rain.context # to consider... maybe this should just be a simple class attr?
        self._properties_exclude_fields = ("key",)

    @classmethod
    def make(cls, key:str, **kwargs) -> "Language": 
        return cls(key, **kwargs)

    def get_key(self):
        return self.key

    def get_properties(self):
        return {k:getattr(self,k) for k in self.__dataclass_fields__.keys() if k not in self._properties_exclude_fields}

    def set_properties(self, **kwargs): 
        # TO CONSIDER: is this the best way to implement...?
        self.__dict__.update(kwargs)

    @property
    def context(self): 
        return self._context

    @property
    def graph(self): 
        return self.context.graph

    @classmethod
    def create(cls, *args, **kwargs):
        me = cls(*args, **kwargs)
        me.create_me()
        return me

    @classmethod
    def merge(cls, *args, **kwargs):
        me = cls(*args, **kwargs)
        me.merge_me()
        return me

@dataclass
class Node(Language, rain.GraphableNodeInterface):
    """
    base class for all language relationships
    """

    @property
    def labels(self) -> list: 
        return [c.__name__ for c in inspect.getmro(self.__class__) if issubclass(c, rain.Node)]



@dataclass
class Relationship(Language, rain.GraphableRelationshipInterface):
    """
    base class for all language relationships
    """

    source: Node = None
    target: Node = None

    def __post_init__(self):
        super().__post_init__()
        self._properties_exclude_fields = ("key", "source", "target")

    @classmethod
    def from_keys(cls, source_key:str, target_key:str):
        return cls(source=Node(source_key), target=Node(target_key))

    @property
    def source_key(self) -> str: 
        return self.source.key if self.source else None

    @property
    def target_key(self) -> str: 
        return self.target.key if self.target else None

    @property
    def relationship_type(self) -> str: 
        return self.__class__.__name__

    def set_source(self, label:str, key:str): 
        self.source = self.context.new_by_label_and_key(label, key)

    def set_target(self, label:str, key:str): 
        self.target = self.context.new_by_label_and_key(label, key)

class Subject(Relationship):
    pass


