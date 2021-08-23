from itertools import cycle, repeat

import rain
import abjad

space_a = rain.MusicCell.create("SPACEA", pitch=((12, 25), (13, 24)), dur=cycle((1,)) )

space_b = rain.MusicCell.create("SPACEB", pitch=((-2, 12), (0, 10)), dur=cycle((2,)) )



space1 = rain.Sequence.create("SPACE1").extend(
    rain.MusicCell("SPACEA")
)

SPACING = rain.Sequence.create("SPACING").extend(
    space1(machine="PIANO1", pitch_spell="FLAT")
)

if __name__ == "__main__":
    from rain.out.score_machine import OUT_SCORE
    OUT_SCORE.reset()
    pr = rain.PatternReader(SPACING, OUT_SCORE.get_palette())
    pr.read()
    OUT_SCORE.render()