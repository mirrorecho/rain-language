from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from uuid import UUID, uuid4
import inspect, json

import rain

class LanguageBase(ABC):

    def set_context(self, context=None):
        # TO CONSIDER: maybe this should just be a simple class attr?
        self._context = context or rain.context 

    @property
    def context(self): 
        return self._context

    @property
    def graph(self): 
        return self.context.graph    


# TO CONSIDER: make this a mixin
@dataclass
class Language(LanguageBase, rain.GraphableInterface):
    """
    an implementation of GraphableInterface using a simple python dataclass
    - this is the base class for all language nodes and relationships
    """

    key: str = field(default_factory = rain.auto_key)
    name: str = ""

    def __post_init__(self):
        self.set_context()        
        self._properties_exclude_fields = ("key",)
        self._properties_keys = tuple(k for k in self.__dataclass_fields__.keys() if k not in self._properties_exclude_fields)

    @classmethod
    def make(cls, key:str, **kwargs) -> "Language": 
        if key:
            return cls(key, **kwargs)
        else:
            return cls(**kwargs)

    def get_key(self):
        return self.key

    def get_properties(self):
        return {k:getattr(self,k) for k in self._properties_keys}

    def set_properties(self, **kwargs): 
        # TO CONSIDER: is this the best way to implement...?
        self.__dict__.update(kwargs)

    @classmethod
    def create(cls, key=None, *args, **kwargs):
        if key:
            me = cls(key, *args, **kwargs)    
        else:
            me = cls(*args, **kwargs)
        return me.create_me()

    @classmethod
    def merge(cls, *args, **kwargs):
        me = cls(*args, **kwargs)
        return me.merge_me()


@dataclass
class Node(Language, rain.GraphableNodeInterface):
    """
    base class for all language relationships
    """

    # TO CONSIDER: should this be a class attribute?
    @classmethod
    def get_labels(cls) -> list: 
        return [c.__name__ for c in inspect.getmro(cls) if issubclass(c, rain.Node)]

    @classmethod
    def get_label(cls) -> str: 
        return cls.__name__

    def to_json(self, **kwargs) -> str: 
        # TODO maybe: should this really include all the dataclass fields?
        # or just the properties fields + key?
        return json.dumps({k:getattr(self,k) for k in self.__dataclass_fields__})

    @classmethod
    def from_json(cls, json_str:str) -> rain.GraphableInterface: 
        my_dict = json.loads(json_str)
        key = my_dict.pop("key", None)
        return cls.make(key, **my_dict)

    def r(self, direction:str, label:str=None, *keys, **properties) -> "rain.Select":
        sub_select = rain.TargetedRelationshipSelect(direction, label, *keys, **properties)
        # TODO: simplify here using __call__()?
        sub_select.select_from = rain.Select(self.get_label(), self.key)
        return sub_select

    # TODO: maybe use strying relationship_label instead?
    def relate(self, relationship_type:type, other:"Node", **properties) -> "Relationship":
        new_relationship = relationship_type(source=self, target=other)
        return new_relationship

@dataclass
class Relationship(Language, rain.GraphableRelationshipInterface):
    """
    base class for all language relationships
    """

    source: Node = None
    target: Node = None

    def __post_init__(self):
        self.set_context()        
        self._properties_exclude_fields = ("key", "source", "target")
        self._properties_keys = tuple(k for k in self.__dataclass_fields__.keys() if k not in self._properties_exclude_fields)

    @classmethod
    def from_keys(cls, source_key:str, target_key:str, **kwargs):
        key = kwargs.pop("key", None)
        context = kwargs.pop("context", rain.context)
        return cls.make(key, source=context.get_by_key(source_key), target=context.get_by_key(target_key), **kwargs)

    @property
    def source_key(self) -> str: 
        return self.source.key if self.source else None

    # TO CONSIDER: should this be a class attribute?
    @property
    def target_key(self) -> str: 
        return self.target.key if self.target else None

    @classmethod
    def get_label(cls) -> str: 
        return rain.to_upper_snake_case(cls.__name__)

    def set_source(self, label:str, key:str): 
        # TODO: is this method necessary,
        # also, is make_by_label the best context method here?
        self.source = self.context.make_by_label(label, key)

    def set_target(self, label:str, key:str): 
        # TODO: ditto as above
        self.target = self.context.make_by_label(label, key)

    def to_json(self, **kwargs) -> str: 
        my_dict = {k:getattr(self,k) for k in ("key",) + self._properties_keys}
        my_dict["source_key"] = self.source.key
        my_dict["target_key"] = self.target.key
        return json.dumps(my_dict)

    @classmethod
    def from_json(cls, json_str:str) -> rain.GraphableInterface: 
        my_dict = json.loads(json_str)
        source_key = my_dict.pop("source_key")
        target_key = my_dict.pop("target_key")
        return cls.from_keys(source_key, target_key, **my_dict)
