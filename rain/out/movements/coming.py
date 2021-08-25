from itertools import cycle, repeat

import rain

rain.Sequence.create("COMING_1").extend(
    rain.MusicCell.create("COMING_A", pitch=(None, -2, 0, 1), dur=(0.5, 0.5, 0.5, 2.5) ),
    rain.MusicCell.create("COMING_B", pitch=(None, -2, 0, 1, 3), dur=(0.5, 0.5, 0.5, 1.5, 3) ),
    rain.MusicCell.create("COMING_C", pitch=(None, 3, 6, 4, 3), dur=(1, 1, 1.5, 1.5, 2) ),
    rain.MusicCell.create("COMING_D", pitch=(6, 4, 1), dur=(1, 1, 5) ),
)

rain.Sequence.create("COMING_2").extend_by_key(
    "COMING_A", "COMING_B", "COMING_C", "COMING_D",
)

COMING = rain.Sequence.create("COMING").extend(
    rain.Sequence("COMING_1")(machine="FLUTE")
)

if __name__ == "__main__":
    from rain.out.score_machine import OUT_SCORE
    OUT_SCORE.reset()
    pr = rain.PatternReader(COMING, OUT_SCORE.get_palette())
    pr.read()
    OUT_SCORE.render()