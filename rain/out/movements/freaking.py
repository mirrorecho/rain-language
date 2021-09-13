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
            # degree=(-14, (-12, -7), -14, (-10, -7),),
            degree=(None, (-12, -7), -14, (-10, -7),),
            dur=cycle((1,)),
            ),
        freaking_cell("FREAKING_BASS2", 
            # degree=(-16, (-14, -9), -16, (-11, -9),),
            degree=(None, (-14, -9), -16, (-11, -9),),
            dur=cycle((1,)),
            )
    ).tag_all(["("],[")"], key="FREAKING_BASS_SEQ_SLURRED")
)

bass_tags = [], ["-",">"], ["("], [")","."]

# par_ref("FREAKING_PAR").meddle("FREAKING_PAR_PIANO",
#     M("FREAKING_SEQ")(machine="PIANO1"),
#     M("FREAKING_BASS_SEQ")(machine="PIANO2"), 
#     ) 

def flute_figure(ref_key, octave=2):
    ref_cell = OutCell(ref_key).read()
    ref_degrees = ref_cell.degree
    return freaking_cell(
        degree = (None, ref_degrees[1], ref_degrees[1], ref_degrees[1]+1, ref_degrees[2]),
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

# TODO: tremolo notation is odd / not specific
def tremble(degree=[-4,0], dur=4, octave=0, lh_octave=-1, tag_rh=[], tag_lh=[], include_lh=True):
    return par( 
        freaking_cell( 
            degree=(degree,), 
            dur=[dur], tags=(["p", "\<", ":32"]+tag_rh,) 
            )(octave=octave, machine="PIANO1"),
        freaking_cell( 
            degree=(degree[-1]+(7*lh_octave),) if include_lh else (None,), 
            dur=[dur], tags=(["pedal"]+tag_lh,) 
            )(machine="PIANO2")
        )

def arm_lh(dur=1, pitches=[(-15,-13,-12,-10,-8,-7,-5,-3)], instructions="_*"):
    tags=(["note_head:" + str(i) + ":diamond" for i in range(len(pitches[0]))] + ["sfz", ".", ">", instructions],)
    # print(tags)
    return OutCell.create(pitch=pitches, dur=[dur], tags=tags)(machine="PIANO2") 

def arm_rh(dur=1,pitches=[(2,4,5,7,9,11,12,14,16,17)], instructions="*"):
    return arm_lh(dur=dur, pitches=pitches, instructions=instructions)(machine="PIANO1") 

def bump(degree=0):
    return freaking_cell(dur=[1], degree=[(degree-7, degree-14)], tags=[[".", ">"]], machine=["PIANO2"])

def low_shake(degree1=-8, degree2=0, times=4, octave=-1):
    return freaking_cell(dur=[0.5]*times*2, degree=cycle([degree1, degree2]), 
        ).tag_all(["."])(octave=octave, machine="PIANO2")

freaking_cell("END_TREMBLE", degree=[0], dur=[0.5], tags=[[".", "pedal!"]],
        machine=["PIANO2"])

# ======================================================================
# ======================================================================

FREAKING.extend(

    par(
        freaking_cell(dur=[1,1,1,1], degree=[7,4,7,4]).tag(["(click track...)"])(machine="FLUTE"),
        freaking_cell(dur=[1,1,1,1], degree=[7,4,7,4]).tag(["(click track...)"])(machine="PIANO1"),
    ).tag_all(["note_head:0:cross"]),

    # TODO MAYBE: tie tremolo pitches to the FREAKING1-4 cell pitches?
    tremble(degree=[3,7], dur=8)(pitch_spell="SHARP"),

    # TODO: spell with sharps?
    par(
        ((double_freak + OutCell("FREAKING2"))*2).change(
            degree=[None],
            ).tag(["mf"]).tag_all_notes(["."])(
            pitch_spell="SHARP")(octave=1, machine="PIANO1"), 
        OutCell("END_TREMBLE"),
    ),
    rest_all(2),
    tremble(degree=[4,6,7], dur=6)(pitch_spell="SHARP"),

    # MEASURE 8 ==========================================================

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
        (rain.Sequence.create().extend_by_key("FREAKING3", "FREAKING3", "FREAKING2",)*2 +
            rain.Sequence.create().extend_by_key("FREAKING4", "FREAKING4")
            ).change(degree=[None]).tag([],["mf"]).tag_all_notes(["."])(pitch_spell="SHARP")(machine="PIANO1"),
        
        seq(arm_lh(instructions="_* forearm on keys").tag(["pedal!"]),
            rest_all(6, "PIANO2"), bump(),
            rest_all(7.5, "PIANO2"), arm_lh(0.5))
    ),

    par(
        seq(
            rest_all(1, "PIANO1"),
            tremble(degree=(-3,-2,1), dur=3)(pitch_spell="FLAT"),
        ),
        ),

    par(
        flute_figure("FREAKING4") + flute_freak("FREAKING4"),
        (OutCell("FREAKING4")*2).change(degree=[None]).tag(["f"]).tag_all_notes(["."])(machine="PIANO1"),
        seq(
            OutCell("END_TREMBLE").change(degree=[-6]),
            rest_all(2.5, "PIANO2"),
            bump(-7),
        )
        )(pitch_spell="FLAT")
)

