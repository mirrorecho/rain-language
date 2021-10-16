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

    @classmethod
    @abstractmethod 
    def get_label(self) -> str: pass

    # # TO CONSIDER: the following propery to indicate whether, for a given object
    # # if that object has already been loaded/read from the underlying data store
    # @property
    # @abstractmethod 
    # def loaded(self) -> bool: pass

    # TO DO: are these names overkill? (adding _me)
    def create_me(self):
        self.graph.create(self)
        return self

    def merge_me(self):
        self.graph.merge(self)
        return self

    def read(self):
        self.graph.read(self)
        return self

    def save(self):
        self.graph.save(self)
        return self

    def delete(self):
        self.graph.delete(self.get_key())

    def __eq__(self, other:"GraphableInterface"):
        try:
            return self.get_key() == other.get_key()
        except:
            return False


class SelectInterface(ABC): 

    @property
    @abstractmethod
    def select_from(self) -> "SelectInterface": pass

    @property
    @abstractmethod
    def direction(self) -> str: 
        """
        an indicator that specifies whether to filter/traverse select_from by:
        '->' : relationships that have select_from nodes as the sources
        '<-' : relationships that have select_from nodes as the targets
        '->()' : nodes which select_from relationships point to as targets
        '<-()' : nodes which select_from relationships point to as sources
        None : no filter/traversal
        """
        pass

    # TO DO: should I implement __next__?

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

    # TO DO: add test for this
    @property
    def first(self) -> GraphableInterface: 
        return next(iter(self), None)

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

    @classmethod
    @abstractmethod 
    def get_labels(self) -> list: pass



class GraphableRelationshipInterface(GraphableInterface): 

    @property
    def data_type(self):
        return "Relationship"

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

    # TO DO: is this what we want here?
    def read(self):
        self.graph.read_relationship(self)
        return self


class GraphInterface(ABC):
    
    #TODO why is this here?
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
    def read_relationship(self, data:GraphableRelationshipInterface): pass

    @abstractmethod 
    def save(self, data:GraphableInterface): pass

    @abstractmethod 
    def delete(self, key:str): pass


class ContextInterface(ABC):

    @property
    @abstractmethod 
    def graph(self) -> GraphInterface: pass

    @abstractmethod 
    def init_empty_graph(self, graph_type:type=None, **kwargs) -> GraphInterface: pass

    def init_graph(self, graph_type:type=None, **kwargs)-> GraphInterface:
        # here, this merely calls init_empty_graph to create a new empty graph
        # but specific implementations may connect to existing graph data stores
        return self.init_empty_graph(graph_type, **kwargs)

    # TO CONSIDER... a decorator for this
    @abstractmethod 
    def register_types(self, *types): pass #TODO: type hinting for this

    @abstractmethod 
    def get_type(self, label:str) -> type: pass

    @abstractmethod 
    def new_by_key(self, key:str) -> GraphableInterface: pass

    def new_by_label_and_key(self, label:str, key:str, **kwargs) -> GraphableInterface:
        return self.get_type(label)(key, **kwargs)

