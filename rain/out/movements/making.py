from itertools import cycle, repeat
from rain.patterns.machine import Machine

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, add_modulate)
from rain.out.score_machine import score_with_meter, rest_all
from rain import ref, par, seq, par_ref, seq_ref
from rain.score import meters

M = rain.MeddleHelper

# TODO: may want to change start global tonic
making_cell = OutCellFactory(mode=1, global_tonic=GlobalTonic(0))
making_tonic = GlobalTonic(0)

MAKING = rain.Sequence.create("MAKING")

# TODO: these are repeated in every movement... DRY
def mod_and_seq_return(pitches=2, *patterns):
    making_tonic.modulate(pitches)
    return seq(*patterns).alter(add_modulate(making_tonic))

def mod_and_seq(pitches=2, *patterns):
    MAKING.append(mod_and_seq_return(pitches, *patterns))

making_rhythm = [0.75]*4 + [0.25, 0.75]
making_rhythm_durs = (0.75, [0.25, 0.5], [0.5, 0.25], 0.75, 0.25, 0.75)
making_rhythm_yo = [0.75, 0.75, 1, 0.5, 1]
making_rhythm_yo_durs = [0.75, [0.25, 0.5], [0.5, 0.5], 0.5, 1]
making_degrees1 = [2,0,5,0,3,2]
making_degrees2 = [1,0,2,0,3,4,]
making_degrees3 = [4,4,4,4,4,3]



def make_walk(key=None, degree=0, step_degree=2, walk_degree=1, repeats=(2,2,2,1,2,1,2)):
    degrees = []
    tags=[]
    for rep in repeats:
        for r in range(rep):
            degrees.extend([degree,degree+step_degree])
        tags.append(["("])
        for i in range(rep*2-2):
            tags.append([])
        tags.append([")"])
        degree += walk_degree
    return making_cell(degree=degrees, tags=tags, dur=cycle([0.5])).tag_all(["[",], ["]",])

# TODO: DRY
making_cell("MAKING1",
    degree=making_degrees1, dur=making_rhythm, leaf_durs=making_rhythm_durs).tag_all(
        ["("],[")"],key="MAKING1_SLURRED",
    )

OutCell("MAKING1").change(key="MAKING2", degree=making_degrees2).tag_all(
        ["("],[")"],key="MAKING2_SLURRED",
    )

OutCell("MAKING1").change(key="MAKING3", degree=making_degrees3).tag(
        [],[],[],[],["("],[")"],key="MAKING3_SLURRED",
    )

making_cell(degree=[0,-3,-5], dur=[1,1,1]).tag_all("-", key="MAKING_DOWN")

jig_rhythm=making_rhythm[:2]+[0.5,0.5,0.5]
making_cell(
    degree=cycle([3,1]), dur=jig_rhythm,
    ).change(key="MAKING_JIG", leaf_durs=[0.75])

def making_whole(degree=0, octave=0, dur=4, key=None):
    return making_cell(key=key, degree=[degree], octave=[octave], dur=[dur])

seq("MAKINGA_SLURRED", OutCell("MAKING1_SLURRED"), OutCell("MAKING2_SLURRED"), OutCell("MAKING3_SLURRED"),)

# TODO: would be REALLY COOL to vary the number of reps here
making_cell(dur=[0.5]*8, degree=[None]+[-1]*7).tag(
    [],["-"],["-"],["-"],["-"],["-"],["-",">"],[".", ">"]).tag_all("[", "]", 
    key="MAKING_TENSE")
tense_dyn = [],["mp", "\<"],[],[],[],[],[],["f"]

# =====================================================================

MAKING.extend(
    par(
        making_cell(dur=[1,1,1,1], degree=[7,4,7,4]).tag(["(click track...)"])(machine="FLUTE"),
        making_cell(dur=[1,1,1,1], degree=[7,4,7,4]).tag(["(click track...)"])(machine="PIANO1"),
    ).tag_all(["note_head:0:cross"]),

    par(
        seq_ref("MAKINGA_SLURRED").tag(["p"])(octave=1, machine="PIANO1"),
        make_walk()(octave=-1, machine="PIANO2") 
    )
)

# TODO: WARNING WARNIGN!!!!!
# making_tonic.modulate(-3)

