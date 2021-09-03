from dataclasses import dataclass
from typing import Callable, Iterable
from itertools import cycle

import rain

scale_steps = (0,1,3,4,6,8,10,12)

@dataclass
class GlobalTonic():
    start_tonic:int = 0
    modulation:int = 0

    def __init__(self, start_tonic=0):
        self.start_tonic = start_tonic

    def modulate(self, pitches):
        self.modulation += pitches
        if self.modulation >= 12:
            self.modulation -= 12
        elif self.modulation <= -12:
            self.modulation +=12

    @property
    def tonic(self) -> int:
        return self.start_tonic + self.modulation


@dataclass
class OutCell(rain.MusicCell):
    _no_traverse_keys = rain.MusicCell._no_traverse_keys + ("scale",)

    #TODO: MAYBE the scale as separate node(s).. yay!!
    scale: rain.Scale = rain.Scale(steps=scale_steps)

    tonic_mod: Iterable = cycle((0,))

    # TODO MAYBE: implement this:
    # mode:int = 0 

    degree: Iterable = cycle((None,))

    octave: Iterable = cycle((0,))

    pitch: Callable[["OutCell", dict], int] = (
        lambda s, v: rain.transpose(
            s.scale.getitem_with_root(v["degree"], s.scale.root + v["tonic_mod"]), 
            octave=v["octave"]
            )
        )
rain.context.register_types(OutCell)

# TODO maybe... include this in the graph data structure?
@dataclass
class OutCellFactory():
    global_tonic:GlobalTonic = None
    mode:int = 0

    _base_scale = rain.Scale(steps=scale_steps)

    def modulate(self, pitches):
        self.global_tonic.modulate(pitches)

    def __call__(self, *args, **kwargs) -> OutCell:
        # tonic = kwargs.pop("tonic", self.tonic)
        return OutCell.create(
            # scale = self._base_scale.mode(self.mode) + tonic,
            scale = self._base_scale.mode(self.mode) + self.global_tonic.tonic,
            # tonic_mod = cycle((0,)),
            *args, **kwargs
            )


@dataclass
#TODO: ditto as above, can't represent this natively in a graph ... OK?
class AddDegrees(rain.AlterPattern):
    """
    """

    degrees: Iterable = cycle((None,))
    _degrees_iter = ()

    def add_degrees(self, vein_dict: dict) -> dict:
        return_dict = {}
        return_dict.update(vein_dict)

        current_degree = next(self._degrees_iter, None)

        if current_degree is not None:
            existing_degree = return_dict["degree"]
            if existing_degree is None:
                return_dict["degree"] = current_degree
            else:
                return_dict["degree"] = rain.listify(existing_degree, current_degree)
        return return_dict

    def __post_init__(self):
        super().__post_init__()
        self._degrees_iter = iter(self.degrees)
        self.vein_hooks = [lambda s, v: self.add_degrees(v)]

rain.context.register_types(AddDegrees)


@dataclass
#TODO: ditto as above, can't represent this natively in a graph ... OK?
class Mask(rain.AlterPattern):
    """
    """

    _mask_attrs = ("degree",)
    _mask_iter = ()

    mask: Iterable[bool] = cycle((True,))

    def mask_me(self, vein_dict: dict) -> dict:
        current_mask = next(self._mask_iter, True)

        if current_mask:
            return vein_dict
        else:
            return_dict = {}
            return_dict.update(vein_dict)           
            for attr in self._mask_attrs:
                return_dict[attr] = None
            return return_dict

    def __post_init__(self):
        super().__post_init__()
        self._mask_iter = iter(self.mask)
        self.vein_hooks = [lambda s, v: self.mask_me(v)]

rain.context.register_types(Mask)


@dataclass
#TODO: ditto as above, can't represent this natively in a graph ... OK?
class AdditiveModulation(rain.AlterPattern):
    """
    """

    pitches: int = 0

    def modulate_me(self, vein_dict: dict) -> dict:
        if self.pitches:
            return_dict = {}
            return_dict.update(vein_dict)
            return_dict["tonic_mod"] += self.pitches
            return return_dict
        else:
            return vein_dict

    def __post_init__(self):
        super().__post_init__()
        self.vein_hooks = [lambda s, v: self.modulate_me(v)]

rain.context.register_types(AdditiveModulation)

def add_modulate(global_tonic:GlobalTonic, key:str=None):
    return AdditiveModulation.create(key, pitches = global_tonic.modulation)