from dataclasses import dataclass
from itertools import cycle, repeat
from typing import Iterable

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, add_modulate)
from rain.out.score_machine import score_with_meter, rest_all
from rain import ref, par, seq, par_ref, seq_ref
from rain.score import meters

M = rain.MeddleHelper

# TODO: likely change start global tonic
burning_cell = OutCellFactory(mode=5, global_tonic=GlobalTonic(-5))
burning_tonic = GlobalTonic(-5)

# TODO: these are repeated in every movement... DRY
def mod_and_seq_return(pitches=5, *patterns):
    burning_tonic.modulate(pitches)
    return seq(*patterns).alter(add_modulate(burning_tonic))

def mod_and_seq(pitches=5, *patterns):
    BURNING.append(mod_and_seq_return(pitches, *patterns))

def space_intervals(s, v:dict):
    degree = v["degree"]
    if isinstance(degree, (list, tuple)) and len(degree)==2:
        return (max(degree), min(degree)+7)
    else:
        return degree

tiniest_degree=[(4,5),(2,3),(6,7)]
tiny_degree=[(4,5),(2,3),(6,7),2]

def chord_i(chord_seq, *indices):
    ret_list = []
    for c,i in zip(chord_seq, indices):
        if isinstance(c, (list, tuple)) and isinstance(i, int):
            ret_list.append( c[i] )
        else:
            ret_list.append(c)
    return ret_list

burning_cell("TINIEST_BURN_HI", degree=tiniest_degree, dur=cycle([0.5]), machine=cycle(["FLUTE"]))
burning_cell("TINIEST_BURN_LOW", degree=[-3,-4,-1], dur=cycle([0.5]), 
    tonic_mod=cycle([5])
    )

burning_cell("TINY_BURN_HI", degree=tiny_degree, dur=cycle([0.5]), tonic_mod=(0,0,0,5))
burning_cell("TINY_BURN_LOW", degree=[-3,-4,-4,-1], dur=cycle([0.5]), 
    tonic_mod=cycle([5])
    )

# b1 = burning_cell("B1",
#     degree=((0,6), -2),
#     dur=cycle((0.5, 1.5,)),
#     machine=cycle(("PIANO1",)),
#     tags =cycle((None,)),
# )

# burning_cell("BURNING")

BURNING = rain.Sequence.create()

BURNING.extend( par(
    OutCell("TINIEST_BURN_HI").change(
        degree=chord_i(tiniest_degree,None,1),
        octave=[0,1]
        )(degree=space_intervals, machine="PIANO1").tag(["mf"]),
    OutCell("TINIEST_BURN_LOW")(machine="PIANO2") #.tag(["treble"])
)(pitch_spell="FLAT"))

mod_and_seq(5, par(
    OutCell("TINIEST_BURN_HI").change(
        degree=chord_i(tiniest_degree,1,None,0),
        # octave=[0,0,-1]
        )(degree=space_intervals, machine="PIANO1"),
    OutCell("TINIEST_BURN_LOW").change(octave=[0,0,-1])(machine="PIANO2") 
)(pitch_spell="FLAT"))

mod_and_seq(-7, par(
    OutCell("TINIEST_BURN_HI").change(
        degree=chord_i(tiniest_degree,None,1,None),
        octave=[0,1,0]
        )(degree=space_intervals, machine="PIANO1"),
    OutCell("TINIEST_BURN_LOW")(machine="PIANO2") 
)(pitch_spell="FLAT"))

mod_and_seq(5, par(
    OutCell("TINIEST_BURN_HI")(degree=space_intervals, machine="PIANO1"),
    OutCell("TINIEST_BURN_LOW")(machine="PIANO2") 
)(pitch_spell="FLAT"))

mod_and_seq(-7, par(
    OutCell("TINIEST_BURN_HI")(degree=space_intervals, machine="PIANO1"),
    OutCell("TINIEST_BURN_LOW")(machine="PIANO2") 
)(pitch_spell="SHARP"))

mod_and_seq(5,par(
    OutCell("TINY_BURN_HI")(degree=space_intervals, machine="PIANO1"),
    OutCell("TINY_BURN_LOW")(machine="PIANO2") 
)(pitch_spell="SHARP"))

mod_and_seq(-7, par(
    OutCell("TINY_BURN_HI")(degree=space_intervals, machine="PIANO1"),
    OutCell("TINY_BURN_LOW")(machine="PIANO2") 
)(pitch_spell="SHARP"))


# BURNING = BURNING.meddle(
#     # M("TINIEST_BURN_LOW"),
#     M("TINY_BURN_HI")(dur=1).tag([">"])
# ).meddle(M("TINIEST_BURN_LOW", 0)(machine="FLUTE"))

# burning_tonic.modulate(5)


if __name__ == "__main__":
    score = score_with_meter()
    score.reset()
    pr = rain.PatternReader(BURNING, score.get_palette())
    pr.read()
    score.render("BURNING")