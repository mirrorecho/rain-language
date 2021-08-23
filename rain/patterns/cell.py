from dataclasses import dataclass
from typing import Iterable
from itertools import cycle

import rain

@dataclass
class Cell(rain.Pattern):
    """
    each cell property value would be one of:
    int, float, str, or an iterable of one of those types (or nested iterable)
    """
    dur: Iterable = ()
    machine: Iterable = cycle((None,))
    simultaneous: bool = False
    tags: Iterable = cycle((None,))


    @property
    def veins(self) -> Iterable[dict]:
        keys, values = zip(*(
            (k, getattr(self, k))
            for k in self._properties_keys if k not in ("name", "simultaneous", "leaf_hooks", "vein_hooks")
            ))
        for zipped_values in zip(*values):
            return_dict = {k:v for k, v in zip(keys, zipped_values)}
            for h in self.vein_hooks:
                return_dict = h(self, return_dict)
            yield return_dict

    # def cyclize(self, obj):
    #     if isinstance(obj, (tuple, list, cycle)):
    #         return obj
    #     else:
    #         return 

# --------------------------------------------------------------------

@dataclass
class MusicCell(Cell):
    pitch: Iterable = cycle((None,))
    pitch_spell: Iterable[str] = cycle((None,),)

# --------------------------------------------------------------------

@dataclass
class Rest(MusicCell):
    pitch: Iterable = (None,)



