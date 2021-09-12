import rain
from math import floor, ceil

TOTAL_POMO = 122

FREAKING_BARS_COMPLETE = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,8,19,20,21,22,23,24,25,26,27,28]
SPACING_BARS_COMPLETE = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
PASSING_BARS_COMPLETE = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
MAKING_BARS_COMPLETE = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
    25,26,27,28,29,30,31]
BURNING_BARS_COMPLETE = []
FLIPPING_BARS_COMPLETE = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
COMING_BARS_COMPLETE = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,
    23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]

total_bars_complete = len(FREAKING_BARS_COMPLETE+SPACING_BARS_COMPLETE+PASSING_BARS_COMPLETE+
    MAKING_BARS_COMPLETE+BURNING_BARS_COMPLETE+FLIPPING_BARS_COMPLETE+COMING_BARS_COMPLETE)

freaking_bars = 28
spacing_bars = 14
passing_bars = 16
making_bars = 31
burning_bars = 18
flipping_bars = 20
coming_bars = 39

total_bars = (freaking_bars + spacing_bars + passing_bars + making_bars + burning_bars
    + flipping_bars + coming_bars)

bars_per_pomo = 1.2
total_pomos_alloted = total_bars/bars_per_pomo

variance = total_bars_complete - (TOTAL_POMO*bars_per_pomo)
bars_remaining = total_bars-total_bars_complete

def pomo_time(pomos):
    return str(floor(pomos*10/60)) + " HOURS, " + str(round(pomos*10) % 60) + " MINUTES"

print()
print()
print("================================================")

print("TOTAL BARS TO WRITE: ", total_bars)
print("TOTAL POMOS ALLOTTED: ", total_pomos_alloted, " - TAKING ", pomo_time(total_pomos_alloted))
print()
print("================================================")

print("WRITTEN: ", total_bars_complete)
print("POMOS USED: ", TOTAL_POMO, " - HAVING TAKEN ", pomo_time(TOTAL_POMO))
print()
print("================================================")
if variance < 0:
    print("OH NO! BEHIND BY", (0-variance), "BARS!")
    print("SHOULD USE 2 POMOS, or 20 MINUTES, FOR THE NEXT", (0-variance)+bars_per_pomo*2, "BARS")
elif variance == 0:
    print("YAY! EXCACTLY ON TRACK!")
else:
    print("YAY !!!! AHEAD BY", variance, "BARS")
    print((variance/bars_per_pomo)+1, "POMOS, OR", pomo_time((variance/bars_per_pomo)+1), " TO WORK WITH")
print()
print("================================================")
print("REMAINING: ", bars_remaining, "BARS")
print("EXPECTED POMOS NEEDED: ", ceil(bars_remaining/bars_per_pomo), " - TAKING ", pomo_time(bars_remaining/bars_per_pomo))

print()
print("================================================")
print()