from itertools import cycle, repeat

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, add_modulate)
from rain.out.score_machine import score_with_meter, rest_all
from rain import ref, par, seq, par_ref, seq_ref

from rain.out.movements import coming


M = rain.MeddleHelper

flipping_cell = OutCellFactory(mode=6, global_tonic=GlobalTonic(-1))
flipping_tonic = GlobalTonic(-1)

FLIPPING = rain.Sequence.create("FLIPPING")

# TODO: LATER: these are repeated in every movement... DRY
def mod_and_seq_return(pitches=3, *patterns):
    flipping_tonic.modulate(pitches)
    return seq(*patterns).alter(add_modulate(flipping_tonic))

def mod_and_seq(pitches=3, *patterns):
    FLIPPING.append(mod_and_seq_return(pitches, *patterns))

flip_tags_2 = (["("], [], [".", ">", ")"])

coming_cells = dict(
    a = OutCell("COMING_A").read(),
    b = OutCell("COMING_B").read(),
    c = OutCell("COMING_C").read(),
    d = OutCell("COMING_D").read(),
)

def coming_flip(letter:str="a"):
    my_coming_cell = coming_cells[letter]
    return flipping_cell(degree=my_coming_cell.degree, dur=my_coming_cell.dur)

coming_flip("a").change(
    octave=[0,1,1,2],
    degree=[False,False, 4, 3],
    dur=[False, False, 0.75, 0.25],
    leaf_durs=[False, False, 0.75, 0.25],
    ).tag([],["-"],["-"],[">",".","^"], key="COMING_FLIP_A_SWAP"),

# TODO: EVENTUALLY make this universal somewhere
def flip_wrap(key_prefix:str, pattern:rain.Pattern, bookend_rests=(0,0), bookend_machine="PIANO1", **kwargs):
    if bookend_rests[0] or bookend_rests[1]:
        return_pattern = rain.Sequence.create(key_prefix+"_BOOKEND")
        if bookend_rests[0]:
            return_pattern.append(rest_all(bookend_rests[0], bookend_machine))
        return_pattern.append(pattern)
        if bookend_rests[1]:
            return_pattern.append(rest_all(bookend_rests[1], bookend_machine))
    else: return_pattern = pattern
    # return_pattern = pattern
    return return_pattern

def flip(key_prefix:str=None, intro_times=0, start_tags=(), **kwargs):
    key_prefix = key_prefix or rain.auto_key()
    # return OutCell.create(degree=[1],dur=[1])
    return flip_wrap(key_prefix, seq(key_prefix+"_SEQ",
        *[par(key_prefix+"_INTRO"+str(i), 
            flipping_cell(key_prefix+"_INTRO_HI"+str(i), degree=(0,2), dur=(0.5,0.5), 
                tags=(["."] if i==0 else [".",")"], [">", "("]),
                )(octave=1, machine="PIANO1"),
            flipping_cell(key_prefix+"_INTRO_LOW"+str(i), degree=(0,0), dur=(0.5,0.5), 
                tags=(["."], [">"]),
                )(machine="PIANO2"),
            ) for i in range(intro_times)],
        par(key_prefix+"_A", 
            flipping_cell(key_prefix+"_A_HI", degree=(0,2,4), dur=(0.5,0.5,0.25), 
                tags=(["."] if intro_times==0 else [".",")"], [">", "("], [".", ")"]),
                )(octave=1, machine="PIANO1"),
            flipping_cell(key_prefix+"_A_LOW", degree=(0,0), dur=(0.5,0.75), 
                tags=(["."], [">"]),
                )(machine="PIANO2"),
            ),
        par(key_prefix+"_B", 
            flipping_cell(key_prefix+"_B_HI", degree=(1,3,5), dur=(0.25,0.25,0.25),
                tags=flip_tags_2,
                )(octave=1, machine="PIANO1"),
            OutCell(key_prefix+"_A_HI").alter_leaves(tags=flip_tags_2)(key_prefix+"_B_LOW", dur=0.25)(machine="PIANO2"),
            ),
        ), **kwargs)
      

flipping_cell("FLIPPING_4THS_0", degree=cycle( ((0,3,6),) ), dur=(0.5,), tags=cycle((("^",),)) ),
flipping_cell("FLIPPING_STRIKE_0", degree=cycle( ((-3,4),) ), dur=(0.5,), tags=cycle((("^",),)) )

