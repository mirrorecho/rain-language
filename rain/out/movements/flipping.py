from itertools import cycle, repeat

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, add_modulate)
from rain.out.score_machine import score_with_meter, rest_all
from rain import ref, par, seq, par_ref, seq_ref

M = rain.MeddleHelper

# TODO: MAYBE change start global tonic?
flipping_cell = OutCellFactory(mode=6, global_tonic=GlobalTonic(-2))
flipping_tonic = GlobalTonic(-2)

FLIPPING = rain.Sequence.create("FLIPPING")

# TODO: these are repeated in every movement... DRY
def mod_and_seq_return(pitches=2, *patterns):
    flipping_tonic.modulate(pitches)
    return seq(*patterns).alter(add_modulate(flipping_tonic))

def mod_and_seq(pitches=2, *patterns):
    FLIPPING.append(mod_and_seq_return(pitches, *patterns))

flip_tags_2 = (["("], [], [".", ">", ")"])

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
            flipping_cell(key_prefix+"INTRO_HI"+str(i), degree=(0,2), dur=(0.5,0.5), 
                tags=(["."] if i==0 else [".",")"], [">", "("]),
                )(octave=1, machine="PIANO1"),
            flipping_cell(key_prefix+"INTRO_LOW"+str(i), degree=(0,0), dur=(0.5,0.5), 
                tags=(["."], [">"]),
                )(machine="PIANO2"),
            ) for i in range(intro_times)],
        par(key_prefix+"_A", 
            flipping_cell(key_prefix+"A_HI", degree=(0,2,4), dur=(0.5,0.5,0.25), 
                tags=(["."] if intro_times==0 else [".",")"], [">", "("], [".", ")"]),
                )(octave=1, machine="PIANO1"),
            flipping_cell(key_prefix+"A_LOW", degree=(0,0), dur=(0.5,0.75), 
                tags=(["."], [">"]),
                )(machine="PIANO2"),
            ),
        par(key_prefix+"_B", 
            flipping_cell(key_prefix+"B_HI", degree=(1,3,5), dur=(0.25,0.25,0.25),
                tags=flip_tags_2,
                )(octave=1, machine="PIANO1"),
            OutCell(key_prefix+"A_HI").alter_leaves(tags=flip_tags_2)(key_prefix+"B_LOW", dur=0.25)(machine="PIANO2"),
            ),
        ), **kwargs)
      

flipping_cell("FLIPPING_4THS_0", degree=cycle( ((0,3,6),) ), dur=(0.5,), tags=cycle((("^",),)) ),
flipping_cell("FLIPPING_STRIKE_0", degree=cycle( ((-3,4),) ), dur=(0.5,), tags=cycle((("^",),)) )


def flip_out(key_prefix:str=None, times=1, **kwargs):
    key_prefix = key_prefix or rain.auto_key()
    dur = [0.25 for i in range(times)]
    if (times % 2)== 1:
        dur[-1] = 0.5
    return flip_wrap(key_prefix, par(key_prefix+"_SEQ_CLUSTER", 
            rain.Cell("FLIPPING_4THS_0").alter_leaves(dur=dur)(key_prefix+"4THS", octave=1, machine="PIANO1"),
            rain.Cell("FLIPPING_STRIKE_0").alter_leaves(dur=dur)(key_prefix+"STRIKE", machine="PIANO2"),
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

#TODO: ADD SPACE
FLIPPING.extend(
    flip("FLIP0").tag(["f"])(pitch_spell="FLAT"),
    flip_out("FLIPPING0", bookend_rests=(0.5,1)), #TODO: start with single 4ths before stacked 4ths
    flip_out("FLIPPING1", times=2, bookend_rests=(0,1.5)),
    flip("FLIP1", intro_times=2),
    # OutCell("FLIPPING0"),
    # flip_cluster(times=2),
    # flip_out("FLIPPING2", times=3, bookend_rests=(0,1)),
    # flip("FLIP2", intro_times=3),
    # flip_out("FLIPPING3", times=1, bookend_rests=(0.5,2)),
    # flip_out("FLIPPING4", times=8, bookend_rests=(0,2)),
    # flip_cluster(times=4, bookend_rests=(0,1)), # TODO: times=1 doesn't work. WHY?
    # flip("FLIP3", intro_times=4, bookend_rests=(0,1)),
    # flip("FLIP4", intro_times=5),
    # flip_out("FLIPPING5", bookend_rests=(0.5,1)),
    # flip_out("FLIPPING6", times=2, bookend_rests=(0,1.5)),
    # flip_out("FLIPPING7", times=4, bookend_rests=(0,1)),
    # flip_out("FLIPPING8", times=12, bookend_rests=(0,1)),
    # flip_cluster(times=2),
    # flip_out("FLIPPING9", times=2, bookend_rests=(0,0.5)),
    # flip("FLIP5", intro_times=1),
    # flip_out("FLIPPING10", times=1, bookend_rests=(0.5,0)),
    # flip("FLIP6", intro_times=1),
    # flip_out("FLIPPING11", times=1, bookend_rests=(0.5,0)),
    # flip_out("FLIPPING12", times=4, bookend_rests=(0.5,0)),
    # flip_out("FLIPPING13", times=1, bookend_rests=(0,0)),
    # flip_out("FLIPPING14", times=1, bookend_rests=(0.5,0)),
    # flip_out("FLIPPING15", times=1, bookend_rests=(0.5,0)),
    # flip_out("FLIPPING16", times=1, bookend_rests=(0.5,0)),
    # # # TODO MAYBE: a longer pause before this last
    # flip_out("FLIPPING17", times=32),

    # # TODO: WHAT WAS THIS????
    # # seq("FLIP_FLIP_OUT"), 
    # # flip_out("FLIPPING1", times=2),
    # # rest_all(1.5, "PIANO1"),
    # # flip(intro_times=2)(pitch_spell="FLAT"),
    # # rest_all(0.5, "PIANO1"),
    # # flip_out("FLIPPING2", times=4),
)

FLIPPING = FLIPPING.tag(["tempo:132:1:4:Angry"])

if __name__ == "__main__":
    score = score_with_meter()
    score.reset()
    pr = rain.PatternReader(FLIPPING, score.get_palette())
    pr.read()
    score.render("FLIPPING")