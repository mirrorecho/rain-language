from itertools import cycle, repeat

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, AddDegrees, Mask,
    add_modulate)
from rain.out.score_machine import score_with_meter, rest_all
from rain import ref, par, seq, par_ref, seq_ref

M = rain.MeddleHelper

# TODO: likely change start global tonic
freaking_cell = OutCellFactory(mode=3, global_tonic=GlobalTonic(4))
freaking_tonic = GlobalTonic(4)

FREAKING = rain.Sequence.create("FREAKING")

# TODO: this is copied into every movement... DRY
def mod_and_seq(*patterns):
    freaking_tonic.modulate(2)
    FREAKING.append(
        rain.Sequence.create().extend(*patterns).alter(add_modulate(freaking_tonic))
    )

par("FREAKING_PAR",
    seq("FREAKING_SEQ",
        freaking_cell("FREAKING1", degree=(-4,-1,0,-1), dur=cycle((0.5,)) ),
        freaking_cell("FREAKING2", degree=(-3,-1,0,-1), dur=cycle((0.5,)) ),
        freaking_cell("FREAKING3", degree=(-3,-2,0,-2), dur=cycle((0.5,)) ),
        freaking_cell("FREAKING4", degree=(-3,-2,1,-2), dur=cycle((0.5,)) ),
    ),
    seq("FREAKING_BASS_SEQ",
        freaking_cell("FREAKING_BASS1", 
            degree=(-14, (-12, -7), -14, (-10, -7),),
            dur=cycle((1,)),
            ),
        freaking_cell("FREAKING_BASS2", 
            degree=(-16, (-14, -9), -16, (-11, -9),),
            dur=cycle((1,)),
            )
    ).tag_all(["("],[")"], key="FREAKING_BASS_SEQ_SLURRED")
)

par_ref("FREAKING_PAR").meddle("FREAKING_PAR_PIANO",
    M("FREAKING_SEQ")(machine="PIANO1"),
    M("FREAKING_BASS_SEQ")(machine="PIANO2"), 
    ) 

def flute_figure(ref_key):
    ref_cell = OutCell(ref_key).read()
    ref_degrees = ref_cell.degree
    return freaking_cell(
        degree = (None, ref_degrees[1], ref_degrees[2], ref_degrees[2]+1, ref_degrees[2]+2),
        dur = [0.5, 0.5, 0.25, 0.25, 0.5],
        octave=cycle([2]),
        tags = ([],["."],["."],["."],[".",">"],),
        machine=cycle(["FLUTE"]),
    )

def flute_freak(ref_key, instructions=""):
    ref_cell = OutCell(ref_key).read()
    ref_degrees = ref_cell.degree
    freak_tags = ["note_head:0:cross", ">","*"]
    if instructions:
        freak_tags.append(instructions)
    return freaking_cell(
        degree=[None,ref_degrees[0]],
        dur = (1,1),
        octave = cycle([2]),
        tags = ([], freak_tags),
        machine=cycle(["FLUTE"]),
    )

double_freak = OutCell("FREAKING1")*2

def arm_lh(dur=1, pitches=[(-17,-15,-13,-12,-10,-8,-7,-5,-3)], instructions="_*"):
    tags=(["note_head:" + str(i) + ":diamond" for i in range(len(pitches[0]))] + [".", ">", instructions],)
    # print(tags)
    return OutCell.create(pitch=pitches, dur=[dur], tags=tags)(machine="PIANO2") 

FREAKING.extend(

    # TODO: tremolo notation is odd / not specific
    # also TODO: paramatize this
    # also TODO MAYBE: tie tremolo pitches to the FREAKING1-4 cell pitches?
    freaking_cell( degree=([-4,0],), dur=[4], tags=(["p", "\<", ":32"],), machine=["PIANO1"])(pitch_spell="SHARP"),

    # TODO: spell with sharps?
    ((double_freak + OutCell("FREAKING2"))*2).tag(["mf"]).tag_all(["."])(pitch_spell="SHARP")(machine="PIANO1"), # lower forarm on keys on first and final 8ths

    freaking_cell( degree=([-3,-1,0],), dur=[4], tags=([":32"],), machine=["PIANO1"])(pitch_spell="SHARP"),

    # flute enters, highlighting the lines in an angular way
    # lower forarm on keys on first (and maybe final 8ths??)
    # (OutCell("FREAKING3") + OutCell("FREAKING2") + OutCell("FREAKING3")*2 )(machine="PIANO1"),
    rain.Parallel.create().extend(
        seq(
            flute_figure("FREAKING3").tag([],["mf"]),
            flute_freak("FREAKING2", instructions="markup_column:* make a scary/scared|vocal sound into flute,|roughly on this pitch|(in any register)"),
            flute_figure("FREAKING3"),
            flute_freak("FREAKING3"),
            # TODO.. encapsulate this....
            freaking_cell(
                degree=(None, 1,5),
                dur = (2,5.5,0.5),
                tags = ([],["mp","\<"], ["f",">","."]),
                )(octave=2, machine="FLUTE"),
            )(pitch_spell="SHARP"),
        (rain.Sequence.create().extend_by_key("FREAKING3", "FREAKING2", "FREAKING3")*2 +
            rain.Sequence.create().extend_by_key("FREAKING4", "FREAKING3")
            ).tag_all(["."])(pitch_spell="SHARP")(machine="PIANO1"),
        arm_lh(instructions="_* forearm on keys") + rest_all(14.5, "PIANO2") + arm_lh(0.5)
    ),

    par(
        # TREMOLO, (maybe with arms on lower keys at start?)
        freaking_cell( degree=([-3,-2,1],), dur=[4], tags=(["mp", "\<", ":32"],), 
            machine=["PIANO1"])(pitch_spell="FLAT"),
        # rest_all(4), 
        ),

    par(
        flute_figure("FREAKING4") + flute_freak("FREAKING4"),
        (OutCell("FREAKING4")*2).tag(["f"]).tag_all(["."])(machine="PIANO1"),
        freaking_cell(
            degree=(None, [0,7]),
            dur=(3,1,),
            tags=([],[">","."])
        )(octave=-3, machine="PIANO2")
        )(pitch_spell="FLAT")
)

