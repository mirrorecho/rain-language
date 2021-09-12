from itertools import cycle, repeat

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, add_modulate)
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

def flute_figure(ref_key, octave=2):
    ref_cell = OutCell(ref_key).read()
    ref_degrees = ref_cell.degree
    return freaking_cell(
        degree = (None, ref_degrees[1], ref_degrees[2], ref_degrees[2]+1, ref_degrees[2]+2),
        dur = [0.5, 0.5, 0.25, 0.25, 0.5],
        octave=cycle([octave]),
        tags = ([],["."],["."],["."],[".",">"],),
        machine=cycle(["FLUTE"]),
    )

def flute_freak(ref_key, octave=2, dur=(1,1), instructions=""):
    ref_cell = OutCell(ref_key).read()
    ref_degrees = ref_cell.degree
    freak_tags = ["note_head:0:cross", ">","*"]
    if instructions:
        freak_tags.append(instructions)
    return freaking_cell(
        degree=[None,ref_degrees[0]],
        dur = dur,
        octave = cycle([octave]),
        tags = ([], freak_tags),
        machine=cycle(["FLUTE"]),
    )

double_freak = OutCell("FREAKING1")*2

def arm_lh(dur=1, pitches=[(-17,-15,-13,-12,-10,-8,-7,-5,-3)], instructions="_*"):
    tags=(["note_head:" + str(i) + ":diamond" for i in range(len(pitches[0]))] + [".", ">", instructions],)
    # print(tags)
    return OutCell.create(pitch=pitches, dur=[dur], tags=tags)(machine="PIANO2") 

def arm_rh(dur=1,pitches=[(2,4,5,7,9,11,12,14,16,17)], instructions="*"):
    return arm_lh(dur=dur, pitches=pitches, instructions=instructions)(machine="PIANO1") 

