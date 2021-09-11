from itertools import cycle, repeat
from rain.patterns.machine import Machine

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, add_modulate)
from rain.out.score_machine import score_with_meter, rest_all
from rain import ref, par, seq, par_ref, seq_ref
from rain.score import meters

M = rain.MeddleHelper

# TODO: may want to change start global tonic
making_cell = OutCellFactory(mode=1, global_tonic=GlobalTonic(0))
making_tonic = GlobalTonic(0)

MAKING = rain.Sequence.create("MAKING")

# TODO: these are repeated in every movement... DRY
def mod_and_seq_return(pitches=2, *patterns):
    making_tonic.modulate(pitches)
    return seq(*patterns).alter(add_modulate(making_tonic))

def mod_and_seq(pitches=2, *patterns):
    MAKING.append(mod_and_seq_return(pitches, *patterns))

making_rhythm = [0.75]*4 + [0.25, 0.75]
making_rhythm_durs = (0.75, [0.25, 0.5], [0.5, 0.25], 0.75, 0.25, 0.75)
making_degrees1 = [2,0,5,0,3,2]
making_degrees2 = [1,0,2,0,3,4,]
making_degrees3 = [4,4,4,4,4,3]



def make_walk(key=None, degree=0, repeat_degree=7, repeats=(2,2,2,1,2,1,2)):
    degrees = []
    for rep in repeats:
        for r in range(rep):
            degrees.extend([degree,degree+2])
        degree += 1
    print(degrees)
    return making_cell(degree=degrees, dur=cycle([0.5])).tag_all(["["], ["]"])

# TODO: DRY
making_cell("MAKING1",
    degree=making_degrees1, dur=making_rhythm, leaf_durs=making_rhythm_durs).tag_all(
        ["("],[")"],key="MAKING1_SLURRED",
    )

OutCell("MAKING1").change(key="MAKING2", degree=making_degrees2).tag_all(
        ["("],[")"],key="MAKING2_SLURRED",
    )

OutCell("MAKING1").change(key="MAKING3", degree=making_degrees3).tag(
        [],[],[],[],["("],[")"],key="MAKING3_SLURRED",
    )

seq("MAKINGA_SLURRED", OutCell("MAKING1_SLURRED"), OutCell("MAKING2_SLURRED"), OutCell("MAKING3_SLURRED"),)

# =====================================================================

MAKING.extend(
    par(
        seq_ref("MAKINGA_SLURRED")(octave=1, machine="PIANO1"),
        make_walk()(octave=-1, machine="PIANO2") 
    )
)

mod_and_seq(-3,
    par(
        seq_ref("MAKINGA_SLURRED")(octave=1, machine="PIANO1"),
        make_walk()(machine="PIANO2") 
    ) 
)

MAKING = MAKING.tag(["tempo:126:1:4:Intense"])

if __name__ == "__main__":
    score = score_with_meter(
        # piano2_clef="treble"
        )
    score.reset()
    pr = rain.PatternReader(MAKING, score.get_palette())
    pr.read()
    score.render()