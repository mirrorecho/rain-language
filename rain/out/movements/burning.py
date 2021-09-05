from dataclasses import dataclass
from itertools import cycle, repeat
from typing import Iterable

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, AddDegrees, Mask,
    add_modulate)
from rain.out.score_machine import score_with_meter, rest_all

M = rain.MeddleHelper


# TODO: likely change start global tonic
burning_cell = OutCellFactory(mode=5, global_tonic=GlobalTonic(-4))
burning_tonic = GlobalTonic(-4)

# current_tonic = start_tonic # TODO: keep this?????

def space_intervals(s, v:dict):
    degree = v["degree"]
    if isinstance(degree, (list, tuple)) and len(degree)==2:
        return (max(degree), min(degree)+7)
    else:
        return degree


burning_cell("TINIEST_BURN_HI", degree=[(4,5),(2,3),(6,7)], dur=cycle([0.5]), machine=cycle(["FLUTE"]))
burning_cell("TINIEST_BURN_LOW", degree=[-3,-4,-1], dur=cycle([0.5]), tonic_mod=cycle([5]))
# burning_cell.modulate(5)
burning_cell("TINY_BURN_HI", degree=[(4,5),(2,3),(6,7),2], dur=cycle([0.5]), tonic_mod=(0,0,0,5))
burning_cell("TINY_BURN_LOW", degree=[-3,-4,-4,-1], dur=cycle([0.5]), tonic_mod=cycle([5]))

# b1 = burning_cell("B1",
#     degree=((0,6), -2),
#     dur=cycle((0.5, 1.5,)),
#     machine=cycle(("PIANO1",)),
#     tags =cycle((None,)),
# )
rain.Parallel.create("TINIEST_BURN").extend(
    rain.ref("TINIEST_BURN_HI")(degree=space_intervals, machine="PIANO1"),
    rain.ref("TINIEST_BURN_LOW")(machine="PIANO2") 
    )

BURNING = rain.Sequence.create()

for i in range(3):
    BURNING.append(rain.ref("TINIEST_BURN").alter(add_modulate(burning_tonic)))
    burning_tonic.modulate(5)

for i in range(2):
    BURNING.append(rain.Parallel.create().extend(
            rain.ref("TINY_BURN_HI")(degree=space_intervals, machine="PIANO1"),
            rain.ref("TINY_BURN_LOW")(machine="PIANO2") 
            ).alter(add_modulate(burning_tonic)))
    burning_tonic.modulate(5)

# rain.ref("BURNING")("BURNING_MOD",
#     rain.Meddle("TINIEST_BURN"),
#     rain.Meddle("TINY_BURN_LOW"),
#     )

mh = M("TINIEST_BURN_LOW", 0)

BURNING = BURNING.meddle(
    M("TINIEST_BURN_LOW", 0)(dur=4),
    M("TINY_BURN_HI")(dur=1).tag([">"])
).meddle(M("TINIEST_BURN_LOW", 0)(machine="FLUTE"))

print("0000000000000000000000000000000000000000000000000")


# for c in BURNING.get_descendant_cues():
#     print(c.cues_pattern.key, "CUE EXISTS", c.key)


# print(BURNING.ref("TINY_BURN_LOW"))

# BURNING.alter_sub("TINY_BURN_LOW", )

# for n in BURNING.nodes:
#     print(type(n).__name__, n.key)


# BURNING.append(rain.Parallel.create().extend(
#         rain.ref("TINY_BURN_HI")(degree=space_intervals, machine="PIANO1"),
#         rain.ref("TINY_BURN_LOW")(machine="PIANO2") 
#         ).alter(add_modulate(burning_tonic)))
# burning_tonic.modulate(5)
# BURNING.append(rain.Parallel.create().extend(
#         rain.ref("TINY_BURN_HI")(degree=space_intervals, machine="PIANO1"),
#         rain.ref("TINY_BURN_LOW")(machine="PIANO2") 
#         ).alter(add_modulate(burning_tonic)))

# BURNING = rain.Sequence.create("BURNING").extend(
# ,
#     rain.Parallel.create().extend(
#         rain.ref("TINIEST_BURN_HI")(tonic=current_tonic+5)(degree=space_intervals, machine="PIANO1"),
#         rain.ref("TINIEST_BURN_LOW")(tonic=current_tonic+10, machine="PIANO2")
#         ).change(degree=(0,0), dur=(1,)),
#     # rain.Parallel("TINIEST_BURN"),
#     # rain.Parallel("TINIEST_BURN")(tonic=current_tonic+5),
# ).alter(AddDegrees.create(degrees=(0, None, 0) ))
# # )

if __name__ == "__main__":
    score = score_with_meter()
    score.reset()
    pr = rain.PatternReader(BURNING, score.get_palette())
    pr.read()
    score.render()