from itertools import cycle, repeat

import rain
import abjad

PASSING = rain.Sequence.create("PASSING").extend(
    
)

if __name__ == "__main__":
    from rain.out.score_machine import OUT_SCORE
    OUT_SCORE.reset()
    pr = rain.PatternReader(PASSING, OUT_SCORE.get_palette())
    pr.read()
    OUT_SCORE.render()