from itertools import cycle, repeat
from rain.patterns.machine import Machine

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, add_modulate)
from rain.out.score_machine import score_with_meter, rest_all
from rain import ref, par, seq, par_ref, seq_ref
from rain.score import meters

M = rain.MeddleHelper

# TODO: may want to change start global tonic
passing_cell = OutCellFactory(mode=2, global_tonic=GlobalTonic(3))
passing_tonic = GlobalTonic(3)

PASSING = rain.Sequence.create("PASSING")

# TODO: these are repeated in every movement... DRY
def mod_and_seq_return(*patterns):
    passing_tonic.modulate(-3)
    return seq(*patterns).alter(add_modulate(passing_tonic))

def mod_and_seq(*patterns):
    PASSING.append(mod_and_seq_return(*patterns))

passing1_degree=(6, 3, 2, 1, 0, 3)

seq("PASSING_SEQA",
    passing_cell("PASSING1", degree=passing1_degree, dur=(0.5, 0.5, 0.5, 0.5, 0.5, 0.5,) ),
    passing_cell("PASSING2", degree=(2, 1, 0, 2, 1, 0,), dur=(0.5, 0.5, 0.5, 0.5, 0.5, 0.5,) ),
    passing_cell("PASSING3", degree=(1, 0, -3, (-1, -2)), dur=(0.5, 0.5, 1, 4,) ),
)

seq_ref("PASSING_SEQA").meddle("PASSING_SEQB",
    M("PASSING1").change(key="PASSING1B", degree=[4]),
    M("PASSING2").alter_leaves(key="PASSING2B", degree=(2, 1, 0)),
    M("PASSING3").alter_leaves(key="PASSING3B",dur=(0.5, 1,), leaf_durs=(False,1)),
)

seq("PASSING_CHORDS",
    passing_cell("PASSING_CHORD1", degree=[(-3,0,2)], dur=[3]),
    passing_cell("PASSING_CHORD2", degree=[(-3,0,1)], dur=[2]),
    passing_cell("PASSING_CHORD3", degree=[(-3,-1,0,3)], dur=[1], leaf_durs=[1]),
)

PASSING.extend(
    # rest_all(3),
    par(
        seq(
            passing_cell(degree=[passing1_degree[0]], dur=[3], octave=[1], tags=(["~", "p", "\<", "("],))(pitch_spell="SHARP", machine="FLUTE"),
            seq_ref("PASSING1")(octave=1, pitch_spell="SHARP", machine="FLUTE").change(
                machine=[False]*5+["SKIP"],
                dur=[False]*4+[1,False], 
                leaf_durs=[False]*4+[1,False],
                ).tag([],[],[],[],["mp",")"]),
            rest_all(4.5, "FLUTE"),
            passing_cell(degree=[4], dur=[1.5], octave=[1], tags=(["~", "p", "\<", "("],))(pitch_spell="SHARP", machine="FLUTE"),
            seq_ref("PASSING1B").tag(
                ["mp"],[],[],[],[")"],["("]
                )(octave=1, pitch_spell="SHARP",  machine="FLUTE"),
            seq_ref("PASSING2B").tag(
                [],[],[")"]
                )(octave=1, pitch_spell="SHARP", machine="FLUTE"),
            seq_ref("PASSING3B").tag(
                ["("],[")"],
                )(octave=1, pitch_spell="SHARP", machine="FLUTE"),
            rest_all(3, "FLUTE"),
            #TODO: double first 1-2 notes in piano here?
            seq_ref("PASSING1").tag(
                ["(","\>"],[],[],[],[")"],["("]
                )(tonic_mod=-3, octave=1, pitch_spell="FLAT", machine="FLUTE"),
        ),
        seq(
            rest_all(5.5,"PIANO1"),
            passing_cell(degree=[passing1_degree[-1]], dur=[0.5], tags=(["p", "\<", "("],))(pitch_spell="SHARP", machine="PIANO1"),
            seq_ref("PASSING2")(octave=1,pitch_spell="SHARP", machine="PIANO1").change(
                ).tag([],[],[],[],[],["mp",")"]),
            seq_ref("PASSING3")(octave=1,machine="PIANO1").change(
                pitch_spell=["SHARP"]*3 + ["FLAT"],
                leaf_durs=[False]*3+[(1,3)],
                ).tag(["("],[],[")"],[],[]),
            OutCell("PASSING_CHORD1")(pitch_spell="FLAT", machine="PIANO1").change(
                dur=[2.5],
                leaf_durs=[(1.5,1)],
                ).tag(["pp"]),
            passing_cell(dur=[0.5], degree=[-2], octave=[1], tags=(["(","mp"],))(pitch_spell="FLAT", machine="PIANO1"),
            seq_ref("PASSING3")(octave=1, pitch_spell="FLAT", machine="PIANO1").change(
                leaf_durs=[False]*3+[(1,3)],
                degree=[-1],
                ).tag([],[],[")"],[],[]),
            ),
        seq(
            rest_all(6,"PIANO2"),
            seq_ref("PASSING_CHORDS").tag(["treble"]).change(
                pitch_spell=["SHARP", "SHARP", "FLAT"],
            )(machine="PIANO2"),
            passing_cell(degree=[0], dur=[6], octave=[-3], machine=["PIANO2"]).tag(["bass","pp"]),
            OutCell("PASSING_CHORD2").change(
                degree=[(-3,-1,0)],
                ).tag(["treble"])(pitch_spell="FLAT", machine="PIANO2"),
            OutCell("PASSING_CHORD3")(pitch_spell="FLAT", machine="PIANO2"),
            passing_cell(degree=[0], dur=[3], octave=[-3], machine=["PIANO2"]).tag(["bass"]),
            )
        )
    )

