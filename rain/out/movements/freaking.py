from itertools import cycle, repeat

from abjad.indicators.Fermata import Fermata

import rain


# freaking = rain.Sequence.create("FREAKING_SEQ").extend_by_key(
#     "FREAKING1", "FREAKING2", "FREAKING3", "FREAKING4", 
# )

freaking = rain.Sequence.create("FREAKING_SEQ").extend(
    rain.MusicCell.create("FREAKING1", pitch=(-2,3,4,3), dur=cycle((1,)) ),
    rain.MusicCell.create("FREAKING2", pitch=(0,3,4,3), dur=cycle((1,)) ),
    rain.MusicCell.create("FREAKING3", pitch=(0,1,4,1), dur=cycle((1,)) ),
    rain.MusicCell.create("FREAKING4", pitch=(0,1,6,1), dur=cycle((1,)) ),
)

freaking_bass1 = rain.MusicCell.create("FREAKING_BASS1", 
    pitch=(-20, (-16, -8), -20, (-12, -8),),
    dur=cycle((1,)),
    tags=(["(", "bass"],[")"],["("],[")"],),
    )

freaking_bass2 = rain.MusicCell.create("FREAKING_BASS2", 
    pitch=(-23, (-20, -11), -23, (-14, -11),),
    dur=cycle((1,)),
    tags=(["("],[")"],["("],[")"],),
    )

freaking_bass = rain.Sequence.create("FREAKING_BASS_SEQ").extend(
    freaking_bass1, freaking_bass2
)

freaking_par1 = rain.Parallel.create("FREAKING_PAR").extend(
    freaking(dur=0.5, machine="PIANO1"),
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