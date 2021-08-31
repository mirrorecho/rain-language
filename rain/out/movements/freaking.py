from itertools import cycle, repeat

import rain

from rain.out.out_cell import OutCell, OutCellFactory
from rain.out.score_machine import score_with_meter, rest_all

start_tonic = 4
freaking_cell = OutCellFactory(mode=3, tonic=start_tonic)

rain.Sequence.create("FREAKING_SEQ").extend(
    freaking_cell("FREAKING1", degree=(-4,-1,0,-1), dur=cycle((0.5,)) ),
    freaking_cell("FREAKING2", degree=(-3,-1,0,-1), dur=cycle((0.5,)) ),
    freaking_cell("FREAKING3", degree=(-3,-2,0,-2), dur=cycle((0.5,)) ),
    freaking_cell("FREAKING4", degree=(-3,-2,1,-2), dur=cycle((0.5,)) ),
)

freaking_bass1 = freaking_cell("FREAKING_BASS1", 
    degree=(-14, (-12, -7), -14, (-10, -7),),
    dur=cycle((1,)),
    tags=(["(", "bass"],[")"],["("],[")"],),
    )

freaking_bass2 = freaking_cell("FREAKING_BASS2", 
    degree=(-16, (-14, -9), -16, (-11, -9),),
    dur=cycle((1,)),
    tags=(["("],[")"],["("],[")"],),
    )

freaking_bass = rain.Sequence.create("FREAKING_BASS_SEQ").extend(
    freaking_bass1, freaking_bass2
)

rain.Parallel.create("FREAKING_PAR").extend(
    rain.Sequence("FREAKING_SEQ")(machine="PIANO1"),
    freaking_bass(machine="PIANO2"),
)

double_freak = OutCell("FREAKING1")*2

FREAKING = rain.Sequence.create("FREAKING").extend(

    rest_all(4), # TREMOLO just 1 bar?

    (double_freak + OutCell("FREAKING2"))(machine="PIANO1")*2, # lower forarm on keys on first and final 8ths

    rest_all(4), # TREMOLO just 1 bar?

    # flute enters, highlighting the lines in an angular way
    # lower forarm on keys on first and final 8ths    
    (OutCell("FREAKING3") + OutCell("FREAKING2") + OutCell("FREAKING3")*2 )(machine="PIANO1"),

    (OutCell("FREAKING4") + OutCell("FREAKING3"))(machine="PIANO1"),

    rest_all(4), # TREMOLO, with arms on lower keys at start

    (OutCell("FREAKING4")*2 + OutCell("FREAKING1")(tonic=start_tonic+2)*2)(machine="PIANO1"),
    
    rest_all(4), # TREMOLO, with arms on lower keys at start

    rain.Parallel("FREAKING_PAR")(tonic=start_tonic+2), 
    
    rain.Parallel("FREAKING_PAR")(tonic=start_tonic+4),

    # right forarm on keys somewhere in here + RH tremolo
    #TODO: funk this up a bit
    freaking_bass(tonic=start_tonic+6, dur=0.5, machine="PIANO2"), 
    freaking_bass(tonic=start_tonic+8, dur=0.5, machine="PIANO2"), 

    rain.Parallel("FREAKING_PAR")(tonic=start_tonic+10),
    rest_all(4), # TREMOLO, but insert this into the middle of the above
    # after the tremolo, start moving towards parallel

    #emphasize electo sounds from the beginning! (full circle)
    rain.Sequence("FREAKING_SEQ")(tonic=start_tonic, machine="PIANO1"), # parallel motion ... also TODO speed up the harmonic progress
    rain.Sequence("FREAKING_SEQ")(tonic=start_tonic+2, machine="PIANO1"), # parallel motion ... also TODO speed up the harmonic progress
    #abrupt big chord end

    # tonic + 4 (is that OK?)
    rest_all(4), # very low / high temolo, ending with both arms on keys
    rest_all(8), # HYPERVENTILATE INTO FLUTE (air tones only) ... dog whining
)

if __name__ == "__main__":
    score = score_with_meter()
    score.reset()
    pr = rain.PatternReader(FREAKING, score.get_palette())
    pr.read()
    score.render()