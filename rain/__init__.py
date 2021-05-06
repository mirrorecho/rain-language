from rain.utils import auto_key, to_snake_case, to_upper_snake_case

from rain.graph.interface import (GraphableInterface, GraphableNodeInterface, 
    GraphableRelationshipInterface, GraphInterface, SelectionInterface)

from rain.graph.local import GraphLocal

from rain.language.context import Context
from rain.language.base import Language, Node, Relationship, Subject
from rain.language.selection import Selection

context = Context(
    GraphLocal # can change to any other graph type to use that type in default context
    )

# TO DO: use decorator instead of registering here
context.register_types(Language, Node, Relationship, Subject)

