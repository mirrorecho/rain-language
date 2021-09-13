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

def tongue(end_degree=None,):
    return making_cell(
        degree=[2,0,None, end_degree],
        dur=[0.75, 2.75, 0.5] if end_degree is None else [0.75, 1.75, 0.5, 1],
        leaf_durs=[0.75, (0.25,2,0.5),0.5] if end_degree is None else [0.75, (0.25,1,0.5), 0.5, 1]
        ).tag_all_notes([":32"])(machine="FLUTE")

def whole_tongue(degree=0):
    return making_cell(
        degree=[degree],
        dur=[4],
        ).tag_all_notes([":32"])(machine="FLUTE")

def make_walk(key=None, degree=0, step_degree=2, walk_degree=1, repeats=(2,2,2,1,1,)):
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

    tongue().tag(["mp","flz."]),
    tongue(),
    tongue(end_degree=4),
    tongue(end_degree=3),
    par(
        whole_tongue(6),
        making_whole(degree=[-1,3], octave=1).tag(["p"])(machine="PIANO1"),
        making_whole(degree=4, octave=-3)(machine="PIANO2")
    )
)

# TODO: WARNING WARNIGN!!!!!

mod_and_seq(6,
    par(
        seq(
            tongue(),
            making_whole(3).tag(["pp","\<", "(normal)"])(machine="FLUTE"),
        ),
        # seq_ref("MAKINGA_SLURRED").tag(["p"])(octave=1, machine="PIANO1"),
        make_walk().change(
            octave=[1]*15+[0],
            ).tag([],[],[],[],[],[],[],[],[],[],[],[],["\<"])(pitch_spell="SHARP", machine="PIANO1"),
        seq(
            rest_all(6, "PIANO2"),
            making_whole(degree=(-3,-1,1), dur=2)
        )(octave=-1, pitch_spell="SHARP", machine="PIANO2")
    )
)

mod_and_seq(6,
    par(
        seq(
            tongue(end_degree=5).tag(["mf","flz."])(octave=1),
            tongue(end_degree=6)(octave=1),
        ),
        seq(
            OutCell("MAKING1_SLURRED").change(octave=[1,1]).tag(["mp"]), 
            OutCell("MAKING2_SLURRED").tag(["\<"])
        )(machine="PIANO1"),
        seq(
            making_cell(dur=[1]*8, degree=[0,0,1,2,3,4,5,6,7]).tag_all(["-"])
        )(octave=-1, machine="PIANO2"),
    )
)

mod_and_seq(-3,
    par(
        seq(
            making_cell(
                dur=[0.5, 2.5, 0.25, 0.75], 
                degree=[0, None, 4, 3],
                leaf_durs=[False, False, 0.25, 0.75],
                )(octave=2).tag(["(normal)","-"], [], ["("],[")"]),
            OutCell("MAKING_JIG")(octave=2).tag_all_notes(["-"]),
            # OutCell("MAKING3_SLURRED")
        )(machine="FLUTE"),
        seq(
            making_cell(dur=[1]*8, degree=[2,3,4,5]).add_chord_degree(
                None,None,7,7).tag_all(["-"]).tag([],["mf"]),
            OutCell("MAKING_TENSE")(octave=2)
        )(pitch_spell="SHARP", machine="PIANO1",),
        seq(
            rest_all(1, "PIANO2"), making_whole(degree=(-7,0), dur=3),
            OutCell("MAKING_TENSE").change(degree=[None]+[3]*7)(octave=1)
        )(octave=-1, pitch_spell="SHARP", machine="PIANO2"),
    )
)

