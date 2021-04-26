from collections.abc import Iterable, Iterator
from abc import ABC, abstractmethod
import rain

# TO CONSIDER... a very base base class for any data with label, key, and properties

class GraphableInterface(ABC):

    @property
    @abstractmethod
    def graph(self) -> "GraphInterface": pass

    # TO CONSIDER: use duck-typing instead?
    @property
    @abstractmethod
    def data_type(self): pass

    @abstractmethod 
    def get_key(self) -> str: pass

    @abstractmethod 
    def get_properties(self) -> dict: pass

    @abstractmethod 
    def set_properties(self, **kwargs): pass

    @classmethod
    @abstractmethod 
    def make(cls, key, **kwargs) -> "GraphableInterface": pass

    # TO DO: are these names overkill? (adding _me)
    def create_me(self):
        self.graph.create(self)

    def merge_me(self):
        self.graph.merge(self)

    def read(self):
        self.graph.read(self)

    def save(self):
        self.graph.save(self)

    def delete(self):
        self.graph.delete(self.get_key())



class SelectionInterface(ABC): 

    @property
    @abstractmethod
    def select_from(self) -> "SelectionInterface": pass

    def yield_from_iterable(self) -> Iterable: 
        return self.graph.select_interface(self)

    def __iter__(self) -> Iterator: 
        yield from self.graph.select_interface(self)

    def __contains__(self, k) -> bool: 
        # TO DO MAYBE: if end up implementing equivalence for graphable objects (by key)
        # then may be cleaner to use that instead
        if isinstance(k, GraphableInterface):
            key = k.get_key()
        else:
            key = k
        return next((True for d in self if d.get_key() == key), False)

    # # DON'T implement until caching is implemented
    # def __len__(self):
        
    #     # NOTE: unable to use the following:
    #     # return len(list(self))
    #     # ... because list(), or tuple() for that matter, internally calls len() 
    #     # ... so would result in infinite recursion

    @property
    @abstractmethod
    def context(self) -> "rain.Context": pass

    @property
    @abstractmethod
    def graph(self) -> "GraphInterface": pass

    @property
    @abstractmethod
    def label(self) -> str: pass

    @property
    @abstractmethod
    def keys(self) -> tuple: pass

    @property
    @abstractmethod 
    def properties(self) -> dict: pass

    @abstractmethod 
    def set_properties(self, **kwargs): pass

    @abstractmethod
    def __getitem__(self, k): pass

    @abstractmethod
    def __call__(self, *args, **kwargs): pass



class GraphableNodeInterface(GraphableInterface): 

    @property
    def data_type(self):
        return "Node"

    @property
    @abstractmethod 
    def labels(self) -> list: pass



class GraphableRelationshipInterface(GraphableInterface): 

    @property
    def data_type(self):
        return "Relationship"

    @property
    @abstractmethod 
    def relationship_type(self) -> str: pass

    # TO DO will these methods make sense in the context of 
    # graph databases (e.g. Neo4j, ...)?
    @property
    @abstractmethod 
    def source_key(self) -> str: pass

    @property
    @abstractmethod 
    def target_key(self) -> str: pass

    @abstractmethod 
    def set_source(self, label:str, key:str): pass

    @abstractmethod 
    def set_target(self, label:str, key:str): pass




class GraphInterface(ABC):
    
    @abstractmethod 
    def __init__(self, **kwargs): pass

    # TO CONSIDER... is this playing with fire? 
    # (will generate query whenever it's used in a real db context)
    @abstractmethod 
    def __contains__(self, key) -> bool: pass

    def exists(self, data:GraphableInterface) -> bool:
        return data.get_key() in self

    @abstractmethod 
    def create(self, data:GraphableInterface): pass

    @abstractmethod 
    def merge(self, data:GraphableInterface): pass

    @abstractmethod
    def read(self, data:GraphableInterface): pass

    @abstractmethod
    def get_relationship(self, data:GraphableRelationshipInterface): pass

    @abstractmethod 
    def save(self, data:GraphableInterface): pass

    @abstractmethod 
    def delete(self, key:str): pass
