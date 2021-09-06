from abjad import score
import rain

from rain.score import meters
from rain.out.out_cell import OutCell

#TODO: revisit this implementation
# ESPECIALLY... rethink should the Score node really carry the meter??? 
# INSTEAD, should be part of the cell tree structure
def score_with_meter(meter=meters.METER_4_4, piano1_clef="treble", piano2_clef="bass"):
    return rain.Score.create("OUT_SCORE", meter=meter).extend(
        rain.Staff.create("FLUTE", "Flute", meter=meter),
        rain.StaffGroup.create("PIANO", group_type="PianoStaff").extend(
            rain.Staff.create("PIANO1", "Piano 1", meter=meter, clef=piano1_clef),
            rain.Staff.create("PIANO2", "Piano 2", meter=meter, clef=piano2_clef),
        )
    )


def rest_all(dur:int, *args):
    if not args:
        args = ("FLUTE", "PIANO1", "PIANO2")
    return rain.Parallel.create().extend(
        *[OutCell.create(dur=[dur], degree=[None])(machine=m) for m in args]
    )
