from itertools import cycle, repeat

import rain

from rain.out.out_cell import OutCell, OutCellFactory
from rain.out.score_machine import score_with_meter, rest_all

start_tonic = 8
spacing_cell = OutCellFactory(mode=0, tonic=start_tonic)

space_a = rain.MusicCell.create("SPACEA_CHORD", pitch=((12, 25), (13, 24)), dur=cycle((1,)) )
space_b = rain.MusicCell.create("SPACEB_CHORD", pitch=((-2, 12), (0, 10)), dur=cycle((2,)) )


rain.Sequence.create("SPACING_SEQ").extend(
    spacing_cell("SPACING1", degree=(None, 1, 0, -1, -1, -2), dur=(0.5, 0.5, 0.5, 0.5, 0.25, 1.75) ),
    spacing_cell("SPACING2", degree=(None, -2, -5, -4, -3, 1, 0), dur=(0.5, 0.5, 0.25, 0.25, 0.25, 0.75, 1.5) ),
    spacing_cell("SPACING3", degree=(None, 0, -1, -2, -1, 0), dur=(0.5, 0.5, 0.5, 0.5, 1.5, 0.5) ),
)


# space1 = rain.Sequence.create("SPACE1").extend(
#     # rain.rest(0.5),
#     # rain.MusicCell("SPACEA") 
#     )

#TRY TO CUT SOME !!!!!!
SPACING = rain.Sequence.create("SPACING").extend(
    rest_all(6), # long tones, swells
    rain.Sequence("SPACING_SEQ")(machine="FLUTE", pitch_spell="SHARP"),
    rest_all(2), # long tones, swells
    rain.Sequence("SPACING_SEQ")(machine="FLUTE", pitch_spell="SHARP", tonic=start_tonic+7),
    rain.Parallel.create().extend(
        rain.Sequence("SPACING_SEQ")(machine="FLUTE", pitch_spell="SHARP", tonic=start_tonic+2),
        rain.Sequence.create().extend(
            rain.rest(8),
            rain.Sequence("SPACING_SEQ")(machine="PIANO1", pitch_spell="FLAT", tonic=start_tonic+9)
        ),
    ),
    rain.rest(2),
    OutCell("SPACING2")(machine="FLUTE", pitch_spell="FLAT", tonic=start_tonic+9),
    rain.rest(6),
)

if __name__ == "__main__":
    score = score_with_meter()
    score.reset()
    pr = rain.PatternReader(SPACING, score.get_palette())
    pr.read()
    score.render()