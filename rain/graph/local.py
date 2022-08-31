from typing import Callable
from collections.abc import Iterable, Iterator
from abc import ABC, abstractmethod

import rain


# TO CONSIDER... property based indexing

class GraphLocal(rain.GraphInterface):
    
    class _Data(ABC):
        """
        private base class for nodes and relationships in the local graph
        """
        def __init__(self, key:str, **kwargs):
            self.key = key
            self._properties = kwargs

        def any_property_matches(self, **kwargs) -> bool:
            # return true if any kwarg value matches this data's propery by the same name,
            # otherwise false
            for n,v in kwargs.items():
                if n in self._properties and self._properties.get(n) == v:
                    return True
            return False

        @property
        @abstractmethod
        def primary_label(self)  -> str: pass

        @abstractmethod
        def cleanup(self, graph):
            """to call before deleting me"""
            pass

    class _Node(_Data):
        def __init__(self, key:str, *labels, **kwargs):
            super().__init__(key, **kwargs)
            self.labels = labels
            # TO CONSIDER: whether these dicts are the best implementation here...
            self._sources_for = {} # a dict for faster indexing ... keys are relationships, values are the target nodes
            self._targets_for = {} # a dict for faster indexing ... keys are relationships, values are the target nodes

        @property
        def primary_label(self):
            return self.labels[0]

        def cleanup(self, graph):
            for label in self.labels:
                graph._discard_label_index(label, self)
            for source_for_relationship in list(self._sources_for):
                graph.delete(source_for_relationship.key)
            for target_for_relationship in list(self._targets_for):
                graph.delete(target_for_relationship.key)

    class _Relationship(_Data):
        def __init__(self, key:str, relationship_type:str, source, target, **kwargs):
            super().__init__(key, **kwargs)
            self.relationship_type = relationship_type
            self.source = source
            self.target = target

        @property
        def primary_label(self):
            return self.relationship_type

        @property
        def labels(self)  -> tuple: 
            # implemented purely for interoperability with _Node
            return (self.relationship_type,)

        def cleanup(self, graph):
            graph._discard_label_index(self.relationship_type, self)
            del self.source._sources_for[self]
            del self.target._targets_for[self]

    def __init__(self, **kwargs):
        self._data = {} # all nodes and relationships by key
        self._type_index = {} # index of each label or relationship type, with the values
        # being dicts of key/object references

    def __getitem__(self, key) -> _Data:
        return self._data[key]

    def __contains__(self, key) -> bool: 
        return key in self._data

    def _check_key(self, key, exists=True):
        if (key in self) != exists:
            raise KeyError(str(key) + (" does not exist!" if exists else " already exists!"))

    def _add_label_index(self, label:str, _data:_Data):
        if label not in self._type_index:
            self._type_index[label] = {}
        self._type_index[label][_data.key] = _data

    def _discard_label_index(self, label:str, _data:_Data):
        self._type_index[label].pop(_data.key, None)

    def _create_node(self, key, *labels, **kwargs):
        _node = GraphLocal._Node(key, *labels, **kwargs)
        self._data[key] = _node
        for label in labels:
            self._add_label_index(label, _node)

    def _create_relationship(self, key:str, relationship_type:str, source_key:str, target_key:str, **kwargs):
        self._check_key(source_key)
        self._check_key(target_key)

        source = self._data[source_key]
        target = self._data[target_key]

        _relationship = GraphLocal._Relationship(key, relationship_type, source, target, **kwargs)
        self._data[key] = _relationship

        source._sources_for[_relationship] = target
        target._targets_for[_relationship] = source

        self._add_label_index(relationship_type, _relationship)

    # ============================================================================================================

    @property
    def size(self):
        return len(self._data)
    
    def get_properties(self, key:str) -> dict:
        return self._data[key]._properties

    # ============================================================================================================

    # TODO: rename these data arguments in methods below to "item" to avoid confusion with local "_data" attribute
    def create(self, data:rain.GraphableInterface): 
        self._check_key(data.get_key(), False) # TODO when to use get_key() method vs key property?
        if data.data_type == "Node":
            self._create_node(data.key, *data.get_labels(), **data.get_properties())
        else:
            self._create_relationship(data.key, data.get_label(), data.source_key, data.target_key, **data.get_properties())

    def merge(self, data:rain.GraphableInterface):
        if data.key in self:
            # note, not calling save here to avoid checking for key twice
            self.get_properties(data.key).update(data.get_properties())
        else:
            # ditto
            if data.data_type == "Node":
                self._create_node(data.key, *data.get_labels(), **data.get_properties())
            else:
                self._create_relationship(data.key, data.get_label(), data.source_key, data.target_key, **data.get_properties())

    def read(self, data:rain.GraphableInterface): 
        self._check_key(data.key)
        data.set_properties(**self.get_properties(data.key))

    def read_relationship(self, data:rain.GraphableRelationshipInterface): 
        self.read(data)
        _relationship = self._data[data.get_key()]
        _source = _relationship.source
        _target = _relationship.target
        data.set_source(_source.primary_label, _source.key)
        data.set_target(_target.primary_label, _target.key)

    def save(self, data:rain.GraphableInterface):
        self._check_key(data.key)
        self.get_properties(data.key).update(data.get_properties())

    def delete(self, key:str): 
        self._data[key].cleanup(self)
        del self._data[key]

    def clear(self):
        self._data = {}
        self._type_index = {}


    def _get_typed(self, local_data:_Data, context:rain.ContextInterface) -> rain.GraphableInterface:
            # NOTE: even though we're calling contect.make_by_label here
            # (which instantiates an object not necessarily in graph),
            # in this case we know it's connected to the graph, via the local_data arg
            return context.make_by_label(
                local_data.primary_label, 
                local_data.key, 
                **local_data._properties
                )


    def get_typed(self, key:str, context:rain.ContextInterface) -> rain.GraphableInterface:
        return self._get_typed(self._data[key], context)


    def select_interface(self, select:rain.SelectInterface): #TODO - return type hint?
        return map(
            lambda x: self._get_typed(x, select.context), 
            self._iter_data(select)
            )


    def _iter_data(self, select:rain.SelectInterface) -> Iterable:
        if select.select_from:
            my_iter = self._iter_data(select.select_from)
            if select.direction:
                if select.direction == "->":
                    my_iter = (y for x in my_iter for y in x._sources_for)
                elif select.direction == "<-":
                    my_iter = (y for x in my_iter for y in x._targets_for)
                elif select.direction == "->()":
                    my_iter = map(lambda x: x.target, my_iter)
                elif select.direction == "<-()":
                    my_iter = map(lambda x: x.source, my_iter)

            if select.keys:
                # WARNING: this implementation differs from the key select
                # above for the original select ... it's purely a filter ... won't re-order or duplicate items
                my_iter = filter(lambda x: x.key in select.keys, my_iter)

            if select.label:
                my_iter = filter(lambda x: select.label in x.labels, my_iter)

        else:
            my_iter=()

            if select.label and select.keys:
                my_iter = filter(
                    lambda x: x is not None, 
                    map(self._type_index[select.label].get, select.keys)
                    )
            elif select.keys and not select.label:
                my_iter = filter(
                    lambda x: x is not None, 
                    map(self._data.get, select.keys)
                    )
            elif select.label and not select.keys:
                my_iter = self._type_index[select.label].values()
            elif select.properties:
                my_iter = self._data.values()

        if select.properties:
            my_iter = filter(lambda x: x.any_property_matches(**select.properties), my_iter)

        return my_iter

