from itertools import cycle, repeat

import rain
import abjad

b1 = rain.MusicCell.create("B1",
    pitch=((12,22), 8),
    dur=cycle((0.5, 1.5,)),
    machine=cycle(("PIANO1",)),
    tags =cycle((None,)),
)

# TODO.. make this a development of b1
b2 = rain.MusicCell.create("B2",
    pitch=((12,22), 8),
    dur=cycle((0.5, 1.5,)),
    machine=cycle(("PIANO1",)),
    tags =cycle((None,)),
)

BURNING = rain.Sequence.create("BURNING").extend(
    b1
)

if __name__ == "__main__":
    from rain.out.score_machine import OUT_SCORE
    OUT_SCORE.reset()
    pr = rain.PatternReader(BURNING, OUT_SCORE.get_palette())
    pr.read()
    OUT_SCORE.render()