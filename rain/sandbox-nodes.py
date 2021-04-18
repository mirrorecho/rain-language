import uuid

from dataclasses import dataclass

# import yaml
# import rain

print("--------------------")


# ==============================================================

# implement a local, (non-persistent) graph data structure
# ... this can eventually be replaced, in whole, or in part
# with a graph database data store, with the same interface

class RainBase: 
    """
    bass class for all rain models ... is this even necessary?
    """
    pass



class LocalGraph(RainBase):
    class _Data:
        """
        private base class for nodes and relationships in the local graph
        """
        def __init__(self, type_key:str, key:str=None, **kwargs):
            self.type_key = type_key
            self.key = key or uuid.uuid4().hex
            self._properties = kwargs

    class _Node(_Data):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self._sources_for = set() # for indexing set of _Relationship data
            self._targets_for = set() # for indexing set of _Relationship data

    class _Relationship(_Data):
        def __init__(self, type_key:str, source, target, key:str=None, **kwargs):
            super().__init__(key, **kwargs)
            self.source = source
            self.target = target

        # def __str__(self):
        #     return self.key + ": " + self.source.key + " -> " + self.target.key

        # def __repr__(self):
        #     return self.key + ": " + self.source.key + " -> " + self.target.key

    def __init__(self):
        self._data = {} # all nodes and relationships by key
        self._type_mapping = {}

    def __getitem__(self, k):
        return self.make_typed(self._data[k])

    def _check_key(self, key, exists=True, attr="_data"):
        if (key in getattr(self, attr)) != exists:
            raise KeyError(key + (" does not exist!" if exists else " already exists!"))
 
    def register_type(self, type_class):
        if hasattr(type_class, "type_key"):
            self._type_mapping[type_class.type_key] = type_class
        else:
            raise AttributeError(str(type_class) + " does not have a type_key attribute") 

    def make_typed(self, data_object):
        node_type = self._type_mapping[data_object.type_key]
        return node_type()

    def update(self, key:str, **kwargs):
        self._check_key(key)
        self._data[key]._properties.update(kwargs)
        # TO CONSIDER assume don't need to return the node, but may consider it

    def create_node(self, type_key:str, key:str=None, **kwargs):
        self._check_key(type_key, attr="_type_mapping")
        self._check_key(key, False)
        node = LocalGraph._Node(type_key=type_key, key=key, **kwargs)
        self._data[node.key] = node
        return self.make_typed(node)

    def create_or_update_node(self, type_key:str, key:str=None, **kwargs):
        # duplicating some logic here to avoid unnecessarily checking keys
        # but able to make it more DRY?
        if key in self._data:
            self._data[key]._properties.update(kwargs)
        else:
            self._check_key(type_key, attr="_type_mapping")
            node = LocalGraph._Node(type_key=type_key, key=key, **kwargs)
            self._data[node.key] = node
        # TO DO... should this return the typed object?


    def create_relationship(self, type_key:str, source_key:str, target_key:str, key:str=None, **kwargs):
        self._check_key(type_key, attr="_type_mapping")
        self._check_key(source_key)
        self._check_key(target_key)
        self._check_key(key, False)

        source = self._data[source_key]
        target = self._data[target_key]
        relationship = LocalGraph._Relationship(type_key, source, target, key=key, **kwargs)

        self._data[relationship.key] = relationship
        self._data[source_key]._sources_for.add(relationship)
        self._data[target_key]._targets_for.add(relationship)

    def create_or_update_relationship(self, type_key:str, source_key:str, target_key:str, key:str=None, **kwargs):
        # same as with nodes... duplicating some logic here to avoid unnecessarily checking keys
        # but able to make it more DRY?
        if key in self._data:
            self._data[key]._properties.update(kwargs)
        else:
            self.create_relationship(type_key, source_key, target_key, key, **kwargs)
        # TO DO... should this return the typed object?

    def delete(self, key:str): 
        
        to_delete = self._data[key]

        # for nodes, delete the any relationships that point to this
        # node as a source or target
        for source_for_relationship in getattr(to_delete, "_sources_for", ()):
            self.delete(source_for_relationship)
        for target_for_relationship in getattr(to_delete, "_targets_for", ()):
            self.delete(target_for_relationship)
            
        del self._data[key]

# ==============================================================

# fixture for empty graph
# also fixture for graph with dummy data?

# - test_create_node_creates
# - test_create_raises_exception_on_key_exists

# - test_update_node_updates
# - test_update_raises_exception_on_

# - test_delete_node_deletes
# - test_delete_node_deletes_relationships
# - test_delete_node_deletes_only_relevant_relationships

# - test_create_or_update_relationship_creates
# - test_create_or_update_relationship_updates

# ==============================================================
 
@dataclass
class RainData(RainBase): 
    """
    ORM wrapper methods for interacting with the data (CRUD)
    object creation from YAML and represent as YAML
    ... lazy loading? (as in Django queries)
    """
    key: str = None

    @classmethod
    def type_key(cls):
        return cls.__name__

    @classmethod
    def create(cls):
        return cls.__name__

    def save(self): pass

    @classmethod
    def load(cls): 
        return cls()

class QuerySet(RainBase): pass

class Node(RainData): 
    # TO DO: auto-set type_key based on class name
    type_key: str = "Node"
    relationships: QuerySet = None


class Relationship(RainData): 
    type_key: str = "Relationship"
    source: Node = None # SHOUD NEVER BE NONE
    target: Node = None # SHOUD NEVER BE NONE

    source_type: type = Node
    target_type: type = Node

class Sign(Node): 
    type_key: str = "Sign"

class Character(Sign): 
    type_key: str = "Character"

class Action(Sign): 
    type_key: str = "Action"


class Expression(Sign):
    type_key: str = "Expression"

    # represented by Express relationships that point to other Sign nodes
    # these are JUST propoerties ... 
    action: Sign = None 
    agent: Sign = None
    receiver: Sign = None # *** NEED NEW WORD?
    toward: Sign = None
    context: Sign = None
    # ... to consider, can an expression reference multiple of these? (could be interesting)

    material: QuerySet

# =========================================================

g = LocalGraph()
g.register_type(Character)
g.register_type(Action)
g.register_type(Expression)
g.register_type(Relationship)

awn = Character("AWN")


awn = g.create_node("Character", "AWN")
cep = g.create_node("Character", "CEP")
loving = g.create_node("Action", "LOVING")
exp = g.create_node("Expression", "AWN_LOVING_CEP")
r = g.create_relationship("Relationship", "AWN_LOVING_CEP", "LOVING")

print(loving)


# @dataclass
# class YoMama:
#     showers: str = "Never!"
#     smells_bad: bool = True

#     fancy:str = None

# y = YoMama()
# print(dir(y))
# print("-------------------------------")
# print(y.__dataclass_fields__.keys())


# print(g["LOVING"])

# g.create_node("CEP", type_key="Character")
# g.create_node("LOVING", type_key="Action")
# g.create_node("AWN_LOVING_CEP", type_key="Expression")
# g.create_relationship("AWN_LOVING_CEP", "LOVING", type_key="ACTION")
# g.create_relationship("AWN_LOVING_CEP", "AWN", type_key="AGENT")
# g.create_relationship("AWN_LOVING_CEP", "CEP", type_key="RECEIVER")
# print(g["AWN_LOVING_CEP"]._sources_of)