# TODO: implement tremolo degree
def flip_flute(key_prefix:str=None, degree=0, soft_dynamic="p", end_dynamic="f", flip_degree=None, dur=3, attack_dur=0.5, punct_dur=0.5, 
        octave=1, tremolo_degree=None, bookend_rests=(0,0),**kwargs):
    key_prefix = key_prefix or rain.auto_key()
    flip_degree = flip_degree or degree
    my_flip = flipping_cell(
        dur=[attack_dur, dur-attack_dur-punct_dur, punct_dur],
        degree = [degree, degree,degree, ],
        octave = [octave, octave, octave],
        tags=(["f",">","~"],[soft_dynamic,"\<"],[end_dynamic,"^",".",">"]),
        )(machine="FLUTE")
    return flip_wrap(key_prefix, my_flip, bookend_rests=bookend_rests, 
        bookend_machine="FLUTE", **kwargs)

def flip_out(key_prefix:str=None, octave=0, times=1, **kwargs):
    key_prefix = key_prefix or rain.auto_key()
    dur = [0.25 for i in range(times)]
    if (times % 2)== 1:
        dur[-1] = 0.5
    return flip_wrap(key_prefix, par(key_prefix+"_SEQ_CLUSTER", 
            rain.Cell("FLIPPING_4THS_0").alter_leaves(dur=dur)(key_prefix+"_4THS", octave=octave+1, machine="PIANO1"),
            rain.Cell("FLIPPING_STRIKE_0").alter_leaves(dur=dur)(key_prefix+"_STRIKE", octave=octave, machine="PIANO2"),
        ), **kwargs)

def flip_cluster(key_prefix:str=None, times=1, degrees=(0,1,2,3,4), **kwargs):
    key_prefix = key_prefix or rain.auto_key()
    
    dur = [0.25 for i in range(times*2-1)] + [1.25] if times % 2 == 0 else [0.75]
    tags = [["."] for i in range(times*2-1)] + [["-", ">"]]
    # TODO: don't need this Parallel wrapper unless adding flute ...
    return flip_wrap(key_prefix, rain.Parallel.create(key_prefix+"_PAR_STRIKES").extend(
            flipping_cell(key_prefix+"_HI", degree=cycle( (degrees,) ), dur=dur, tags=tags,
                octave=cycle((1,0)), machine=cycle(("PIANO1", "PIANO2"))
            )
        ), **kwargs)

# =================================================================================

# TODO: ledger lines for flute, or 8va?

#TODO: MAYBE ADD SPACE
FLIPPING.extend(
    # TODO: tag piano with treble clef from the start
    par(
        seq(
            # TODO: add tremolo
            flip_flute("FLIPF_0", degree=1, octave=2, dur=2, bookend_rests=(2.5,0.5),
                )
        ),
        seq(
            flip("FLIP0").meddle(
                M("FLIP0_A_LOW").tag(["treble"])
                ).tag(["f"]),
            flip_out("FLIPPING0", bookend_rests=(0.5,1)), #TODO: start with single 4ths before stacked 4ths
            flip_out("FLIPPING1", times=2, bookend_rests=(0,1.5)),
            flip("FLIP1", intro_times=2),
        ),
    )(pitch_spell="SHARP")
)
# MEASURE 2.5 ===========================================================
mod_and_seq(3,
    par(
        seq(
            # TODO: add tremolo
            flip_flute("FLIPF_1", degree=0, octave=2, dur=4.5, bookend_rests=(0.5,1),),
            flip_flute("FLIPF_2", degree=-1, octave=2, dur=3, bookend_rests=(5.5,2.5),),
            coming_flip("a").change(
                octave=[0,1,2,1],
                ).tag([],["-"],[".",">"])(machine="FLUTE"),
        ),
        seq(
            flip_out("FLIPPING0A", bookend_rests=(0.5,1)),
            flip_cluster(times=2),
            flip_out("FLIPPING2", times=3, bookend_rests=(0,1)),
            flip("FLIP2", intro_times=3),
            flip_out("FLIPPING3", times=1, bookend_rests=(0.5,2)),
            flip_out("FLIPPING4", times=8, bookend_rests=(0,2)),
            flip_cluster(times=4, bookend_rests=(0,1)), # TODO: times=1 doesn't work. WHY?
        ),
    )(pitch_spell="FLAT")
)