mod_and_seq(-3,
    par(
        seq(
            rest_all(8, "FLUTE"),
            making_whole(-1, octave=2).tag(["p","\<"]),
            OutCell("MAKING_JIG").tag(["mf"])(octave=2),
            rest_all(1, "FLUTE"),
            )(machine="FLUTE"),
        #TODO: consider changing the end of this:            
        seq(
            seq_ref("MAKINGA_SLURRED").change(
                octave=[1,2,1,2,1,1,1,2,1,]+[2]*9,
                ).tag([],[],[],[],[],[],[],[],[],[],[],[],["\<"],),
            making_whole(-1, octave=2).tag(["mf"])
            )(machine="PIANO1"),
        seq(
            make_walk(degree=2).tag(["treble"]),
            making_whole((-3,4), octave=1),
            )(machine="PIANO2") 
    )(pitch_spell="SHARP")
)

# MEASURE 8 =============================================
# TODO: WARNING WARNIGN!!!!!
# making_tonic.modulate(6)

mod_and_seq(6,
    par(
        seq(
            rest_all(1, "FLUTE"),
            OutCell("MAKING_DOWN")(octave=2),
            rest_all(4, "FLUTE"),
            making_whole(3, octave=1).tag(["p","\<"]),
            OutCell("MAKING_JIG").tag(["mf"])(octave=1),
            )(machine="FLUTE"),
        # TODO: vary up these walks a little bit
        seq(
            making_cell(degree=[None,(0,2,4)], dur=[1,3]).tag([], ["bass"]),
            make_walk()(octave=-2),
            )(octave=-1, machine="PIANO1"),
        seq(
            making_cell(dur=[4], degree=[(0,7)], octave=[-3]).tag(["bass"]),
            make_walk()(octave=-2),
            )(machine="PIANO2")
    )(pitch_spell="FLAT")
)

# MEASURE 12 =============================================
# TODO: WARNING WARNIGN!!!!!
# making_tonic.modulate(-3)

mod_and_seq(-3,
    par(
        seq(
            OutCell("MAKING_JIG")(octave=1), rest_all(1, "FLUTE"),
            OutCell("MAKING_JIG")(octave=1), rest_all(1, "FLUTE"),
            making_whole(-1, octave=2).tag(["p","\<"]),
            making_cell(degree=[3,1, None], dur=[0.75, 2.25, 1])(octave=2).change(leaf_durs=[0.75]),
            #TODO: add the above to the graph so this can be DRY
            making_cell(degree=[3,1, None], dur=[0.75, 2.25, 1])(octave=2).change(leaf_durs=[0.75]),
            )(machine="FLUTE"),
        #TODO: consider changing the end of this:            
        seq(
            make_walk(degree=2).tag(["treble"])(octave=0),
            making_whole((-1,4), octave=1),
            making_whole((-1,4), octave=1),
            )(machine="PIANO1") ,
        seq(
            make_walk(degree=2)(octave=-1),
            making_whole((-3,4), octave=0),
            making_whole((-3,4), octave=0),
            )(machine="PIANO2") 
    )(pitch_spell="FLAT")
)

# MEASURE 15 =============================================
mod_and_seq(-3,
    par(
        seq(
            OutCell("MAKING1_SLURRED").change(octave=[2,2,1,2,1,1]),
            OutCell("MAKING2_SLURRED").alter_leaves(dur=making_rhythm[:2])(octave=1),
            making_cell(degree=[2, None], dur=[1.5,1])
        )(machine="FLUTE"),
        seq(
            making_whole((-2,4), octave=1),
            making_whole((-1,4), octave=1, dur=8),
            )(machine="PIANO1"),
        seq(
            making_whole((0,4), octave=0),
            making_whole((0,4), octave=0, dur=8),
            )(machine="PIANO2"),
    )(pitch_spell="SHARP"),
    # MEASURE 20 =============================================
    par(
        seq(
            rest_all(10, "FLUTE"),
            making_cell(degree=[1, 6], dur=[1.5,0.5])(octave=2).tag(["mf","\<"], ["f", ">", "."])
        )(machine="FLUTE"),
        # TODO: consider not having octaves doubled on ALL of these
        seq(
            OutCell("MAKING1").alter_leaves(
                dur=making_rhythm_yo, leaf_durs=making_rhythm_yo_durs
                ).change(octave=[1,1,0,1,1]
                ).add_chord_degree(*([7]*6)).tag_all("-"),
            OutCell("MAKING2").alter_leaves(
                dur=making_rhythm_yo, leaf_durs=making_rhythm_yo_durs
                ).change(degree=[False]*4 + [None],
                ).add_chord_degree(*([7]*4))(octave=1).tag_all("-"),
            OutCell("MAKING_TENSE").change(
                degree=[None]+ [(-2,0,5)]*3 + [(-1,1,6)]*4)(octave=1).tag(*tense_dyn)
            )(machine="PIANO1"),
        seq(
            making_cell(dur=[1]*4, degree=[(0,4)]*4).tag_all("-"),
            making_cell(dur=[1]*4, degree=[(1,5)]*4).tag_all("-"),
            OutCell("MAKING_TENSE").change(
                degree=[None]+ [(-3,4)]*2 + [(-3,3)]*5)(octave=-1)
            )(machine="PIANO2"),
    )(pitch_spell="SHARP")
)