mod_and_seq(
    par(
        seq(
            seq_ref("PASSING2").tag(
                [],[],[")"],["("],[],[")","p"]
                )(octave=1, pitch_spell="FLAT", machine="FLUTE"),
            rest_all(2.5, "FLUTE"),
            passing_cell(degree=[0], octave=[1], dur=[0.5], tags=(["\<", "("],))(machine="FLUTE"),
            seq_ref("PASSING3").change(
                octave=[1,1,2,2],
                leaf_durs=[False]*3+[(1,3)],
                degree=[False]*3 + [-2]
                ).tag(
                    [],[],[")"],["mp", ([],"fermata")],
                )(pitch_spell="FLAT", machine="FLUTE"),
            ),
        seq(
            OutCell("PASSING_CHORD1")(pitch_spell="FLAT", machine="PIANO1").change(
                dur=[2.5],
                leaf_durs=[(1.5,1)],
                ),
            passing_cell(degree=[0,1,2,6,(7,8)], dur=(0.5,0.5,0.5,1,1), leaf_durs=[False]*4+[1]).tag(
                ["("],[],[], [")"],
                )(pitch_spell="FLAT", machine="PIANO1"),
            OutCell("PASSING_CHORD2")(octave=1, pitch_spell="FLAT", machine="PIANO1"),
            OutCell("PASSING_CHORD3")(octave=1, pitch_spell="FLAT", machine="PIANO1"),
            passing_cell(degree=[(5,6)], octave=[1], dur=[3], tags=[["fermata"]], machine=["PIANO1"])
        ),
        seq(
            passing_cell(degree=[0,(0,4),(0,5),0], dur=[6,2,1,3], octave=[-2,-1,-1,-2], 
                leaf_durs=[False, (1.5, 0.5), 1, False],
                ).tag([],[],[],["fermata", "~"])(machine="PIANO2"),
        ),
    )
)

mod_and_seq(
    par(
        seq(
            rest_all(1, "FLUTE").tag(["tempo:54:3:8:Freely, Slowing Down"]).change(
                leaf_durs=[1]),
            OutCell("PASSING1").change(
                degree=[False,False,False,False,None],
                dur=[False,False,False,1,False,1],
                leaf_durs=[False,False,False,False,False,1],
                )(octave=1).tag(["(","\>"],[],[],[")"],[],["fermata","("]),
            OutCell("PASSING2").change(
                dur=[False,False,1,1,1,3],
                leaf_durs=[False,False,1,1,1,],
                degree=[False,False,False,None],
                )(octave=1).tag(
                    [],[],[")", "fermata"], [],["("],[")", "fermata", "pp", "|."])
        )(machine="FLUTE"),
        seq(
            OutCell("PASSING_CHORD1").change(dur=[3],
                )(octave=1).tag(["pp", "~"]), # TODO: why won't tagging fermata on second leaf work here?
            OutCell("PASSING_CHORD1").change(dur=[1.5],
                )(octave=1).tag(["fermata"]),
            
            OutCell("PASSING_CHORD3").change(dur=[1.5], leaf_durs=[1.5],
                )(octave=1).tag(["~"]),
            OutCell("PASSING_CHORD3").change(dur=[1.5], leaf_durs=[1.5],
                )(octave=1).tag(["fermata"]),
            
            OutCell("PASSING_CHORD2").change(dur=[1.5],
                ).tag(["~", "bass"]),
            OutCell("PASSING_CHORD2").change(dur=[3],
                ).tag(["fermata"]),

        )(machine="PIANO1"),
        passing_cell(
            dur=[1.5,1.5,4,2,1,2], 
            leaf_durs=[1.5,1.5,(3,1),2,1,2],
            degree=[2,0,0,1,None,0], octave=[-2,-1,-1,-1,0,-3],
            ).tag(
            [],["~"],["fermata"],["fermata"],["fermata"],["^fff", "fermata","8vb","|."])(machine="PIANO2")
    )
    # seq_ref("PASSING_SEQA")(machine="PIANO1"),
    # seq_ref("PASSING_SEQB")(machine="PIANO1"),
    # rest_all(3), # this is downward motion "LH" figure only
    )

# mod_and_seq(
#     seq_ref("PASSING_SEQB")(machine="PIANO2"),
#     )

PASSING = PASSING.tag(["tempo:92:3:8:Dreamy"])

if __name__ == "__main__":
    score = score_with_meter(meters.METER_6_8)
    score.reset()
    pr = rain.PatternReader(PASSING, score.get_palette())
    pr.read()
    score.render()