from itertools import cycle, repeat

import rain

from rain.out.out_cell import OutCell, OutCellFactory
from rain.score import meters
from rain.out.score_machine import score_with_meter, rest_all

start_tonic = 3 # TODO: likely change this
passing_cell = OutCellFactory(mode=2, tonic=start_tonic)

rain.Sequence.create("PASSING_SEQA").extend(
    passing_cell("PASSING1", degree=(6, 3, 2, 1, 0, 3), dur=(0.5, 0.5, 0.5, 0.5, 0.5, 0.5,) ),
    passing_cell("PASSING2", degree=(2, 1, 0, 2, 1, 0,), dur=(0.5, 0.5, 0.5, 0.5, 0.5, 0.5,) ),
    passing_cell("PASSING3", degree=(1, 0, 1, (-2, -3)), dur=(0.5, 0.5, 1, 2.5,) ),
)

rain.Sequence.create("PASSING_SEQB").extend(
    OutCell("PASSING1").alter_leaves(degree=(4, 3, 2, 1, 0, 3)), # TODO: would be more elegant to only change the first degree
    OutCell("PASSING2").alter_leaves(degree=(2, 1, 0)),
    OutCell("PASSING3").alter_leaves(dur=(0.5, 0.5, 1, 1,)),
)

rain.Sequence.create("PASSING_SEQ").extend_by_key("PASSING_SEQA", "PASSING_SEQB")


PASSING = rain.Sequence.create("PASSING").extend(
    rain.Sequence("PASSING_SEQ")(machine="PIANO1"),
    rain.Sequence("PASSING_SEQA")(tonic=start_tonic-3, machine="PIANO1"),
    rain.Sequence("PASSING_SEQB")(tonic=start_tonic-6, machine="PIANO2").tag(["bass"]),
    rain.rest(3), # this is downward motion "LH" figure only
    rain.Sequence("PASSING_SEQB")(tonic=start_tonic-9, machine="PIANO2"),
)

if __name__ == "__main__":
    score = score_with_meter(meters.METER_6_8)
    score.reset()
    pr = rain.PatternReader(PASSING, score.get_palette())
    pr.read()
    score.render()