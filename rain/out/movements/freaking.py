from itertools import cycle, repeat

import rain
import abjad


osti1 = rain.MusicCell.create("FREAKING_O1",
    pitch=(3,4,6,4),
    dur=cycle((0.5,)),
    tags=cycle((None,)),
    machine=cycle(("PIANO1",)),
)

flute_osti1 = rain.AlterPatternAttrs.create("FLUTE_OSTI1")
flute_osti1.setup_attrs(dur=cycle((1,)),)
rain.Alters.create(source=flute_osti1, target=osti1)


flute_osti2 = rain.AlterPatternAttrs.create("FLUTE_OSTI2")
flute_osti2.setup_attrs(machine=cycle(("FLUTE",)),)
rain.Alters.create(source=flute_osti2, target=flute_osti1)


FREAKING = rain.Sequence.create("FREAKING").extend(
    flute_osti2
)

if __name__ == "__main__":
    from rain.out.score_machine import OUT_SCORE
    OUT_SCORE.reset()
    pr = rain.PatternReader(FREAKING, OUT_SCORE.get_palette())
    pr.read()
    OUT_SCORE.render()