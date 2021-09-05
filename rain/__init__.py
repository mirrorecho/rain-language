from rain.utils.utils import (auto_key, to_snake_case, to_upper_snake_case, 
    transpose, rest, listify, pattern_set_branch_hooks)
from rain.utils.scale import Scale

from rain.graph.interface import (GraphableInterface, GraphableNodeInterface, 
    GraphableRelationshipInterface, GraphInterface, SelectInterface)

from rain.graph.local import GraphLocal

from rain.language.context import Context

context = Context(
    GraphLocal # can change to any other graph type to use that type in default context
    )

from rain.language.base import LanguageBase, Language, Node, Relationship
from rain.language.select_ import Select, TargetedRelationshipSelect # note have to name the module select_ (with underscore at end) to avoid namine conflicts with uuid dependencies


from rain.patterns.palette import Palette
from rain.patterns.pattern import AlterableMixin, Pattern
from rain.patterns.cell import Cell, MusicCell, RestCell
from rain.patterns.cue import Cue, Contains, Cues, CueNext, CueFirst, CueLast
from rain.patterns.machine import Machine, Printer #, SynthDefMaker
from rain.patterns.tree_pattern import TreePattern, CellTree, Sequence, Parallel, Combo, MachineTree
from rain.patterns.alters import (AlterPattern, Alters, AlterPatternVeins, 
    AlterPatternLeaves, AlterPatternTagVeins, Change, MeddleHelper, Meddle, MeddleConnectAlter)
from rain.patterns.pattern_reader import PatternReader

from rain.score.staff import Staff
from rain.score.staff_group import StaffGroup
from rain.score.score import Score

# ADDTIONAL IMPORTS THAT ARE NOT NODES IN THE GRAPH
from rain.patterns.alters import Meddle

# TO DO: use decorator instead of registering here
context.register_types(
    Language, Node, Relationship,
    Pattern, Cell, Cue, Contains, Cues,
    CueNext, CueFirst, CueLast, TreePattern, MachineTree, Machine,
    CellTree, Sequence, Parallel, Combo,
    AlterPattern, Alters, AlterPatternVeins, AlterPatternLeaves, AlterPatternTagVeins, 
    Change, Meddle, MeddleConnectAlter,
    MusicCell, RestCell,
    Staff, StaffGroup, Score )

def ref(key:str):
    return context.new_by_key(key)