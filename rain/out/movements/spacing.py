from itertools import cycle, repeat
# from rain.out.movements.freaking import FREAKING

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, add_modulate)
from rain.out.score_machine import score_with_meter, rest_all
from rain import ref, par, seq, par_ref, seq_ref

M = rain.MeddleHelper

# TODO: MAYBE change start global tonic?
spacing_cell = OutCellFactory(mode=0, global_tonic=GlobalTonic(8))
spacing_tonic = GlobalTonic(8)

SPACING = rain.Sequence.create("SPACING")

# TODO: these are repeated in every movement... DRY
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
    [],["("],["["],["]", ")"],["("],[")"],
    [], ["-","\<"],["("],[],[")"],["(","\>"],[")","\!"],
    [], ["("],["["],["]", ")"],  ["("],[")"],
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
        )(key="PIANO_RISE_H", machine="PIANO1"),
    spacing_cell("RISE_L", degree=([1,7],[-3,5],-2,-1,0), dur=(1,1,0.5,0.5,1)).tag(
        [], ["bass"], [], [], []).change(
            octave=[0,-2,-2,-1,-1]
        )(key="PIANO_RISE_L",machine="PIANO2")
)

#TODO MAYBE: try to cut some

#TODO FOR SURE... SING INTO FLUTE

SPACING.extend(
    # rest_all(6), # long tones, swells in electronics
    par(
        spacing_cell(dur=[0.5]*8, degree=[4,1,2,1]*2).tag(["(click track...)"])(machine="FLUTE"),
        spacing_cell(dur=[0.5]*8, degree=[4,1,2,1]*2).tag(["(click track...)"])(machine="PIANO1"),
    ).tag_all(["note_head:0:cross"]),
    par(
        # TODO: these are used later (at end, maybe elsewhere) .... DRY
        spacing_cell(degree=[0, 0, 0], dur=[2,2,2])(octave=1).tag(["pp"])(machine="PIANO1"),
        spacing_cell(degree=[0,1,6], dur=[2,2,2], octave=[-3, -1, -1]).tag([], [], ["treble"])(machine="PIANO2"),
    )(pitch_spell="SHARP"),
    par(
        # rest_all(2, "FLUTE") + 
        seq_ref("SPACING_SEQ_SLURRED").meddle(
            M("SPACING1").change(),
            M("SPACING2").change(dur=[1.5], octave=[0,0,1,1,1], degree=[None,1]),
            M("SPACING3").change(dur=[1.5]),
            ).tag([],["p"])(machine="FLUTE", pitch_spell="SHARP"),
        seq(
            par_ref("PIANO_TWINKLE").meddle(
                M("TWINKLE_H").tag([],["\<"])
            ),
            par(
                OutCell("PIANO_RISE_H").change(
                    dur=[2, 1.5, 0.5, 1], degree=[(0,2,4)],).tag(["p",],[],["(",],[")"], ["("], [")"]),
                OutCell("PIANO_RISE_L").change(
                    dur=[2, 1.5, 0.5, 1], degree=[1]),
            ),
            par_ref("PIANO_TWINKLE").meddle(
                M("TWINKLE_H").tag([],["\!"]),
                M("TWINKLE_L").tag([],["treble"])
            )
        )(pitch_spell="SHARP"),
    ),
    par(
        spacing_cell(degree=([-4,0],0), dur=[2,2,], octave=[2,2,]
            )(machine="PIANO1"),
        spacing_cell(degree=(0,0), dur=[2,2,], tonic_mod=[0,7]
            )(machine="PIANO2"),
    )(pitch_spell="SHARP"),
    # rest_all(2), # long tones, swells
)