# MEASURE 14 ============================
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


        seq(
            (OutCell("FREAKING1")*2).tag_all_notes(["."])(pitch_spell="FLAT", machine="PIANO1") +
            rest_all(1, "PIANO1"),
            tremble(dur=3, include_lh=False),
        )(pitch_spell="FLAT"),
        seq(
            rest_all(1, "PIANO2"),
            bump(-7),
            rest_all(2, "PIANO2"),
            arm_lh()
        )(pitch_spell="FLAT"),
    ),


    # TODO: (MAYBE more) mask some of this to add interest
    par(
        # TODO... this is repeated... paramatize and DRY
        freaking_cell(
            dur=(1,1,2,1,1,2),
            degree=(0,2,None,-2,0,None),
            tags=(["("],[")",">"],[])*2,
            )(octave=2, machine="FLUTE"),
        seq_ref("FREAKING_SEQ").change(degree=[None]).tag(["f"]
            ).tag_all_notes(["."])(machine="PIANO1"),        
        seq(
            OutCell("END_TREMBLE")(octave=-1),
            OutCell("FREAKING_BASS1").change(
                dur=[0.5],
                ).tag(*bass_tags),
            freaking_cell(degree=[(-9,-2)], dur=[4], octave=[-1])
            )(machine="PIANO2")
        )(pitch_spell="FLAT"), 
    )

# MEASURE 18 ===========================================================
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
        OutCell("FREAKING_SEQ").tag_all(["."])(machine="PIANO1"),
        seq(
            OutCell("FREAKING_BASS1").tag(*bass_tags),
            freaking_cell(degree=[(-9,-2)], dur=[4], octave=[-1])
        )(machine="PIANO2")
        )(pitch_spell="FLAT")
    )

#TODO: MAYBE funk this up a bit
# right forarm on keys somewhere in here + RH tremolo
mod_and_seq(
    par(
        seq(
            flute_freak("FREAKING2", octave=1),
            flute_freak("FREAKING4", octave=1),
            )(pitch_spell="FLAT"),
        freaking_cell( degree=([-4,3],), dur=[4],)(machine="PIANO1"),
        seq_ref("FREAKING_BASS_SEQ").tag_all(["."])(dur=0.5, pitch_spell="FLAT", machine="PIANO2")
        )
    )

