from itertools import cycle, repeat

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, AddDegrees, Mask,
    add_modulate)
from rain.out.score_machine import score_with_meter, rest_all
from rain import ref, par, seq, par_ref, seq_ref
from rain.score import meters

M = rain.MeddleHelper

# TODO: may want to change start global tonic
passing_cell = OutCellFactory(mode=2, global_tonic=GlobalTonic(3))
passing_tonic = GlobalTonic(3)

PASSING = rain.Sequence.create("PASSING")

# TODO: these are repeated in every movement... DRY
def mod_and_seq_return(*patterns):
    passing_tonic.modulate(-3)
    return seq(*patterns).alter(add_modulate(passing_tonic))

def mod_and_seq(*patterns):
    PASSING.append(mod_and_seq_return(*patterns))

seq("PASSING_SEQA",
    passing_cell("PASSING1", degree=(6, 3, 2, 1, 0, 3), dur=(0.5, 0.5, 0.5, 0.5, 0.5, 0.5,) ),
    passing_cell("PASSING2", degree=(2, 1, 0, 2, 1, 0,), dur=(0.5, 0.5, 0.5, 0.5, 0.5, 0.5,) ),
    passing_cell("PASSING3", degree=(1, 0, 1, (-2, -3)), dur=(0.5, 0.5, 1, 2.5,) ),
)

seq_ref("PASSING_SEQA").meddle("PASSING_SEQB",
    M("PASSING1").change(degree=[4]),
    M("PASSING2").alter_leaves(degree=(2, 1, 0)),
    M("PASSING3").alter_leaves(dur=(0.5, 0.5, 1, 1,)),
)

seq("PASSING_SEQ", 
    seq_ref("PASSING_SEQA"), 
    seq_ref("PASSING_SEQB")
    )

PASSING.append(
    seq_ref("PASSING_SEQ")(machine="PIANO1"),
    )

mod_and_seq(
    seq_ref("PASSING_SEQA")(machine="PIANO1"),
    )

mod_and_seq(
    seq_ref("PASSING_SEQB")(machine="PIANO2"),
    rest_all(3), # this is downward motion "LH" figure only
    )

mod_and_seq(
    seq_ref("PASSING_SEQB")(machine="PIANO2"),
    )

if __name__ == "__main__":
    score = score_with_meter(meters.METER_6_8)
    score.reset()
    pr = rain.PatternReader(PASSING, score.get_palette())
    pr.read()
    score.render()