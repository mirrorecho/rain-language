from abc import ABC, abstractmethod


class GraphableInterface(ABC):

    @property
    @abstractmethod
    def graph(self): pass

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
    pass



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



class GraphInterface(ABC):

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
    def save(self, data:GraphableInterface): pass

    @abstractmethod 
    def delete(self, key:str): pass
