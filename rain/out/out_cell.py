from dataclasses import dataclass
from typing import Callable, Iterable
from itertools import cycle

import rain

scale_steps = (0,1,3,4,6,8,10,12)

@dataclass
class OutCell(rain.MusicCell):
    _no_traverse_keys = rain.MusicCell._no_traverse_keys + ("scale",)

    #TODO: MAYBE the scale as separate node(s).. yay!!
    scale: rain.Scale = rain.Scale(steps=scale_steps)

    tonic: Iterable = cycle((None,))

    # TODO MAYBE: implement this:
    # mode:int = 0 

    degree: Iterable = cycle((None,))

    octave: Iterable = cycle((0,))

    pitch: Callable[["OutCell", dict], int] = (
        lambda s, v: rain.transpose(
            s.scale.getitem_with_root(v["degree"], v["tonic"]), 
            12*v["octave"]
            )
        )



rain.context.register_types(OutCell)

@dataclass
class OutCellFactory():
    tonic:int = 0
    mode:int = 0

    _base_scale = rain.Scale(steps=scale_steps)

    def __call__(self, *args, **kwargs) -> OutCell:
        tonic = kwargs.pop("tonic", self.tonic)
        return OutCell.create(
            scale = self._base_scale.mode(self.mode) + tonic,
            tonic = cycle((None,)),
            *args, **kwargs
            )