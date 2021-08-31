from itertools import cycle, repeat

import rain

from rain.out.out_cell import OutCell, OutCellFactory
from rain.out.score_machine import score_with_meter, rest_all

start_tonic = -2 # TODO: likely change this
flipping_cell = OutCellFactory(mode=6, tonic=start_tonic)

flip_tags_2 = (["("], [], [".", ">", ")"])

rain.Sequence.create("FLIPPING_GESTURE1_SEQ").extend(
    flipping_cell("FLIPPING1", degree=(0,2,4), dur=(0.5,0.5,0.25), 
        tags=(["."], [">", "("], [".", ")"]),
        ),
    flipping_cell("FLIPPING2", degree=(1,3,5), dur=(0.25,0.25,0.25),
        tags=flip_tags_2,
        ),
)

flipping_cell("FLIPPING_4THS_0", degree=cycle( ((0,3,6),) ), dur=(0.5,), tags=cycle(((">",),)) ),

rain.Sequence.create("FLIPPING_BASS1_SEQ").extend(
    flipping_cell("FLIPPING_BASS1", degree=(0,0,), dur=(0.5,0.75),
        tags=(["."], [">"])
        ),
    rain.Cell("FLIPPING1").alter_leaves(tags=flip_tags_2)(dur=0.25),
)


rain.Parallel.create("FLIPPING_PAR_P1").extend(
    rain.Sequence("FLIPPING_GESTURE1_SEQ")(octave=1, machine="PIANO1"),
    rain.Sequence("FLIPPING_BASS1_SEQ")(machine="PIANO2"),
)

FLIPPING = rain.Sequence.create("FLIPPING").extend(
    rain.Parallel("FLIPPING_PAR_P1")(pitch_spell="FLAT"),
    rain.rest(0.5)(machine="PIANO1"),
    rain.Cell("FLIPPING_4THS_0")(octave=1, machine="PIANO1"),
    rain.rest(1)(machine="PIANO1"),
    rain.Cell("FLIPPING_4THS_0").alter_leaves(dur=(0.25,0.25))(octave=1, machine="PIANO1"),
    rain.rest(1.5)(machine="PIANO1"),
    rain.Parallel("FLIPPING_PAR_P1")(pitch_spell="FLAT"),
)

if __name__ == "__main__":
    score = score_with_meter()
    score.reset()
    pr = rain.PatternReader(FLIPPING, score.get_palette())
    pr.read()
    score.render()