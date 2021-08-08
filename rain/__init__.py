from rain.utils import auto_key, to_snake_case, to_upper_snake_case

from rain.graph.interface import (GraphableInterface, GraphableNodeInterface, 
    GraphableRelationshipInterface, GraphInterface, SelectInterface)

from rain.graph.local import GraphLocal

from rain.language.context import Context

context = Context(
    GraphLocal # can change to any other graph type to use that type in default context
    )

from rain.language.base import LanguageBase, Language, Node, Relationship
from rain.language.select_ import Select, TargetedRelationshipSelect # note have to name the module select_ (with underscore at end) to avoid namine conflicts with uuid dependencies

from rain.language.pattern import (Palette, Pattern, Cell, Cue, Contains, Cues,
    CueNext, CueFirst, CueLast, TreePattern, MachineTree, Machine,
    CellTree, Sequence, Parallel, Combo,
    AlterPattern, AlterCue, Alters,
    Context, Meter,
    PatternReader,
    MusicCell,
    )
from rain.score.staff import Staff
from rain.score.staff_group import StaffGroup
from rain.score.score import Score

# TO DO: use decorator instead of registering here
context.register_types(
    Language, Node, Relationship,
    Pattern, Cell, Cue, Contains, Cues,
    CueNext, CueFirst, CueLast, TreePattern, MachineTree, Machine,
    CellTree, Sequence, Parallel, Combo,
    AlterPattern, AlterCue, Alters,
    Context, Meter,
    MusicCell, 
    Staff, StaffGroup, Score )