# MEASURE 12 ============================
mod_and_seq(
    par(
        seq(
            flute_freak("FREAKING1"),
            freaking_cell(
                degree=(1,5,None),
                dur = (2,1,3),
                tags = (["mf","\<"], ["f",">","."]),
                )(octave=1, machine="FLUTE"),
            )(pitch_spell="FLAT"),


        (OutCell("FREAKING1")*2).tag_all(["."])(pitch_spell="FLAT")(machine="PIANO1") +
        # TREMOLO, with arms on lower keys at start
            freaking_cell( degree=([-4,0],), dur=[4], tags=([":32"],), 
                machine=["PIANO1"])(pitch_spell="FLAT"),
        

        freaking_cell(
            degree=(None, [0,7],None),
            dur=(1,1,2),
            tags=([],[">","."],[])
        )(octave=-3, machine="PIANO2", pitch_spell="FLAT") + arm_lh(),
    ),


    # TODO: mask some of this to add interest
    par(
        freaking_cell(
            dur=(1,1,2,1,1,2),
            degree=(0,2,None,-2,0,None),
            tags=(["("],[")",">"],[])*2,
            )(octave=2, machine="FLUTE"),
        seq_ref("FREAKING_SEQ").tag_all(["."])(machine="PIANO1"), 
        seq_ref("FREAKING_BASS_SEQ").change(
            degree=[None]+[False]*4+[None], 
            octave=[False]*4+[1]
            ).tag([], ["-",">"], ["("],[")"], ["-",">"], [], ["("], [")"])(machine="PIANO2")
        )(pitch_spell="FLAT"), 
    )

mod_and_seq(
    # TODO DITTO: mask some of this to add interest
    rain.Parallel("FREAKING_PAR_PIANO").meddle(
        M("FREAKING_SEQ").tag_all(["."]), 
        )(pitch_spell="FLAT"), 
    )

#TODO: funk this up a bit
# right forarm on keys somewhere in here + RH tremolo
mod_and_seq(
    rain.Sequence("FREAKING_BASS_SEQ")(dur=0.5, pitch_spell="FLAT", machine="PIANO2")
    )
mod_and_seq(
    rain.Sequence("FREAKING_BASS_SEQ")(dur=0.5, machine="PIANO2")
    )
mod_and_seq(
    rain.Parallel("FREAKING_PAR_PIANO"),
    rest_all(4), # TREMOLO, but insert this into the middle of the above
    # # after the tremolo, start moving towards parallel
    )
mod_and_seq( # #emphasize electo sounds from the beginning! (full circle)
    rain.Sequence("FREAKING_SEQ")(machine="PIANO1"), # parallel motion ... also TODO speed up the harmonic progress
    )
mod_and_seq( # #emphasize electo sounds from the beginning! (full circle)
    rain.Sequence("FREAKING_SEQ")(machine="PIANO1"), # DITTO parallel motion ... also TODO speed up the harmonic progress
    )
    # #abrupt big chord end
mod_and_seq(
    rest_all(4), # very low / high temolo, ending with both arms on keys
)
mod_and_seq(
    rest_all(8), # HYPERVENTILATE INTO FLUTE (air tones only) ... dog whining
)

FREAKING = FREAKING.tag(["tempo:144:1:4:Agitated"])

if __name__ == "__main__":
    score = score_with_meter()
    score.reset()
    pr = rain.PatternReader(FREAKING, score.get_palette())
    pr.read()
    score.render()