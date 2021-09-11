from itertools import cycle, repeat
# from rain.out.movements.freaking import FREAKING

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, AddDegrees, Mask,
    add_modulate)
from rain.out.score_machine import score_with_meter, rest_all
from rain import ref, par, seq, par_ref, seq_ref

M = rain.MeddleHelper

# TODO: MAYBE change start global tonic?
coming_cell = OutCellFactory(mode=4, global_tonic=GlobalTonic(-5))
coming_tonic = GlobalTonic(-5)

COMING = rain.Sequence.create("COMING")

#TODO: what was this for???? 
# IMPORTANT_RHYTHM = (1, 1, 0.25, 0.25, 0.5, 1.5, 0.75, 0.25, 0.25, 0.5, 0.5,)

seq("COMING_1",
    coming_cell("COMING_A", degree=(None, 2, 3, 4), dur=(0.5, 0.5, 0.5, 2.5) ),
    coming_cell("COMING_B", degree=(None, 2, 3, 4, 5), dur=(0.5, 0.5, 0.5, 1.5, 3) ),
    coming_cell("COMING_C", degree=(None, 5, 7, 6, 5), dur=(1, 1, 1.5, 1.5, 2) ),
    coming_cell("COMING_D", degree=(7, 6, 4), dur=(1, 1, 5) ),
)

chord_seqa = [(1,4), (2,4), (3,4), (4,5)]
chord_seqb = [(4,7), (0,6), (4,5), (1,4)]

seq("OSTI_CHORDS", 
    coming_cell("CHORD1", degree=chord_seqa+chord_seqb, dur=cycle([2]))
)

COMING.extend(
    par(
        seq_ref("COMING_1")(machine="FLUTE"),
        rest_all(1, "PIANO1") + seq_ref("OSTI_CHORDS")(machine="PIANO1"),
        coming_cell(dur=[2]*8, degree=[0]*8)(octave=-1, machine="PIANO2")
    )
)

if __name__ == "__main__":
    score = score_with_meter()
    score.reset()
    pr = rain.PatternReader(COMING, score.get_palette())
    pr.read()
    score.render()