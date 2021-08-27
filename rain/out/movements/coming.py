from itertools import cycle, repeat

import rain

from rain.out.structures import OutCellFactory
coming_cell = OutCellFactory(mode=4, tonic=6)

rain.Sequence.create("COMING_1").extend(
    coming_cell("COMING_A", degree=(None, 2, 3, 4), dur=(0.5, 0.5, 0.5, 2.5) ),
    coming_cell("COMING_B", degree=(None, 2, 3, 4, 5), dur=(0.5, 0.5, 0.5, 1.5, 3) ),
    coming_cell("COMING_C", degree=(None, 5, 7, 6, 5), dur=(1, 1, 1.5, 1.5, 2) ),
    coming_cell("COMING_D", degree=(7, 6, 4), dur=(1, 1, 5) ),
)

# rain.Sequence.create("COMING_2").extend_by_key(
#     "COMING_A", "COMING_B", "COMING_C", "COMING_D",
# )

COMING = rain.Sequence.create("COMING").extend(
    rain.Sequence("COMING_1")(machine="FLUTE"),
)

if __name__ == "__main__":
    from rain.out.score_machine import OUT_SCORE
    OUT_SCORE.reset()
    pr = rain.PatternReader(COMING, OUT_SCORE.get_palette())
    pr.read()
    OUT_SCORE.render()