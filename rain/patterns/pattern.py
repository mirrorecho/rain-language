from dataclasses import dataclass
from typing import Any, Iterable, Iterator, Callable

import rain

@dataclass
class Pattern(rain.Node): 
    # a node that represents an iterable over a group nodes ... each of which is connected
    # to this node, in a "pattern"

    # TODO: MAYBE consider this
    # node_hooks: Iterable[Callable[["rain.Pattern", "rain.Pattern"], "rain.Pattern"]] = ()
    
    leaf_hooks: Iterable[Callable[["rain.Pattern", "rain.Pattern"], "rain.Pattern"]] = ()
    vein_hooks: Iterable[Callable[["rain.Pattern", Any, int], Any]] = ()
    _parentage = () 

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

    def alter(self, alter_pattern):
        rain.Alters.create(source=alter_pattern, target=self)
        return alter_pattern

    def change(self, **kwargs):
        key = kwargs.pop("key",None)
        return self.alter(rain.Change.create(key, change_attrs=kwargs))

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
        return self.alter(rain.AlterPatternTagVeins.create(key=kwargs.pop("key",None), tags=args))

    def __mul__(self, times):
        return rain.Sequence.create().extend(*[self for i in range(times)])

    def __add__(self, other):
        return rain.Sequence.create().extend(self, other)

    def get_palette(self):
        return rain.Palette(*self.leaves)

    def __iter__(self) -> Iterator[Any]:
        yield from self.veins