mod_and_seq(-3,
    par(
        seq(
            rest_all(1, "FLUTE"), OutCell("MAKING_DOWN")(octave=2),
            rest_all(6, "FLUTE"),
            whole_tongue(3)(octave=2).tag(["flz.", "\<"]),
            making_cell(degree=[1, 6], dur=[1.5,0.5])(octave=2).tag(["(normal)"], ["f", ">", "."])
        )(machine="FLUTE"),
        seq(
            making_cell(degree=[None,(0,2,4)], dur=[1,3]).tag(),
            make_walk()(octave=2),
            OutCell("MAKING_TENSE").change(
                degree=[None]+ [(-2,0,5)]*3 + [(-1,1,6)]*4)(octave=1).tag(*tense_dyn)
            )(octave=1, machine="PIANO1"),
        seq(
            making_cell(dur=[4], degree=[(0,7)], octave=[-1]).tag(["bass"]),
            # make_walk()(octave=0),
            making_cell(dur=[1]*8, degree=[0,0,1,1,2,2,3,4])(octave=-1).tag_all(["-"]),
            OutCell("MAKING_TENSE").change(
                degree=[None]+ [(-3,4)]*2 + [(-3,3)]*5)(octave=-1)
            )(machine="PIANO2")
    )(pitch_spell="SHARP")
)

# MAYBE use this
# ... making_cell(degree=[3,1, None], dur=[0.75, 2.25, 1])(octave=2).change(leaf_durs=[0.75]),
mod_and_seq(6,
    par(
        seq(
            rest_all(1, "FLUTE"), OutCell("MAKING_DOWN")(octave=2),
            rest_all(4, "FLUTE"),
            # OutCell("MAKING2").alter_leaves(
            #     # dur=making_rhythm_yo, 
            #     # leaf_durs=making_rhythm_yo_durs
            #     ).change(degree=[None, None])(octave=2).tag_all("-"),
            OutCell("MAKING3").alter_leaves(
                dur=making_rhythm_yo, leaf_durs=making_rhythm_yo_durs
                )(octave=1).tag_all("-"),
        )(machine="FLUTE"),
        seq(
            making_cell(degree=[None,(0,2,4)], dur=[1,3])(octave=1),
            rest_all(1, "PIANO1"), make_walk(repeats=[1]*7)(octave=1),
            )(machine="PIANO1"),
        seq(
            rest_all(1, "PIANO2") + OutCell("MAKING_DOWN").add_chord_degree(-7,-7,-7),
            rest_all(1, "PIANO2"), make_walk(repeats=[1]*7)(octave=-1),
        )(machine="PIANO2"),
    )(pitch_spell="FLAT"),

    par(
        # TODO: FLUTE REALLY shouldn't be resting here?
        seq(
            # rest_all(8, "FLUTE"),
            OutCell("MAKING_TENSE").change(degree=[False, False, False, False, 3,3,6,6])(octave=2).tag(*tense_dyn)
            )(machine="FLUTE"),
        seq(
            # rest_all(1, "PIANO1"), make_walk(degree=4, repeats=[1]*7),
            OutCell("MAKING_TENSE").change(
                degree=[None]+ [(-2,0,5)]*3 + [(-1,1,6)]*4)(octave=1).tag(*tense_dyn),
            rest_all(4, "PIANO1"),
            making_cell(degree=[0,2,4]*5+[0], 
                octave=[-1,-1,-1,0,0,0,1,1,1,2,2,2,3,3,3,4], 
                dur=[0.5]*15+[4.5]
                ).tag(["tempo_text:ritard. to end", "bass", "(","\>"],[],[],[],["treble"],[],[],[],[],[],[],[],["8va"],
                    [],[],["8va!", "p", ")", ([],"|.")],),
            )(machine="PIANO1"),
        seq(
            # rest_all(1, "PIANO2"), make_walk(degree=4, repeats=[1]*7)(octave=-2),
            OutCell("MAKING_TENSE").change(
                degree=[None]+ [(-3,4)]*2 + [(-3,3)]*5)(octave=-1),
            rest_all(3, "PIANO2"),
            making_whole(dur=13)(octave=-3).add_chord_degree(7).tag([">"])
            )(machine="PIANO2"),
    )
)


MAKING = MAKING.tag(["tempo:96:1:4:Simmering"])

if __name__ == "__main__":
    score = score_with_meter(
        # piano2_clef="treble"
        )
    score.reset()
    pr = rain.PatternReader(MAKING, score.get_palette())
    pr.read()
    score.render("MAKING",
    stylesheets=["./rain-language/rain/score/stylesheets/stylesheet_title_making.ily"])