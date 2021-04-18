from rain.settings import *
from rain.utils import (auto_key, )

from rain.graph.interface import (GraphableInterface, GraphableNodeInterface, 
    GraphableRelationshipInterface, GraphInterface)

from rain.graph.local import GraphLocal

from rain.language.base import Language, Node, Relationship, Subject

_language_type_registry = {}

# TO CONSIDER... this might be more elegantly implemented with decorators
def register_types(*types):
    for t in types:
        _language_type_registry[t.__name__] = t

def get_type(label:str):
    return(_language_type_registry[label])

register_types(Language, Node, Relationship, Subject)

DEFAULT_GRAPH = GraphLocal()