# MEASURE 7.75 ===========================================================
mod_and_seq(3,
    par(
        seq(
            # TODO: add tremolo
            # flip_flute("FLIPF_3", degree=0, octave=2, dur=4.5, bookend_rests=(0.5,1),),
            # flip_flute("FLIPF_4", degree=-1, octave=2, dur=3, bookend_rests=(5.5,3.5),),
            rest_all(4, "FLUTE"),
            OutCell("COMING_FLIP_A_SWAP"),
            rest_all(6, "FLUTE"),
            OutCell("COMING_FLIP_A_SWAP"),
            flip_flute("FLIPF_3", degree=-2, octave=2, dur=6, bookend_rests=(0.5,2),),
            coming_flip("c").alter_leaves(dur=[1,0.5,0.5,1.5],).change(
                octave=[0,0,0,0,1],
                ).tag([],["-"],[".",">"])(machine="FLUTE"),
        )(pitch_spell="FLAT", machine="FLUTE"),
        seq(
            flip("FLIP3", intro_times=4, bookend_rests=(0,1))(pitch_spell="FLAT"),
            flip("FLIP4", intro_times=5)(pitch_spell="FLAT"),
            flip_out("FLIPPING5", bookend_rests=(0.5,1)),
            flip_out("FLIPPING6", times=2, bookend_rests=(0,1.5))(pitch_spell="FLAT"),
            flip_out("FLIPPING7", times=4, bookend_rests=(0,1))(pitch_spell="FLAT"),
            flip_out("FLIPPING8", times=12, bookend_rests=(0,1))(pitch_spell="FLAT"),
            flip_cluster(times=2)(pitch_spell="SHARP"),
        ),
    )
)
# MEASURE 15.5 ===========================================================
mod_and_seq(3,
    par(
        seq(
            flipping_cell(degree=[3], octave=[1], dur=[0.5], tags=[[".",">","^"]]),
            coming_flip("d").change(dur=[0.5,1,1,1], octave=[0,0,0,1,]).tag(
                [],[".",">"],[".",">"],[".",">"],),
            flipping_cell(degree=[None,3,None], octave=[0,1,0], dur=[0.5,0.5,1], tags=[[],[".",">","^"],[]]),
            OutCell("COMING_FLIP_A_SWAP"),
        )(machine="FLUTE")(pitch_spell="SHARP"),
        seq(
            flip_out("FLIPPING9", times=2, bookend_rests=(0,0.5)),
            flip("FLIP5", intro_times=1),
            flip_out("FLIPPING10", times=1, bookend_rests=(0.5,0)),
            flip("FLIP6", intro_times=1),
        )(pitch_spell="SHARP")
    )
)

mod_and_seq(3,
    par(
        seq(
            flip_flute("FLIPF_4", soft_dynamic="mf", end_dynamic="ff", degree=-1, octave=3, dur=2.5, bookend_rests=(0.5,0),),
            flip_flute("FLIPF_5", soft_dynamic="mf", end_dynamic="ff", degree=0, octave=3, dur=2.5, bookend_rests=(0.5,0),),
        )(machine="FLUTE")(pitch_spell="SHARP"),
        seq(
            flip_out("FLIPPING11", octave=1, times=1, bookend_rests=(0.5,0)),
            flip_out("FLIPPING12", octave=1, times=4, bookend_rests=(0.5,0)),
            flip_out("FLIPPING13", octave=1, times=1, bookend_rests=(0,0)),
            flip_out("FLIPPING14", octave=1, times=1, bookend_rests=(0.5,0)),
            flip_out("FLIPPING15", octave=1, times=1, bookend_rests=(0.5,0)),
            flip_out("FLIPPING16", octave=2, times=1, bookend_rests=(0.5,0)).meddle(
        M("FLIPPING16_4THS").tag(["8va"], )
        ),
        )(pitch_spell="SHARP")
    )
    # # # TODO MAYBE: a longer pause before this last
)

mod_and_seq(3,
    rest_all(1),
    flip_out("FLIPPING17", octave=2, times=28).meddle(
        M("FLIPPING17_4THS").tag(["ff"], *([],)*26, ["8va!", "|."] )
        ),
)

print(flipping_tonic.tonic)

    # # TODO: WHAT WAS THIS????
    # # seq("FLIP_FLIP_OUT"), 
    # # flip_out("FLIPPING1", times=2),
    # # rest_all(1.5, "PIANO1"),
    # # flip(intro_times=2)(pitch_spell="FLAT"),
    # # rest_all(0.5, "PIANO1"),
    # # flip_out("FLIPPING2", times=4),


FLIPPING = FLIPPING.tag(["tempo:132:1:4:Angry"])

if __name__ == "__main__":
    score = score_with_meter()
    score.reset()
    pr = rain.PatternReader(FLIPPING, score.get_palette())
    pr.read()
    score.render("FLIPPING")