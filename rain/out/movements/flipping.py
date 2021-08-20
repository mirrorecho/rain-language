from itertools import cycle, repeat

import rain
import abjad

FLIPPING = rain.Sequence.create("FLIPPING").extend(
    
)

if __name__ == "__main__":
    from rain.out.score_machine import OUT_SCORE
    OUT_SCORE.reset()
    pr = rain.PatternReader(FLIPPING, OUT_SCORE.get_palette())
    pr.read()
    OUT_SCORE.render()