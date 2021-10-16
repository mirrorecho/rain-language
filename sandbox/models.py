import pydantic
from abc import ABC, abstractmethod
import inspect
import uuid

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


class LanguageYo(pydantic.BaseModel, LanguageBase, rain.GraphableInterface):
    """
    an implementation of GraphableInterface using a simple python dataclass
    - this is the base class for all language nodes and relationships
    """

    key: str = pydantic.Field(default_factory=rain.auto_key)
    name: str = ""

    def __post_init__(self):
        self.set_context()        
        self._properties_exclude_fields = ("key",)
        self._properties_keys = tuple(k for k in self.__dataclass_fields__.keys() if k not in self._properties_exclude_fields)

    @classmethod
    def make(cls, key:str, **kwargs) -> "LanguageYo": 
        return cls(key, **kwargs)

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


class NodeYo(LanguageYo, rain.GraphableNodeInterface):
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

    def r(self, direction:str, label:str=None, *keys, **properties) -> "rain.Select":
        sub_select = rain.TargetedRelationshipSelect(direction, label, *keys, **properties)
        sub_select.select_from = rain.Select(self.get_label(), self.key)
        return sub_select


n = NodeYo(name="Fa")
print(n)