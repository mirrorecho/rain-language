from itertools import cycle, repeat

import rain
import abjad

flute = rain.Staff.create("FLUTE", "Flute")

piano1 = rain.Staff.create("PIANO1", "Piano 1")
piano2 = rain.Staff.create("PIANO2", "Piano 2")
piano = rain.StaffGroup.create("PIANO").extend(
    piano1,
    piano2,
)

score = rain.Score.create("OUT_SCORE").extend(
    flute,
    piano,
)

c1 = rain.MusicCell.create(
    key="C1",
    pitch=(0,0,3,4,3),
    dur=cycle((1,2,)),
    machine=cycle(("FLUTE",)),
    tags = (
        ("~", ">", "\\<",),
        ("-", "(", "((", ":16", "longfermata", "8vb"),
        (".", ")", "||"),
        ("-", "p"),
        ("))", "8vb!"),
    ), # BEWARE OF THIS!
)

pn1 = rain.MusicCell.create(
    key="PN1",
    pitch=((1,3), 5, 4, 7),
    pitch_spell=("FLAT", None, None, None),
    dur=(0.5, 0.5, 0.5, 0.5),
    machine=cycle(("PIANO1",)),
    tags = (
        ("["),
        ("]",),
        ("[",),
        ("]",),
    ), # BEWARE OF THIS!
)

pn2 = rain.MusicCell.create(
    key="PN2",
    pitch=(-12, -8),
    dur=(1.5, 4.5),
    machine=cycle(("PIANO2",)),
    tags = cycle((None,)), # BEWARE OF THIS!
)

def double_dur(pattern):
    pattern.dur = [p*2 for p in pattern.dur]
    return pattern

def up8(pattern):
    pattern.pitch = [p+8 for p in pattern.pitch]
    return pattern

pn1a = rain.AlterPattern.create("PN1A", alter = double_dur)

rain.Alters.create(source=pn1a, target=pn1)

fup = rain.AlterCue.create("FUP", alter = up8)

par1 = rain.Parallel.create().extend(
    c1, pn1, pn2
)

rain.Alters.create(source=fup, target=par1.r("->", "CUE_FIRST").n().first)

par1a = rain.Parallel.create().extend(
    c1, pn1a, pn2
)

s1 = rain.Sequence.create().extend(
    par1, par1a, par1,
)



print("============================================================")

# for x in pn1a.nodes:
#     print(x)

# s1[1][0].alter[0](pitch=3)

# m1 = rain.Meter.create(meter_durations=(1,1,1,1))
# ctx = rain.Context.create(source=s1, target=m1)

print("--------------------------------")
score.reset()
pr = rain.PatternReader(s1, score.get_palette())
pr.read()
score.render()

# print(s1.r("->", "CONTEXT").n().first)
# print(score.branches[0] is score.branches[0])


# s = abjad.Staff()
# s.append(abjad.Container((abjad.Note("ds'4"),)))
# abjad.show(s, 
#     output_directory="./rain-language/rain/out/scores/", 
#     should_open=False,
#     render_prefix="yomama",
# )