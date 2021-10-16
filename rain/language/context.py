import rain

class Context(rain.ContextInterface):
    def __init__(self, graph_type, **kwargs):
        self.init_graph(graph_type, **kwargs)
        self._language_type_registry = {}
        
        # public attributes:
        self.default_graph_type = graph_type

    # overriding public properties:
    @property
    def graph(self) -> rain.GraphInterface:
        return self._graph

    # overriding public methods:
    def init_empty_graph(self, graph_type:type=None, **kwargs) -> rain.GraphInterface:
        graph_type = graph_type or self.default_graph_type
        self._graph = graph_type(**kwargs)
        return self._graph

    # TO CONSIDER... a decorator for this
    def register_types(self, *types): #TODO: type hinting for this
        for t in types:
            self._language_type_registry[t.get_label()] = t

    def get_type(self, label:str) -> type:
        return(self._language_type_registry[label])

    def new_by_key(self, key:str) -> rain.GraphableInterface:
        return self.graph.get_typed(key, self)
