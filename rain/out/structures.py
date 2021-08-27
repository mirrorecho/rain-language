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

    degree: Iterable = cycle((None,))

    pitch: Callable[["OutCell", dict], int] = (lambda s, v: s.scale[v["degree"]])


rain.context.register_types(OutCell)

@dataclass
class OutCellFactory():
    tonic:int = 0
    mode:int = 0

    _base_scale = rain.Scale(steps=scale_steps)

    def get_scale(self, tonic=None):
        return self._base_scale.mode(self.mode) + (tonic or self.tonic)

    def __call__(self, *args, **kwargs) -> OutCell:
        return OutCell.create(scale = self.get_scale(kwargs.pop("tonic", None)), *args, **kwargs)