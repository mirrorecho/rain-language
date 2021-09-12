from itertools import cycle, repeat
# from rain.out.movements.freaking import FREAKING

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, add_modulate)
from rain.out.score_machine import score_with_meter, rest_all
from rain import ref, par, seq, par_ref, seq_ref

M = rain.MeddleHelper

# TODO: MAYBE change start global tonic?
coming_cell = OutCellFactory(mode=4, global_tonic=GlobalTonic(-5))
coming_tonic = GlobalTonic(-5)

COMING = rain.Sequence.create("COMING")

# TODO: these are repeated in every movement... DRY
def mod_and_seq_return(pitches=5, *patterns):
    coming_tonic.modulate(pitches)
    return seq(*patterns).alter(add_modulate(coming_tonic))

def mod_and_seq(pitches=5, *patterns):
    COMING.append(mod_and_seq_return(pitches, *patterns))

#TODO: what was this for???? 
# IMPORTANT_RHYTHM = (1, 1, 0.25, 0.25, 0.5, 1.5, 0.75, 0.25, 0.25, 0.5, 0.5,)

seq("COMING_1",
    coming_cell("COMING_A", degree=(None, 2, 3, 4), dur=(0.5, 0.5, 0.5, 2.5) ),
    coming_cell("COMING_B", degree=(None, 2, 3, 4, 5), dur=(0.5, 0.5, 0.5, 1.5, 3) ),
    coming_cell("COMING_C", degree=(None, 5, 7, 6, 5), dur=(1, 1, 1.5, 1.5, 1.5) ),
    coming_cell("COMING_D", degree=(None, 7, 6, 4, None), dur=(0.5, 1, 1, 5) ),
)
swap_degrees_ab = [False, False, 4, 3]

OutCell("COMING_A").change(key="COMING_A_SWAP", degree=swap_degrees_ab)
OutCell("COMING_B").change(key="COMING_B_SWAP", degree=swap_degrees_ab)

# TODO: MAYBE make these 3 note chords
chord_seqa = [(1,4), (2,4), (3,4), (4,5)]
chord_seqb = [(4,7), (0,6), (4,5), (1,4)]
chord_seq = chord_seqa + chord_seqb

def chord_i(*indices, chord_seq=chord_seq):
    return [c[i] for c,i in zip(chord_seq, indices)]

seq("OSTI_CHORDS", 
    coming_cell("CHORD1", degree=chord_seqa+chord_seqb, dur=[2]*7+[1])
)

coming_cell("RISE", degree=(-2,0), dur=(1,4))

COMING.extend(
    par(
        # seq_ref("COMING_1")(machine="FLUTE"),
        # TODO: start with single notes, then two-note chords
        rest_all(1, "PIANO1") + seq_ref("OSTI_CHORDS").tag(["p"])(machine="PIANO1"),
        coming_cell(dur=[4,4,4,2,2,], degree=[0]*8)(octave=-1, machine="PIANO2")
    ),
    par(
        # TODO: ideally this is only the first two notes
        rest_all(4, "FLUTE") + OutCell("COMING_A").tag(
            [],["(", "p"],[],[")"]
            )(octave=1, machine="FLUTE"),
        # TODO: consider fancifying this piano part
        coming_cell(degree=[None]+chord_seqa[:3], dur=[1,2,2,3])(machine="PIANO1"),
        coming_cell(dur=[4,4], degree=[0]*4)(octave=-1, machine="PIANO2")
    ),
    # TODO: ADD TALKING?????
    # TODO: this doesn't work... 
    rest_all(4).tag_all(["fermata"]),
    par(
        seq(rest_all(4, "FLUTE"),
            OutCell("COMING_A").tag(
            [],["("],[],[")"]
            ),
            OutCell("COMING_B").tag(
            [],["("],[],[],[")"]
            ),
            )(octave=1, machine="FLUTE"),
        # TODO: begin highlighting flute part in piano
        coming_cell(degree=[None]+chord_seqa + chord_seqb[:2], dur=[1,2,2,3,2,2,2,2])(machine="PIANO1"),
        coming_cell(dur=[4,2,2,2,2,2,], degree=[0]*7)(octave=-1, machine="PIANO2")
    ),
    # TODO: DITTO AS ABOVE, this fermata doesn't work...
    rest_all(2).tag_all(["fermata"]),
    #TODO: consider starting to modulate here (DOWN A FIFTH)
    par(
        seq(
            OutCell("COMING_A").tag(
            [],["("],[],[")"]
            ),
            OutCell("COMING_B").tag(
            [],["("],[],[],[")"]
            ),
            OutCell("COMING_C").tag(
            [],["("],[],[],[")"]
            ),
            )(octave=1, machine="FLUTE"),
        # TODO: begin highlighting flute part in piano
        coming_cell(degree=[None]+chord_seq[2:], dur=[1,2,2,3,2,2,5])(machine="PIANO1"),
        coming_cell(dur=[2,2,2,2,4,2,3], degree=[None]+[0]*7)(octave=-1, machine="PIANO2")
    ),
    rest_all(3),
)

