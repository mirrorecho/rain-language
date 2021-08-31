from abjad import score
import rain

from rain.score import meters

#TODO: revisit this implementation
# ESPECIALLY... rethink should the Score node really carry the meter??? 
# INSTEAD, should be part of the cell tree structure
def score_with_meter(meter=meters.METER_4_4):
    return rain.Score.create("OUT_SCORE", meter=meter).extend(
        rain.Staff.create("FLUTE", "Flute", meter=meter),
        rain.StaffGroup.create("PIANO").extend(
            rain.Staff.create("PIANO1", "Piano 1", meter=meter),
            rain.Staff.create("PIANO2", "Piano 2", meter=meter),
        )
    )


def rest_all(dur:int):
    return rain.Parallel.create().extend(
        rain.rest(dur)(machine="FLUTE"),
        rain.rest(dur)(machine="PIANO1"),
        rain.rest(dur)(machine="PIANO2"),
    )
