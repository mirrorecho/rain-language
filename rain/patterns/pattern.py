from dataclasses import dataclass
from typing import Any, Iterable, Iterator, Callable
from itertools import cycle

import rain

@dataclass
class Pattern(rain.Node): 
    # a node that represents an iterable over a group nodes ... each of which is connected
    # to this node, in a "pattern"

    leaf_hooks: Iterable[Callable[["rain.Pattern", "rain.Pattern"], "rain.Pattern"]] = ()
    vein_hooks: Iterable[Callable[["rain.Pattern", Any], Any]] = ()

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


    # def alter_call(self, alter:Callable[["rain.Pattern"], "rain.Pattern"]) -> "rain.AlterPatternAttrs":
    #     ap = rain.AlterPattern.create(alter=alter)
    #     rain.Alters.create(source=ap, target=self)
    #     return ap

    def __call__(self, **kwargs) -> "rain.AlterPatternAttrs":
        alter_attrs={}
        alter_lambdas={}
        for n,v in kwargs.items():
            if callable(v):
                alter_lambdas[n] = v
            else:
                alter_attrs[n] = v
        ap = rain.AlterPatternAttrs.create(alter_attrs=alter_attrs, alter_lambdas=alter_lambdas)
        rain.Alters.create(source=ap, target=self)
        return ap

    # def alter_cycle(self, **kwargs) -> "rain.AlterPatternAttrs":
    #     for n,v in kwargs.items():
    #         kwargs[n] = cycle((v,))
    #     return self.alter_me(**kwargs)


    def get_palette(self):
        return rain.Palette(*self.leaves)

    def __iter__(self) -> Iterator[Any]:
        yield from self.veins