# ======================================================================
# ======================================================================

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
    par(
        seq(
            flute_figure("FREAKING3").tag([],["mf"]),
            flute_freak("FREAKING2", instructions="markup_column:* make a scary/scared|vocal sound into flute,|roughly on this pitch|(in any register)"),
            flute_figure("FREAKING3"),
            flute_freak("FREAKING3", instructions="(vary the sound each time)"),
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
        # TODO: paramatarize these off beats - DRY
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


    # TODO: (MAYBE more) mask some of this to add interest
    par(
        # TODO... this is repeated... paramatize and DRY
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

# MEASURE 16 ===========================================================
mod_and_seq(
    # TODO (MAYBE more) DITTO: mask some of this to add interest
    par(
        seq(
            flute_figure("FREAKING1", octave=1),
            flute_figure("FREAKING2", octave=1),
            freaking_cell(
                dur=(1,1,),
                degree=(-2,0,),
                tags=(["("],[")",">"])
                )(octave=1, machine="FLUTE"),
                flute_figure("FREAKING4", octave=1),
                )(machine="FLUTE"),
        par_ref("FREAKING_PAR_PIANO").meddle(
            M("FREAKING_SEQ").tag_all(["."]), 
            ), 
        )(pitch_spell="FLAT")
    )

#TODO: funk this up a bit
# right forarm on keys somewhere in here + RH tremolo
mod_and_seq(
    par(
        seq(
            flute_freak("FREAKING2", octave=1),
            flute_freak("FREAKING4", octave=1),
            )(pitch_spell="FLAT"),
        freaking_cell( 
            degree=([-4,0],), dur=[4], tags=(["p", "\<", ":32"],),
            )(pitch_spell="FLAT", octave=1, machine="PIANO1"),
        rain.Sequence("FREAKING_BASS_SEQ").tag_all(["."])(dur=0.5, pitch_spell="FLAT", machine="PIANO2")
        )
    )
mod_and_seq(
    par(
        seq(
            flute_freak("FREAKING1", octave=1),
            flute_freak("FREAKING2", dur=(0.5,0.5), octave=1),
            flute_freak("FREAKING3", dur=(0.5,0.5), octave=1),
        )(pitch_spell="FLAT"),
        seq(
            freaking_cell( 
                degree=([-4,-1,0], None), dur=[1,1], tags=(["f",">","."],[]),
                )(octave=1, machine="PIANO1"),
                flute_figure("FREAKING1", octave=1)(machine="PIANO1"),
            )(pitch_spell="SHARP"),
        rain.Sequence("FREAKING_BASS_SEQ").tag_all(["."])(pitch_spell="SHARP", dur=0.5, machine="PIANO2")
    )
)
# MEASURE 20 ===========================================================
mod_and_seq(
    par(
        flute_figure("FREAKING1", octave=1) + flute_figure("FREAKING2", octave=1),
        seq(OutCell("FREAKING1"), OutCell("FREAKING2"),).change(
            degree=[None],
        ).tag_all(["."])(octave=1, machine="PIANO1"),
        OutCell("FREAKING_BASS1")(machine="PIANO2").change(
            degree=([-7,0],None),
            octave=[-2, False, -1, -1],
        ).tag([">","."],[],["("],[")"]),
    )(pitch_spell="SHARP"),
    par(
        rest_all(1, "FLUTE") + flute_freak("FREAKING3").change(
            dur=[3,1],
            octave=[1, 1],
            degree=[0],
            ).tag(["p", "\<"],["f"]),
        seq(
            par(
                freaking_cell( 
                degree=([-4,-1,0],), dur=[4], tags=(["p", "\<", ":32"],),
                )(octave=1, machine="PIANO1"),
                freaking_cell( 
                degree=([-1,0,3],), dur=[4], tags=(["p", "\<", ":32"],),
                )(octave=-2, machine="PIANO2"),
                )(pitch_spell="SHARP"),
            par(
                seq(OutCell("FREAKING2"), OutCell("FREAKING3"),).tag_all(["."]
                    ).change(degree=[None]).tag([],["f"])(octave=1, machine="PIANO1"),
                # TODO PARAMATIZE THIS
                freaking_cell(
                    degree=(None, [0,7])*2,
                    dur=(1,)*4,
                    tags=([],[">","."])*2
                )(octave=-3, machine="PIANO2")
                # OutCell("FREAKING_BASS2")(machine="PIANO2"),
            )(pitch_spell="SHARP"),
        ),
    )
    # # after the tremolo, start moving towards parallel
    ) 
# MEASURE 20 ===========================================================
mod_and_seq( # #emphasize electo sounds from the beginning! (full circle)
    # parallel motion ... also TODO speed up the harmonic progress
    par(
        # seq_ref("FREAKING_SEQ").tag_all(["."])(octave=2, machine="PIANO1"), 
        # seq_ref("FREAKING_SEQ").tag_all(["."])(octave=-2, machine="PIANO2"), 
        seq(rest_all(4, "FLUTE"), flute_freak("FREAKING3")),
        seq_ref("FREAKING_SEQ").tag_all(["."])(octave=2, machine="PIANO1"), 
        seq(
            seq(seq(OutCell("FREAKING1"), OutCell("FREAKING2"),)).tag_all(["."])(octave=-2, machine="PIANO2"), 
                # TODO PARAMATIZE THIS
                freaking_cell(
                    degree=(None, [0,7]),
                    dur=(1,)*2,
                    tags=([],[">","."])
                )(octave=-3, machine="PIANO2"),
            OutCell("FREAKING4").tag_all(["."])(octave=-2, machine="PIANO2"),             
            )
    )(pitch_spell="SHARP")
    )

mod_and_seq( # #emphasize electo sounds from the beginning! (full circle)
    # DITTO parallel motion ... also TODO speed up the harmonic progress
    par(
        seq(rest_all(2, "FLUTE"), flute_freak("FREAKING1"), flute_freak("FREAKING2"), flute_freak("FREAKING3"), ),
        seq_ref("FREAKING_SEQ").tag_all(["."])(octave=2, machine="PIANO1"), 
        seq(
            OutCell("FREAKING1").tag_all(["."])(octave=-2, machine="PIANO2"), 
                # TODO PARAMATIZE THIS
                freaking_cell(
                    degree=(None, [0,7])*3,
                    dur=(1,)*6,
                    tags=([],[">","."])*3
                )(octave=-3, machine="PIANO2"),
            # OutCell("FREAKING4").tag_all(["."])(octave=-2, machine="PIANO2"),             
            )
    )(pitch_spell="FLAT")
    )
    # #abrupt big chord end
mod_and_seq(
    rest_all(1),
    #TODO: arm move placement up/down
    par(arm_rh().tag(["markup_column:try to capture only|the tail of the sound|with the pedal"]), arm_lh().tag(["pedal"]),), # very low / high temolo, ending with both arms on keys
    rest_all(2),
    par(
        freaking_cell( 
            degree=[1], dur=[4], tags=(["fermata", "f", "note_head:0:diamond",
            "markup_column:hyperventilate into flute!|(air tones only)", "|."],),
            )(machine="FLUTE"),        
        freaking_cell( 
            degree=([-4, 0],), dur=[4], tags=(["fermata", "ppp", ":32", "|."],),
            )(octave=1, machine="PIANO1"),
        rest_all(4, "PIANO2")
        # TODO maybe: these low notes instead of rest
        # freaking_cell(degree=([0,3],), octave=[-3], dur=[4], tags=([],))(machine="PIANO2")
    )
    # HYPERVENTILATE INTO FLUTE (air tones only) ... dog whining
)

FREAKING = FREAKING.tag(["tempo:160:1:4:Agitated"])

if __name__ == "__main__":
    score = score_with_meter()
    score.reset()
    pr = rain.PatternReader(FREAKING, score.get_palette())
    pr.read()
    score.render("FREAKING")