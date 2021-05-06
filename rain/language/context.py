import rain

class Context(object):
    def __init__(self, graph_type, **kwargs):
        self.init_graph(graph_type, **kwargs)
        self._language_type_registry = {}
        
        # public attributes:
        self.default_graph_type = graph_type

    # public properties:

    @property
    def graph(self):
        return self._graph

    # public methods:

    def init_empty_graph(self, graph_type:type=None, **kwargs):
        graph_type = graph_type or self.default_graph_type
        self._graph = graph_type(**kwargs)
        return self._graph

    def init_graph(self, graph_type:type=None, **kwargs):
        # here, this merely calls init_empty_graph to create a new empty graph
        # but other implementations may connect to existing graph data stores
        return self.init_empty_graph(graph_type, **kwargs)

    # TO CONSIDER... a decorator for this
    def register_types(self, *types):
        for t in types:
            self._language_type_registry[t.get_label()] = t

    def get_type(self, label:str):
        return(self._language_type_registry[label])

    def new_by_label_and_key(self, label:str, key:str, **kwargs):
        return self.get_type(label)(key, **kwargs)

