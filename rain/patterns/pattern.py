from dataclasses import dataclass
from typing import Any, Iterable, Iterator, Callable
from itertools import cycle

import rain

class AlterableMixin():
    def alter(self, alter_pattern):
        cue = rain.Cue.create()
        rain.Alters.create(source=alter_pattern, target=cue)
        rain.Cues.create(source=cue, target=self)
        return alter_pattern

    def change(self, **kwargs):
        key = kwargs.pop("key",None) #TODO maybe, put key as optional first arg
        return self.alter(rain.Change.create(key, change_attrs=kwargs))

    def meddle(self, 
        *args,
        **kwargs # TODO: USED?
        ):
        key, args = rain.key_from_args(args)
        meddle_pattern = self.alter(rain.Meddle.create(key))
        for meddle_helper in args:
            # TODO: check for meddles connecting to the same cues (shouldn't be allowed)
            meddle_helper.connect_alters(meddle_pattern)
        return meddle_pattern

    def add_chord_degree(self, *args):
        key, args = rain.key_from_args(args)
        return self.alter(rain.AddChordDegree.create(key, degree=args))

    def add_degree(self, *args):
        key, args = rain.key_from_args(args)
        return self.alter(rain.AddDegree.create(key, degree=args))

    def mask(self, *args):
        key, args = rain.key_from_args(args)
        return self.alter(rain.Mask.create(key, mask=args))

    def alter_with_attrs_and_lambdas(self, alter_type:"rain.AlterPattern", key=None, **kwargs):
        alter_attrs={}
        alter_lambdas={}
        for n,v in kwargs.items():
            if callable(v):
                alter_lambdas[n] = v
            else:
                alter_attrs[n] = v
        return self.alter(alter_type.create(key, alter_attrs=alter_attrs, alter_lambdas=alter_lambdas))

    def __call__(self, key=None, **kwargs) -> "rain.AlterPatternVeins":
        return self.alter_with_attrs_and_lambdas(rain.AlterPatternVeins, key, **kwargs)

    def alter_leaves(self, key=None, **kwargs) -> "rain.AlterPatternLeaves":
        return self.alter_with_attrs_and_lambdas(rain.AlterPatternLeaves, key, **kwargs)

    def tag(self, *args, **kwargs):
        #TODO maybe, put key as optional first arg
        return self.alter(rain.AlterPatternTagVeins.create(key=kwargs.pop("key",None), tags=args))

    def tag_all(self, *args, **kwargs):
        #TODO maybe, put key as optional first arg
        return self.alter(rain.AlterPatternTagVeins.create(key=kwargs.pop("key",None), tags=cycle(args)))

@dataclass
class Pattern(rain.Node, AlterableMixin): 
    # a node that represents an iterable over a group nodes ... each of which is connected
    # to this node, in a "pattern"

    # TODO: MAYBE consider this
    # node_hooks: Iterable[Callable[["rain.Pattern", "rain.Pattern"], "rain.Pattern"]] = ()
    
    leaf_hooks: Iterable[Callable[["rain.Pattern", "rain.Pattern"], "rain.Pattern"]] = ()
    vein_hooks: Iterable[Callable[["rain.Pattern", Any, int], Any]] = ()
    _parentage = () 

    is_alter:bool = False

    @property
    def is_leaf(self):
        return True

    @property
    def branches(self) -> Iterable["Pattern"]:
        yield from ()

    @property
    def leaves(self) -> Iterable["Pattern"]:
        return_leaf = self
        for h in self.leaf_hooks:
            return_leaf = h(self, return_leaf)
        yield return_leaf

    @property
    def nodes(self) -> Iterable["Pattern"]:
        yield self

    @property
    def veins(self) -> Iterable[Any]:
        return_vein = self
        for h in self.vein_hooks: 
            return_vein = h(self, return_vein)
        yield return_vein

    def get_child_cues(self) -> Iterator["rain.Cue"]:
        yield from ()

    def get_descendant_cues(self) -> Iterator["rain.Cue"]:
        yield from ()

    def find_cue(self, key:str, index:int=0) -> "rain.Cue":
        index_counter = 0
        for i, cue in enumerate(self.get_descendant_cues()):
            if cue.cues_pattern.key == key:
                if index_counter == index:
                    return cue
                else:
                    index_counter+=1
        return None


    def __mul__(self, times):
        return rain.Sequence.create().extend(*[self for i in range(times)])

    def __add__(self, other):
        return rain.Sequence.create().extend(self, other)

    def get_palette(self):
        return rain.Palette(*self.leaves)

    def __iter__(self) -> Iterator[Any]:
        yield from self.veins