# MEASURE 7 -------------------------------
mod_and_seq(
    par(
        seq_ref("SPACING_SEQ_SLURRED").meddle(
            M("SPACING1").change(dur=[False, 1.5, 1.5], octave=[0,-1,0,0,0,1], 
                tags=[[],["\<","("],[],[],[],["mp",")"]],
                leaf_durs=[None,None,None,None,None,(0.75,1)],
                degree=spacing_2_mod_degrees),
            M("SPACING3").change(
                dur=[False, False, 0.25,0.75,0.25,1.75],
                leaf_durs=[False, False, 0.25,0.75,0.25,(0.75,1)],
                octave=[0,0,0,1,1,1,],
                ).tag([],["\<"],[],[],[],[([],"mf")]),
            )(machine="FLUTE"),
        seq(
            par(
                seq(
                    spacing_cell(degree=([1,7],-2,-1,0), dur=[1,1,1,1], octave=[0,1,0,1]
                        ).tag([],[],["\<"]),
                    OutCell("SPACING1")(dur=0.5, leaf_durs=None).change(
                        octave=[0,0,1,1,0,1]).tag([],["("],[],[],[],[")"]),
                    )(machine="PIANO1"),
                spacing_cell(
                    degree=(-1,0,0,-1,-2,-3,[-4,4]), 
                    dur=[1]*7,
                    octave=(0,0,-1,-1,-2,-3,-3),
                    tags=([],[],[],[],["bass"],[],[])
                    )(machine="PIANO2")
            ),
            # TODO: DRY DRY!!!!!! ... almost the same as PIANO_RISE (just cropped off first quarter-note)
            # refactor with auto-cropping
            par("PIANO_RISE2",
                spacing_cell("RISE_H2", degree=([3,9],-1,0,1,0), dur=(1,0.5,0.5,0.5,0.5,) ).tag(
                    ["mp"], [], [], []).change(
                        octave=[0,0,1,0,1]
                    )(machine="PIANO1"),
                spacing_cell("RISE_L2", degree=([-3,5],-2,-1,0), dur=(1,0.5,0.5,1)).tag(
                    ["bass"], [], [], []).change(
                        octave=[-3,-2,-1,-1]
                    )(machine="PIANO2")
                ),
            par_ref("PIANO_TWINKLE").meddle(
                M("TWINKLE_H")(octave=1),
                M("TWINKLE_L").tag([],["treble"]),
            ),
            ),
    )(pitch_spell="SHARP"),
)

# TODO FOR SURE... GET THAT LEADING 5TH IN HERE

# MEASURE 12 ====================================================
final_phrase_dur=[0.5,0.5,1,1,1.5,3.5]
mod_and_seq(
    par(
        # seq_ref("SPACING_SEQ")(machine="FLUTE", pitch_spell="SHARP"),
        # NOTE: can't nest the modulations... messes up the outer mod (that's why using tonic_mod on here)
        seq(
            rest_all(2, "FLUTE"),
            # TODO: would be cleaner to define SPACING2 / SPACING3 above
            OutCell("SPACING2").change(   
                degree=[None, -7])(octave=1).tag(
                    [],["("],[],[],[],[],[")"]),
            OutCell("SPACING3").change(
                dur=final_phrase_dur,
                octave=[0,0,0,1,1,0]).tag(
                    [],["(","\>"],[")"],["("],[],[")","pp"],)
        )(machine="FLUTE"),
        seq(
            # TODO: add some tasteful doubling
            OutCell("SPACING1").change(
                dur=[0.5,0.5,0.25,0.75,0.5,1.5],
                leaf_durs=[0.5,0.5,0.25,0.75,0.5,(0.5,1)],
                octave=[1]*5+[0],
                ).tag([],["("]),
            spacing_cell(degree=[1],dur=[2],tags=[(")",)]),
            OutCell("TWINKLE_H").change(
                        degree=[None], dur=final_phrase_dur)(octave=1).tag([],["\>"]),
            spacing_cell(degree=[0, 0, 0], dur=[3.5,2,6], octave=[1,1,2]).tag(["pp"]),
            # rest_all(8, "PIANO1"), 
            # TODO: bring this back
            # seq_ref("SPACING_SEQ")(tonic_mod=7, machine="PIANO1", pitch_spell="FLAT"),
        )(machine="PIANO1"),
        seq(
            spacing_cell(degree=[0,-7,-14], dur=[2,2,2]).tag(
                [],["bass"]),
            OutCell("TWINKLE_L").change(
                dur=final_phrase_dur).tag([],["treble"]),
            # TODO: pedal or open tie from low bass note
            spacing_cell(degree=[0,1,6], dur=[3.5,2,6], octave=[-3, -1, -1]).tag(
                ["bass"], [], [("treble","|.")]),
            )(machine="PIANO2"),
    )(pitch_spell="SHARP"),
)

SPACING = SPACING.tag(["tempo:60:1:4:Aloof"])

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
    score.render("SPACING",
    stylesheets=["./rain-language/rain/score/stylesheets/stylesheet_title_spacing.ily"])