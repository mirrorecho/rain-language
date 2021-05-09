from rain.utils import auto_key, to_snake_case, to_upper_snake_case

from rain.graph.interface import (GraphableInterface, GraphableNodeInterface, 
    GraphableRelationshipInterface, GraphInterface, SelectInterface)

from rain.graph.local import GraphLocal

from rain.language.context import Context
from rain.language.base import LanguageBase, Language, Node, Relationship
from rain.language.select_ import Select # note have to name the module select_ (with underscore at end) to avoid namine conflicts with uuid dependencies

context = Context(
    GraphLocal # can change to any other graph type to use that type in default context
    )

# TO DO: use decorator instead of registering here
context.register_types(Language, Node, Relationship)

