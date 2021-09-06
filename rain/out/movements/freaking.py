from itertools import cycle, repeat

import rain

from rain.out.out_cell import (GlobalTonic, OutCell, OutCellFactory, AddDegrees, Mask,
    add_modulate)
from rain.out.score_machine import score_with_meter, rest_all

M = rain.MeddleHelper

# TODO: likely change start global tonic
freaking_cell = OutCellFactory(mode=3, global_tonic=GlobalTonic(4))
freaking_tonic = GlobalTonic(4)

FREAKING = rain.Sequence.create("FREAKING")

def mod_and_seq(*patterns):
    freaking_tonic.modulate(2)
    FREAKING.append(
        rain.Sequence.create().extend(*patterns).alter(add_modulate(freaking_tonic))
    )

rain.Parallel.create("FREAKING_PAR").extend(
    rain.Sequence.create("FREAKING_SEQ").extend(
        freaking_cell("FREAKING1", degree=(-4,-1,0,-1), dur=cycle((0.5,)) ),
        freaking_cell("FREAKING2", degree=(-3,-1,0,-1), dur=cycle((0.5,)) ),
        freaking_cell("FREAKING3", degree=(-3,-2,0,-2), dur=cycle((0.5,)) ),
        freaking_cell("FREAKING4", degree=(-3,-2,1,-2), dur=cycle((0.5,)) ),
    ),
    rain.Sequence.create("FREAKING_BASS_SEQ").extend(
        freaking_cell("FREAKING_BASS1", 
            degree=(-14, (-12, -7), -14, (-10, -7),),
            dur=cycle((1,)),
            tags=cycle((["("],[")"])),
            ),
        freaking_cell("FREAKING_BASS2", 
            degree=(-16, (-14, -9), -16, (-11, -9),),
            dur=cycle((1,)),
            tags=cycle((["("],[")"])),
            )
    ) #.alter_leaves("FREAKING_BASS_SEQ_SLURRED", tags=cycle((["("],[")"]))) # TODO: sluring doesn't come out right... why?
)

rain.Parallel("FREAKING_PAR").meddle("FREAKING_PAR_PIANO",
    M("FREAKING_SEQ")(machine="PIANO1"),
    M("FREAKING_BASS_SEQ")(machine="PIANO2"), 
    ) 

double_freak = OutCell("FREAKING1")*2

FREAKING.extend(

    rest_all(4), # TREMOLO just 1 bar?

    ((double_freak + OutCell("FREAKING2"))*2).tag(["f"])(machine="PIANO1"), # lower forarm on keys on first and final 8ths

    rest_all(4), # TREMOLO just 1 bar?

    # flute enters, highlighting the lines in an angular way
    # lower forarm on keys on first and final 8ths    
    (OutCell("FREAKING3") + OutCell("FREAKING2") + OutCell("FREAKING3")*2 )(machine="PIANO1"),

    (OutCell("FREAKING4") + OutCell("FREAKING3"))(machine="PIANO1"),

    rest_all(4), # TREMOLO, with arms on lower keys at start

    (OutCell("FREAKING4")*2)(machine="PIANO1") 
)

mod_and_seq(
    (OutCell("FREAKING1")*2)(machine="PIANO1"),

    rest_all(4), # TREMOLO, with arms on lower keys at start

    rain.Parallel("FREAKING_PAR_PIANO").meddle(
        M("FREAKING_BASS_SEQ").tag(["bass"]), # TODO: bass should be at beginning of the staff
        ), 
    )

mod_and_seq(
    rain.Parallel("FREAKING_PAR_PIANO")
    )

#TODO: funk this up a bit
# right forarm on keys somewhere in here + RH tremolo
mod_and_seq(
    rain.Sequence("FREAKING_BASS_SEQ")(dur=0.5, machine="PIANO2")
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


if __name__ == "__main__":
    score = score_with_meter()
    score.reset()
    pr = rain.PatternReader(FREAKING, score.get_palette())
    pr.read()
    score.render()