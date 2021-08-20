from dataclasses import dataclass
from typing import Any, Iterable, Iterator
from itertools import cycle

import rain

@dataclass
class Pattern(rain.Node): 
    # a node that represents an iterable over a group nodes ... each of which is connected
    # to this node, in a "pattern"

    @property
    def is_leaf(self):
        return True

    @property
    def branches(self) -> Iterable["Pattern"]:
        yield from ()

    @property
    def leaves(self) -> Iterable["Pattern"]:
        yield self

    @property
    def nodes(self) -> Iterable["Pattern"]:
        yield self

    @property
    def veins(self) -> Iterable[Any]:
        yield self

    def alter_me(self, **kwargs) -> "rain.AlterPatternAttrs":
        ap = rain.AlterPatternAttrs.create()
        ap.setup_attrs(**kwargs)
        rain.Alters.create(source=ap, target=self)
        return ap

    def alter_cycle(self, **kwargs) -> "rain.AlterPatternAttrs":
        for n,v in kwargs.items():
            kwargs[n] = cycle((v,))
        return self.alter_me(**kwargs)

    def to_machine(self, machine_key):
        return self.alter_cycle(machine=machine_key)

    def get_palette(self):
        return rain.Palette(*self.leaves)

    def __iter__(self) -> Iterator[Any]:
        yield from self.veins