# # # coming_tonic.modulate(3)
# MEASURE 17 ===================================================================
mod_and_seq(3,
    par(
        #TODO: mangle / develop the beginning of this flute part
        seq_ref("COMING_1").meddle(
                M("COMING_C").change(dur=[False]*4+[1.5,0.5]),
                M("COMING_D").change(degree=[False,False,4,7])
            ).tag(
            [],["("],[],[")"],
            [],["("],[],[],[")"],
            [],["("],[],[],[")"],
            [],["("],[],[")"],
            )(octave=1, machine="FLUTE"),
        # TODO: begin highlighting flute part in piano
        # TODO: MAYBE - something interesting in piano part at very end
        coming_cell(degree=[None]+chord_seq + [(-2, 0,1)], dur=[1,2,2,2,2,3,2,2,4,4]).change(
            tonic_mod=[False,-3] + [False]*7 + [5],
            )(octave=1,machine="PIANO1"),
        coming_cell(dur=[2]*12, 
            degree=[None,(-2,2),-2,-3,-5,(-6,-1),-7,(-7,-3),-7,(-7,-3),-7,(-7,-3)]
            ).tag(*([],)*11+(["~"],))(octave=-1, machine="PIANO2")
    ),
)

# MEASURE 23 ===================================================================
mod_and_seq(5,
    par(
        seq(
            rest_all(5,"FLUTE"),
            OutCell("RISE").change(dur=[3,4]).tag(["\<"],["mf"]),
            )(octave=2, pitch_spell="FLAT",machine="FLUTE"),
        seq(
            OutCell("COMING_B_SWAP").change(
                dur=[False,False,False,2,2.5],
                octave=[0,1,1,1,0],
                # leaf_durs=[False,False,False,(0.5,1.5)],
                ).add_chord_degree(None,None,None,7,7)(
            ).tag(
            [],["(","]"],["["],["]"],[")"]
            ),
            OutCell("COMING_C").change(
                octave=(0,0,0,1,1),
                dur=[False]*4+[1],
                ).add_chord_degree(None,7,None,None,7).tag(
                    [],["("],[],[],[")",]
                ),
            )(pitch_spell="FLAT",machine="PIANO1"),
        coming_cell(dur=[1]*4+[2,3,1,1,1], 
            degree=[4,4,4,4,0,0,7,7,7]
            ).tag(*([],)*8+(["~"],)).add_chord_degree(4,4,4,4,7,7,4,4,4)(octave=-3, machine="PIANO2"),
    ),
)

# MEASURE 26 ===================================================================
mod_and_seq(5,
    par(
        seq(
            OutCell("COMING_D").change(dur=[1]),
            ).tag([],["(","\>"],[],[")","\!"])(pitch_spell="FLAT", octave=1, machine="FLUTE"),
        seq(
            OutCell("COMING_A_SWAP").change(
                dur=[False,1,1,5.5],
                octave=(0,0,0,1),
                ).tag([],["("],[],[")"]).add_chord_degree(None,(5,7),7,7),
            )(pitch_spell="FLAT", machine="PIANO1"),
        seq(
            coming_cell(dur=[1,1,1,1,2,2], 
                degree=[-3,1,0,-1,-2,-3],
                octave=[-1,-2,-2,-2,-2,-1]
                ).tag([]).add_chord_degree(4,7,7,7,7,7),
        )(pitch_spell="FLAT", machine="PIANO2")
    )
)
# MEASURE 28 ===================================================================
mod_and_seq(3,
    par(
        seq(
            rest_all(2,"FLUTE"),
            OutCell("RISE").change(dur=[2,4]).tag(["\<"],["f"])(octave=2),
            OutCell("COMING_D").change(dur=[1,1,1,1], octave=[0,0,1,2]).tag(
                [],[],["~"]),
            )(pitch_spell="SHARP",machine="FLUTE"),
        seq(
            OutCell("COMING_B_SWAP").change(
                dur=[False]*4+[1],
                octave=(0,0,0,1,1),
                ).tag([],["("],[],[],[")"]).add_chord_degree(None,7,7,7,7)(pitch_spell="FLAT"),
            OutCell("COMING_C").change(
                dur=[False]*4+[3],
                octave=(-1,-1,-1,0,1),
                ).tag([],["("],[],[],[")"]).add_chord_degree(None,7,7,7,7)(pitch_spell="SHARP"),
            )(machine="PIANO1"),
        seq(
            coming_cell(dur=[1,1,1,2], 
                degree=[2,1,-2,-3,],
                ).tag([]).add_chord_degree(7,7,7,7)(octave=-2, pitch_spell="FLAT"),
            coming_cell(dur=[1,1,1,1,1,1,1,1], 
                degree=[4,4,1,1,0,0,0],
                ).tag([],[],[],[],[],[],["~"],).add_chord_degree(4,4,7,7,4,(4,7),(4,7))(octave=-2, pitch_spell="SHARP"),
        )(machine="PIANO2")
    )
)

