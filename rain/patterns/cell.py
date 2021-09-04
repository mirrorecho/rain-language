from dataclasses import dataclass
from typing import Callable, Iterable
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
    tags: Iterable[Iterable[str]] = cycle( ( (),) )

    _no_traverse_keys = ("name", "simultaneous", "node_hooks", "leaf_hooks", "vein_hooks")


    @property
    def veins(self) -> Iterable[dict]:

        #TODO maybe: approach below is less elegant than what's commented out below, but works

        keys = [k for k in self._properties_keys if k not in self._no_traverse_keys]
        
        iterable_keys = []
        iterable_values = []
        callable_keys = []
        callable_values = []

        for k in keys:
            # NOTE... using the leaves attribute
            v = getattr(self, k)
            if isinstance(v, Callable):
                callable_keys.append(k)
                callable_values.append(v)
            else:
                iterable_keys.append(k)
                iterable_values.append(v)

        for zipped_iterable_values in zip(*iterable_values):
            return_dict = {k:v for k, v in zip(iterable_keys, zipped_iterable_values)}

            for h in self.vein_hooks:
                return_dict = h(self, return_dict)

            for k, c in zip(callable_keys, callable_values):
                # print(return_dict)
                return_dict[k] = c(self, return_dict)

            yield return_dict


        # keys, values = zip(*(
        #     (k, getattr(self, k))
        #     for k in self._properties_keys if k not in ("name", "simultaneous", "leaf_hooks", "vein_hooks")
        #     ))
        # for zipped_values in zip(*values):
        #     return_dict = {k:v for k, v in zip(keys, zipped_values)}

        #     for h in self.vein_hooks:
        #         return_dict = h(self, return_dict)
        #     yield return_dict

# --------------------------------------------------------------------

@dataclass
class MusicCell(Cell):
    pitch: Iterable = cycle((None,))
    pitch_spell: Iterable[str] = cycle((None,),)

# --------------------------------------------------------------------

@dataclass
class RestCell(MusicCell):
    pitch: Iterable = (None,)



