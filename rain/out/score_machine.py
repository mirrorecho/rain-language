import rain

flute = rain.Staff.create("FLUTE", "Flute")

piano1 = rain.Staff.create("PIANO1", "Piano 1")
piano2 = rain.Staff.create("PIANO2", "Piano 2")
piano = rain.StaffGroup.create("PIANO").extend(
    piano1,
    piano2,
)

# TODO consider... global variable, or just always return to the data?
OUT_SCORE = rain.Score.create("OUT_SCORE").extend(
    flute,
    piano,
)