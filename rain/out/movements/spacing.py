from itertools import cycle, repeat
# from rain.out.movements.freaking import FREAKING

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, AddDegrees, Mask,
    add_modulate)
from rain.out.score_machine import score_with_meter, rest_all
from rain import ref, par, seq, par_ref, seq_ref

M = rain.MeddleHelper

# TODO: likely change start global tonic
spacing_cell = OutCellFactory(mode=0, global_tonic=GlobalTonic(8))
spacing_tonic = GlobalTonic(8)

SPACING = rain.Sequence.create("SPACING")

def mod_and_seq_return(*patterns):
    spacing_tonic.modulate(7)
    return seq(*patterns).alter(add_modulate(spacing_tonic))


def mod_and_seq(*patterns):
    SPACING.append(mod_and_seq_return(*patterns))

twinkle_degrees_h = [0,3,-1,[0,3]]
twinkle_degrees_l = [1,2,-2,0]
twinkle_dur = [0.5, 1, 1, 1, 0.5]
spacing_2_mod_degrees=[None, 1, 0, -1, -1, -2]

seq("SPACING_SEQ",
    spacing_cell("SPACING1", degree=[None, 1, 0, -2, -1, 0], 
        dur=[0.5, 0.5, 0.5, 0.5, 0.25, 1.75], 
        leaf_durs=[None,None,None,None,None,(0.75,1)] ),
    spacing_cell("SPACING2", degree=[None, -2, -5, -4, -3, 1, 0], dur=[0.5, 0.5, 0.25, 0.25, 0.25, 0.75, 1.5] ),
    spacing_cell("SPACING3", degree=[None, 0, -1, -2, -1, 0], dur=[0.5, 0.5, 0.5, 0.5, 1.5, 0.5] ),
).tag(
    [],["p", "("],["["],["]", ")"],["("],[")"],
    [], ["-","\<"],["("],[],[")"],["(","\>"],[")","\!"],
    [], ["("],[],[")"],  ["("],[")"],
    key="SPACING_SEQ_SLURRED"
)

par("PIANO_TWINKLE",
    spacing_cell("TWINKLE_H", degree=[0] + twinkle_degrees_h, dur=twinkle_dur).change(
        octave=[1,1,2,1,2],
        leaf_durs=(0.5, 1, [0.5,0.5],1,0.5)
        ).tag([], [], [], [], [])(machine="PIANO1"),
    spacing_cell("TWINKLE_L", degree=[None] + twinkle_degrees_l, dur=twinkle_dur).change(
        leaf_durs=(0.5, 1, [0.5,0.5],1,0.5)
        )(octave=0,)(machine="PIANO2")
)


par("PIANO_RISE",
    spacing_cell("RISE_H", degree=([2,4],[3,9],-1,0,1,0), dur=(1,1,0.5,0.5,0.5,0.5,) ).tag(
        [], [], [], [], []).change(
            octave=[1,1,0,0,1,1]
        )(machine="PIANO1"),
    spacing_cell("RISE_L", degree=([1,7],[-3,5],-2,-1,0), dur=(1,1,0.5,0.5,1)).tag(
        [], ["bass"], [], [], []).change(
            octave=[0,-2,-2,-1,-1]
        )(machine="PIANO2")
)

#TODO MAYBE: try to cut some
SPACING.extend(
    # rest_all(6), # long tones, swells in electronics
    par(
        spacing_cell(degree=[0, 0, 0], dur=[2,2,2])(octave=1).tag(["pp"])(machine="PIANO1"),
        # TODO: reuse this
        spacing_cell(degree=[0,1,6], dur=[2,2,2], octave=[-3, -1, -1]).tag([], [], ["treble"])(machine="PIANO2"),
    )(pitch_spell="SHARP"),
    par(
        # rest_all(2, "FLUTE") + 
        seq_ref("SPACING_SEQ_SLURRED").meddle(
            M("SPACING2").change(octave=[0,0,1,1,1], degree=[None,1]),
            )(machine="FLUTE", pitch_spell="SHARP"),
        seq(
            par_ref("PIANO_TWINKLE"),
            par_ref("PIANO_RISE"),
            par_ref("PIANO_TWINKLE").meddle(
                M("TWINKLE_L").tag([],["treble"])
            )
        )(pitch_spell="SHARP"),
    ),
    par(
        spacing_cell(degree=([-4,0],0), dur=[1,1,], octave=[2,2,]
            )(machine="PIANO1"),
        spacing_cell(degree=(0,0), dur=[1,1,], tonic_mod=[0,7]
            )(machine="PIANO2"),
    )(pitch_spell="SHARP"),
    # rest_all(2), # long tones, swells
)

# MEASURE 6 -------------------------------
mod_and_seq(
    par(
        seq_ref("SPACING_SEQ_SLURRED").meddle(
            M("SPACING1").change(dur=[False, 1.5, 1.5], octave=[0,-1,0,0,0,1], degree=spacing_2_mod_degrees),
            M("SPACING3").change(dur=[False, False,False,False,0.5,1.5],),
            )(machine="FLUTE"),
        seq(
            spacing_cell(degree=([1,7],-2,-1,0), dur=[1,1,1,1], octave=[0,1,0,1])(machine="PIANO1"),
            OutCell("SPACING1")(dur=0.5).change(octave=[0,0,1,1,0,1]).tag([],["("],[],[],[],[")"])(machine="PIANO1"),
            # TODO: DRY DRY!!!!!! ... almost the same as PIANO_RISE (just cropped off first quarter-note)
            # refactor with auto-cropping
            par("PIANO_RISE2",
                spacing_cell("RISE_H2", degree=([3,9],-1,0,1,0), dur=(1,0.5,0.5,0.5,0.5,) ).tag(
                    [], [], [], []).change(
                        octave=[0,0,1,0,1]
                    )(machine="PIANO1"),
                spacing_cell("RISE_L2", degree=([-3,5],-2,-1,0), dur=(1,0.5,0.5,1)).tag(
                    ["bass"], [], [], []).change(
                        octave=[-2,-2,-1,-1]
                    )(machine="PIANO2")
                )
            ),
    )(pitch_spell="SHARP"),
)

mod_and_seq(
    par(
        seq_ref("SPACING_SEQ")(machine="FLUTE", pitch_spell="SHARP"),
        # NOTE: can't nest the modulations... messes up the outer mod (that's why using tonic_mod on here)
        seq(
            rest_all(8, "PIANO1"), 
            seq_ref("SPACING_SEQ")(tonic_mod=7, machine="PIANO1", pitch_spell="FLAT"),
           
        ),
    ),
    rest_all(2) #rain.rest(2),
)

# mod_and_seq(
#     OutCell("SPACING_SEQ")(machine="FLUTE", pitch_spell="FLAT"),
#     rest_all(6),
# )
if __name__ == "__main__":
    score = score_with_meter(
        # piano2_clef="treble"
        )
    score.reset()
    pr = rain.PatternReader(SPACING, score.get_palette())
    pr.read()
    score.render()