# MEASURE 21 ===========================================================
mod_and_seq(
    par(
        seq(
            flute_freak("FREAKING1", octave=1),
            flute_freak("FREAKING2", dur=(0.5,0.5), octave=1),
            flute_freak("FREAKING3", dur=(0.5,0.5), octave=1),
        )(pitch_spell="FLAT"),
        seq(
            freaking_cell( 
                degree=([-4,-1,0], None), dur=[1,1], tags=(["f",">","."],[]), ),
                flute_figure("FREAKING1", octave=1),
            )(pitch_spell="SHARP", machine="PIANO1"),
        seq(
            OutCell("FREAKING_BASS1").tag_all(["."])(pitch_spell="SHARP", dur=0.5),
            freaking_cell( degree=([-8,-1],), dur=[2], octave=[-1]),
        )(machine="PIANO2")
    )
)
# MEASURE 22 ===========================================================
mod_and_seq(
    par(
        flute_figure("FREAKING1", octave=1) + flute_figure("FREAKING2", octave=1),
        seq(OutCell("FREAKING1"), OutCell("FREAKING2"),).change(
            degree=[None],
        ).tag_all(["."])(octave=1, machine="PIANO1"),
        OutCell("FREAKING_BASS1")(machine="PIANO2").change(
            degree=([-7,0],None),
            octave=[-2, False, -1, -1],
        ).tag([">","."],[],["("],[")","."]),
    )(pitch_spell="SHARP"),
    
    par(
        rest_all(5, "FLUTE") + flute_freak("FREAKING3").change(
            dur=[3,1],
            octave=[1, 1],
            degree=[0],
            ).tag(["p", "\<"],["f"]),
        seq(
            rest_all(1, "PIANO1"),
            tremble(degree=[-4,-1,0], octave=1, lh_octave=-2, dur=7)( pitch_spell="SHARP"),
            # par(
            #     freaking_cell( 
            #     degree=([-4,-1,0],), dur=[4], tags=(["p", "\<", ":32"],),
            #     )(octave=1, machine="PIANO1"),
            #     freaking_cell( 
            #     degree=([-1,0,3],), dur=[4], tags=(["p", "\<", ":32"],),
            #     )(octave=-2, machine="PIANO2"),
            #     )(pitch_spell="SHARP"),
            par(
                seq(OutCell("FREAKING2"), OutCell("FREAKING3"),).tag_all(["."]
                    ).change(degree=[None]).tag([],["f"])(octave=1, machine="PIANO1"),
                seq(
                    OutCell("END_TREMBLE").change(dur=[1]),
                    # TODO PARAMATIZE THIS
                    freaking_cell(
                        degree=([-7,0], None, [-7,0],),
                        dur=(1,)*3,
                        tags=([">","."], [], [">","."])
                        )
                )(octave=-2, machine="PIANO2")
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
            low_shake(),
            # TODO PARAMATIZE THIS
            freaking_cell(
                degree=(None, [0,7]),
                dur=(1,)*2,
                tags=([],[">","."])
            )(octave=-3, machine="PIANO2"),
            low_shake(times=2, octave=-2),             
            )
    )(pitch_spell="SHARP")
    )

mod_and_seq( # #emphasize electo sounds from the beginning! (full circle)
    # DITTO parallel motion ... also TODO speed up the harmonic progress
    par(
        seq(rest_all(2, "FLUTE"), flute_freak("FREAKING1"), flute_freak("FREAKING2"), flute_freak("FREAKING3"), ),
        seq_ref("FREAKING_SEQ").tag_all(["."])(octave=2, machine="PIANO1"), 
        seq(
            low_shake(octave=-2),
            # OutCell("FREAKING1").tag_all(["."])(octave=-2, machine="PIANO2"), 
                # TODO PARAMATIZE THIS
                freaking_cell(
                    degree=(None, [0,7])*2,
                    dur=(1,)*6,
                    tags=([],[">","."])*2
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
            degree=[2], dur=[4], tags=(["fermata", "f", "note_head:0:diamond",
            "markup_column:hyperventilate into flute|(air tones only)", "|."],),
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
    score.render("FREAKING",
    stylesheets=["./rain-language/rain/score/stylesheets/stylesheet_title_freaking.ily"])