# MEASURE 31 ===================================================================
mod_and_seq(3,
    par(
        seq(
            # OutCell("RISE").change(dur=[2,4]).tag([],[])(octave=2),
            OutCell("COMING_C").change(
                dur=[3,1,1,1,2], 
                # octave=[1,1,1,1]
                ).tag([],["("],[],[],[")"]),
            )(octave=1, pitch_spell="SHARP", machine="FLUTE"),
        seq(
            coming_cell(degree=[None]+chord_seq, dur=[0.5]+[1]*7+[0.5],
                leaf_durs=[False,1,False,1,False,1]*4,
                octave=(0,0,0,1,1,1,1,2,2)
                ).tag([],["("],[],[],[],[],[],[],[")"],).add_degree(None, -3,7,-3,-2,0,None,-2),
            )(pitch_spell="SHARP", machine="PIANO1"),
        seq(
            coming_cell(dur=[1,1,1,2,1,2], 
                degree=[-2,1,-2,-3,-1,-2],
                ).tag([]).add_chord_degree((4,7),7,7,7,7,(4,7))(octave=-2),
            # coming_cell(dur=[1,1,1,1,1,1,1,1], 
            #     degree=[4,4,1,1,0,0,0],
            #     ).tag([]).add_chord_degree(4,4,7,7,4,(4,7),(4,7))(octave=-2, pitch_spell="SHARP"),
        )(pitch_spell="SHARP", machine="PIANO2")
    )
)
# MEASURE 33 ===================================================================
mod_and_seq(-7,
    par(
        seq(
            # OutCell("RISE").change(dur=[2,4]).tag([],[])(octave=2),
            OutCell("COMING_A_SWAP").change(
                dur=[1.5,0.5,0.5,1.5], 
                octave=[1,1,1,2]
                ).tag([],["("],[],[")"]),
            OutCell("COMING_B").tag([],["("],[],[")"])(octave=2),
            rest_all(1, "FLUTE") + OutCell("RISE")(octave=3),
            rest_all(1, "FLUTE") + OutCell("RISE").tag(["\>"],)(octave=2),
            rest_all(1, "FLUTE") + OutCell("RISE").tag([],["p","fermata", "|."])(octave=1),
            )(pitch_spell="SHARP", machine="FLUTE"),
        seq(
            coming_cell(degree=[None]+chord_seq, dur=[0.5]+[1]*6+[1.5],
                leaf_durs=[False,1,False,1,False,1,False, (0.5,1)],
                octave=(0,0,0,1,1,1,1,1,1)
                ).tag([],["("],[],[],[],[],[],[")"],
                ).add_degree(None, 5,7,0,0,0,None,0),
            rest_all(1, "PIANO1") + seq_ref("OSTI_CHORDS"
                ).change(octave=[0]*5+[1,1,1]).add_degree(7,7,7,7,11,None,None,5).tag(
                [],["\>"]),
            coming_cell(degree=[(0,7)], dur=[4]).tag(["fermata", "pp", "|."])(octave=1)
            )(pitch_spell="SHARP", machine="PIANO1"),
        seq(
            coming_cell(dur=[1,1,1,1,1,2,1], 
                degree=[-5,-6,-3,-2,0,0,5],
                ).tag([]).add_chord_degree(7,(4,7),7,7,7,(4,7))(octave=-1),
            coming_cell(dur=[2,1,1,2,1,1,2,2,2,2,4], 
                degree=[(0,4,7),0,5,(0,4),0,5,(0,4),(0,4),(0,4),0,0],
                ).tag([],[],[],[],[],[],[],[],[],[], ["|.", "fermata"])(octave=-1),
        )(pitch_spell="SHARP", machine="PIANO2")
    )
)

COMING = COMING.tag(["tempo:112:1:4"])

if __name__ == "__main__":
    score = score_with_meter()
    score.reset()
    pr = rain.PatternReader(COMING, score.get_palette())
    pr.read()
    score.render()