from typing import Callable
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

        def any_property_matches(self, **kwargs):
            # return true if any kwarg value matches this data's propery by the same name,
            # otherwise false
            for n,v in kwargs.items():
                if n in self._properties and self._properties.get(n) == v:
                    return True
            return False

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

        def cleanup(self, graph):
            graph._discard_label_index(self.relationship_type, self)
            del self.source._sources_for[self]
            del self.target._targets_for[self]

    def __init__(self):
        self._data = {} # all nodes and relationships by key
        self._type_index = {} # index of each label or relationship type, with the values
        # being dicts of key/object references

    def __getitem__(self, key) -> _Data:
        return self._data[key]

    def __contains__(self, key) -> bool: 
        return key in self._data

    def _check_key(self, key, exists=True):
        if (key in self) != exists:
            raise KeyError(key + (" does not exist!" if exists else " already exists!"))

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

    def get_properties(self, key:str) -> dict:
        return self._data[key]._properties

    def create(self, data:rain.GraphableInterface): 
        self._check_key(data.get_key(), False)
        if data.data_type == "Node":
            self._create_node(data.key, *data.labels, **data.get_properties())
        else:
            self._create_relationship(data.key, data.relationship_type, data.source_key, data.target_key, **data.get_properties())

    def merge(self, data:rain.GraphableInterface):
        if data.key in self:
            # note, not calling save here to avoid checking for key twice
            self.get_properties(data.key).update(data.get_properties())
        else:
            # ditto
            if data.data_type == "Node":
                self._create_node(data.key, *data.labels, **data.get_properties())
            else:
                self._create_relationship(data.key, data.relationship_type, data.source_key, data.target_key, **data.get_properties())

    def read(self, data:rain.GraphableInterface): 
        self._check_key(data.key)
        data.set_properties(**self.get_properties(data.key))

    def save(self, data:rain.GraphableInterface):
        self._check_key(data.key)
        self.get_properties(data.key).update(data.get_properties())

    def delete(self, key:str): 
        self._data[key].cleanup(self)
        del self._data[key]

    def clear(self):
        self._data = {}

    @property
    def size(self):
        return len(self._data)

    def select(self, label:str=None, *keys, **properties):

        my_iter=()

        if label and keys:
            my_iter = map(self._type_index[label].get, keys)
        elif keys and not label:
            my_iter = map(self._data.get, keys)
        elif label and not keys:
            my_iter = self._type_index[label].values()
        elif properties:
            my_iter = self._data.values()

        if properties:
            return filter(lambda x: x is not None and x.any_property_matches(**properties), my_iter)
        else:
            return filter(lambda x: x is not None, my_iter)