# MEASURE 23 =============================================
mod_and_seq(-3,
    par(
        seq(
            rest_all(1, "FLUTE"), OutCell("MAKING_DOWN")(octave=3),
            OutCell("MAKING2").alter_leaves(
                dur=making_rhythm_yo, leaf_durs=making_rhythm_yo_durs
                ).change(degree=[None, None])(octave=2).tag_all("-"),
            OutCell("MAKING3").alter_leaves(
                dur=making_rhythm_yo, leaf_durs=making_rhythm_yo_durs
                )(octave=2).tag_all("-"),
        )(machine="FLUTE"),
        seq(
            making_cell(degree=[None,(0,2,4)], dur=[1,3])(octave=1),
            rest_all(1, "PIANO1"), make_walk(repeats=[1]*7)(octave=1),
            )(machine="PIANO1"),
        seq(
            rest_all(1, "PIANO2") + OutCell("MAKING_DOWN").add_chord_degree(-7,-7,-7),
            rest_all(1, "PIANO2"), make_walk(repeats=[1]*7)(octave=-1),
        )(machine="PIANO2"),
    )(pitch_spell="SHARP")
)

# MEASURE 26 =============================================
# TODO: this would be better if it could continue gracefully
mod_and_seq(-6,
    par(
        # TODO: FLUTE REALLY shouldn't be resting here?
        seq(
            rest_all(8, "FLUTE"),
            OutCell("MAKING_TENSE")(octave=2).tag(*tense_dyn)
            )(machine="FLUTE"),
        seq(
            rest_all(1, "PIANO1"), make_walk(degree=4, repeats=[1]*7),
            OutCell("MAKING_TENSE").change(
                degree=[None]+ [(-2,0,5)]*3 + [(-1,1,6)]*4)(octave=1).tag(*tense_dyn),
            rest_all(4, "PIANO1"),
# TODO ADD RIT at end
            making_cell(degree=[0,2,4]*5+[0], 
                octave=[-1,-1,-1,0,0,0,1,1,1,2,2,2,3,3,3,4], 
                dur=[0.5]*15+[4.5]
                ).tag(["bass", "(","\>"],[],[],[],["treble"],[],[],[],[],[],[],[],["8va"],
                    [],[],["8va!", "p", ")"],),
            )(machine="PIANO1"),
        seq(
            rest_all(1, "PIANO2"), make_walk(degree=4, repeats=[1]*7)(octave=-2),
            OutCell("MAKING_TENSE").change(
                degree=[None]+ [(-3,4)]*2 + [(-3,3)]*5)(octave=-1),
            rest_all(3, "PIANO2"),
            making_whole(dur=13)(octave=-3).add_chord_degree(7).tag([">"])
            )(machine="PIANO2"),
    )
)


MAKING = MAKING.tag(["tempo:96:1:4:Intense"])

if __name__ == "__main__":
    score = score_with_meter(
        # piano2_clef="treble"
        )
    score.reset()
    pr = rain.PatternReader(MAKING, score.get_palette())
    pr.read()
    score.render("MAKING",
    stylesheets=["./rain-language/rain/score/stylesheets/stylesheet_title_making.ily"])