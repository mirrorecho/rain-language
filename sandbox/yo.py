from dataclasses import dataclass, field

import abjad

from rain.score import tagging



dur = (1, 4.5, 4.5, 24, 0.25, 0.125, 1, 1, 0.125)
pitch = (0, 5, 4, None, 5,    4,     0, 2, 4)
force_dur = [0.5, 0.5, 1, 2] + [2 for i in range(16)] + [0.5]

current_node = meter.root_node
current_meter_offset = 0
rest_sum = 0

container = abjad.Container()

def next_sibling_or_aunt(node):
    rel_node = node.root
    if not rel_node:
        # iff node is already root, than node.root is None
        # so just return node
        return node

    graph_order = node.graph_order
    ancestor_index = -1
    while node.parent is not None:
        node = node.parent
        sibling_index = graph_order[ancestor_index] + 1
        if len(node) > sibling_index:
            rel_node = node[sibling_index]
            break
        ancestor_index -= 1
    return rel_node


# TODO: handle pickup case
# if self.pickup:
#     # if there's a pickup, try to match metrical node with the pickup...
#     pickup_pair = (1, int((1 / self.pickup) * calliope.MACHINE_BEATS_PER_WHOLE))
#     current_node = next((n for n in reversed(current_node.nodes) if n.duration.pair == pickup_pair), current_node)


def trigger_lt(dur, pitch, force_durs=None):

    global current_node, current_meter_offset, rest_sum

    def meter_node_dur(node):
        meter_pair = node.duration.pair 
        return meter_pair[0]/meter_pair[1]*4


    if force_durs:
        durs = force_durs

    else:
        durs = []
        dur_remaining = dur

        while dur_remaining > 0:

            while meter_node_dur(current_node) > dur_remaining \
                    and isinstance(current_node, abjad.rhythmtrees.RhythmTreeContainer):
                current_node = current_node[0]
            
            dur_meter = meter_node_dur(current_node)

            if dur_meter >= dur_remaining:
                durs.append(dur_remaining)
                current_meter_offset = dur_remaining
                dur_remaining = 0

            else:
                durs.append(dur_meter)
                dur_remaining -= dur_meter
                # current_meter_offset = 0 # needed?
            
            # if current_meter_offset == 0:
            current_node = next_sibling_or_aunt(current_node)

    leaves = []

    if pitch is not None:  
        for d in durs:
            leaves.append(abjad.Note.from_pitch_and_duration(pitch, d/4))
        if len(leaves) > 1:
            abjad.tie(leaves)
    else:
        for d in durs:
            leaves.append(abjad.Rest(d/4))

    container.extend(leaves)

trigger_lt(3, None)
trigger_lt(3, None)
trigger_lt(0.25, None)
trigger_lt(0.125, 0)
trigger_lt(4, 2)
# trigger_lt(0.5, 4)
# trigger_lt(5, 2)
# trigger_lt(6, None)

abjad.show(container, 
    output_directory="./rain-language/sandbox", 
    should_open=False,
    render_prefix="yomama",
    )


""" LOGIC BELOW IS:
- REPEAT WHILE CURRENT NODE STARTS BEFORE END OF LT
    - while current node ends after lt and able to sub-divide, then sub-divide
    - add current node
    - current node moves to next sibling or next aunt or root
- MOVE TO NEXT LT
"""

# from abjad import rhythmtrees

# # rt = abjad.rhythmtrees.R
# rhythmtrees.mutate()

# c = abjad.Container("c'4 d'4. f'8 e'4")

# abjad.show(c, 
#     output_directory="./rain-language/sandbox", 
#     should_open=False,
#     render_prefix="yomama",
#     )