from itertools import cycle, repeat
# from rain.out.movements.freaking import FREAKING

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, AddDegrees, Mask,
    add_modulate)
from rain.out.score_machine import score_with_meter, rest_all

M = rain.MeddleHelper

# TODO: likely change start global tonic
spacing_cell = OutCellFactory(mode=0, global_tonic=GlobalTonic(8))
spacing_tonic = GlobalTonic(8)

SPACING = rain.Sequence.create("SPACING")

def mod_and_seq_return(*patterns):
    spacing_tonic.modulate(7)
    return rain.Sequence.create().extend(*patterns).alter(add_modulate(spacing_tonic))

def mod_and_seq(*patterns):
    SPACING.append(mod_and_seq_return(*patterns))

twinkle_degrees_h = [0,3,-1,[0,3]]
twinkle_degrees_l = [1,2,-2,0]
twinkle_dur = [0.5, 1, 1, 1, 2.5]


rain.Sequence.create("SPACING_SEQ").extend(
    # TODO: create SPACING1 MOD
    spacing_cell("SPACING1", degree=[None, 1, 0, -1, -1, -2], dur=[0.5, 0.5, 0.5, 0.5, 0.25, 1.75] ),
    spacing_cell("SPACING2", degree=[None, -2, -5, -4, -3, 1, 0], dur=[0.5, 0.5, 0.25, 0.25, 0.25, 0.75, 1.5] ),
    spacing_cell("SPACING3", degree=[None, 0, -1, -2, -1, 0], dur=[0.5, 0.5, 0.5, 0.5, 1.5, 0.5] ),
).tag(
    [],["p", "("],[],[")"],["("],[")"],
    [], ["-","\<"],["("],[],[")"],["(","\>"],[")","\!"],
    [], ["("],[],[")"],  ["("],[")"],
    key="SPACING_SEQ_SLURRED"
)

rain.Parallel.create("PIANO_TWINKLE").extend(
    spacing_cell("TWINKLE_H", degree=[0] + twinkle_degrees_h, dur=twinkle_dur).change(
        octave=[1,1,2,1,2]
        ).tag([], [], [], [], [])(machine="PIANO1"),
    spacing_cell("TWINKLE_L", degree=[None] + twinkle_degrees_l, dur=twinkle_dur)(
        octave=0
    )(machine="PIANO2")
)

# space1 = rain.Sequence.create("SPACE1").extend(
#     # rain.rest(0.5),
#     # rain.MusicCell("SPACEA") 
#     )

#TRY TO CUT SOME !!!!!!
SPACING.extend(
    # rest_all(6), # long tones, swells in electronics
    rain.Parallel.create().extend(
        spacing_cell(degree=[0, 0, 0], dur=[2,2,2])(octave=1).tag(["pp"])(machine="PIANO1"),
        spacing_cell(degree=[0,1,6], dur=[2,2,2], octave=[-3, -1, -1]).tag([], ["treble"])(machine="PIANO2"),
    )(pitch_spell="SHARP"),
    rain.Parallel.create().extend(
        # rest_all(2, "FLUTE") + 
        rain.Sequence("SPACING_SEQ_SLURRED")(machine="FLUTE", pitch_spell="SHARP"),
        rain.ref("PIANO_TWINKLE")(pitch_spell="SHARP")
    ),
    rest_all(2), # long tones, swells
)

mod_and_seq(
    rain.Sequence("SPACING_SEQ").change(dur=[False, 1.5, 1.5], octave=[0, -1])(machine="FLUTE", pitch_spell="SHARP"),
)

mod_and_seq(
    rain.Parallel.create().extend(
        rain.Sequence("SPACING_SEQ")(machine="FLUTE", pitch_spell="SHARP"),
        mod_and_seq_return(
            rest_all(8, "PIANO1"), 
            rain.Sequence("SPACING_SEQ")(machine="PIANO1", pitch_spell="FLAT"),
            
        ),
    ),
    rest_all(2) #rain.rest(2),
)

mod_and_seq(
    OutCell("SPACING2")(machine="FLUTE", pitch_spell="FLAT"),
    rest_all(6),
)
if __name__ == "__main__":
    score = score_with_meter(
        # piano2_clef="treble"
        )
    score.reset()
    pr = rain.PatternReader(SPACING, score.get_palette())
    pr.read()
    score.render()