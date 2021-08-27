from itertools import cycle, repeat

from abjad.indicators.Fermata import Fermata

import rain

from rain.out.structures import OutCellFactory
freaking_cell = OutCellFactory(mode=3, tonic=4)

rain.Sequence.create("FREAKING_SEQ").extend(
    freaking_cell("FREAKING1", degree=(-4,-1,0,-1), dur=cycle((1,)) ),
    freaking_cell("FREAKING2", degree=(-3,-1,0,-1), dur=cycle((1,)) ),
    freaking_cell("FREAKING3", degree=(-3,-2,0,-2), dur=cycle((1,)) ),
    freaking_cell("FREAKING4", degree=(-3,-2,1,-2), dur=cycle((1,)) ),
)

freaking_bass1 = freaking_cell("FREAKING_BASS1", 
    degree=(-14, (-12, -7), -14, (-10, -7),),
    dur=cycle((1,)),
    tags=(["(", "bass"],[")"],["("],[")"],),
    )

freaking_bass2 = freaking_cell("FREAKING_BASS2", 
    degree=(-16, (-14, -9), -16, (-11, -9),),
    dur=cycle((1,)),
    tags=(["("],[")"],["("],[")"],),
    )

freaking_bass = rain.Sequence.create("FREAKING_BASS_SEQ").extend(
    freaking_bass1, freaking_bass2
)

freaking_par1 = rain.Parallel.create("FREAKING_PAR").extend(
    rain.Sequence("FREAKING_SEQ")(dur=0.5, machine="PIANO1"),
    freaking_bass(machine="PIANO2"),
)

 
FREAKING = rain.Sequence.create("FREAKING").extend(
    freaking_par1, 
    freaking_par1(pitch=lambda p: rain.transpose(p, 2))
)


if __name__ == "__main__":
    from rain.out.score_machine import OUT_SCORE
    OUT_SCORE.reset()
    pr = rain.PatternReader(FREAKING, OUT_SCORE.get_palette())
    pr.read()
    OUT_SCORE.render()