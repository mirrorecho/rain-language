from itertools import cycle, repeat

import rain
import abjad




REACHING = rain.Sequence.create("REACHING").extend(
    
)

if __name__ == "__main__":
    from rain.out.score_machine import OUT_SCORE
    OUT_SCORE.reset()
    pr = rain.PatternReader(REACHING, OUT_SCORE.get_palette())
    pr.read()
    OUT_SCORE.render()