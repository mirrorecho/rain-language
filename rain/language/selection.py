import rain

class Selection(rain.SelectionInterface):
    def __init__(self, label:str=None, *keys, **properties):
        self._context = rain.context
        self._label = label
        self._keys = keys
        self._properties = properties
        
        self._relationship_follow = None # COULD BE:

        self._select_from = None # to be set to another instance of Selection to create a sub-selection
        self._direction = None

        
    @property
    def select_from(self) -> rain.SelectionInterface: 
        return self._select_from

    @property
    def direction(self) -> str: 
        return self._direction

    # TO CONSIDER: maybe there shouldn't be a public select_from setter?
    @select_from.setter
    def select_from(self, select:rain.SelectionInterface): 
        self._select_from = select

    @property
    def context(self): 
        return self._context

    @property
    def graph(self): 
        return self.context.graph

    @property
    def label(self) -> str: 
        return self._label

    @property
    def keys(self) -> tuple: 
        return self._keys

    @property
    def properties(self) -> dict: 
        return self._properties

    def set_properties(self, **kwargs): 
        self._properties.update(kwargs)

    def __getitem__(self, k): 
        raise NotImplementedError()

    def __call__(self, label:str=None, *keys, **properties) -> rain.SelectionInterface: 
        sub_selection = Selection(label, *keys, **properties)
        sub_selection.select_from = self
        sub_selection._direction = self._direction # TO DO... this warrants some thought and testing
        return sub_selection

    def r(self, direction:str, label:str=None, *keys, **properties) -> "Selection":
        sub_selection = TargetedRelationshipSelection(direction, label, *keys, **properties)
        sub_selection.select_from = self
        return sub_selection

    def n(self, label:str=None, *keys, **properties) -> "Selection":
        raise NotImplementedError()


class TargetedRelationshipSelection(Selection):
    _supported_directions = ("->", "<-")

    def __init__(self, direction:str, label:str=None, *keys, **properties):
        if direction not in self._supported_directions:
            raise ValueError(f"'{direction}' is not a supported direction value")
        super().__init__(label, *keys, **properties)
        self._direction = direction

    def r(self, direction:str, label:str=None, *keys, **properties):
        raise NotImplementedError("Chaining .r relationship selects not supported (add a .n select between)")

    def n(self, label:str=None, *keys, **properties):
        sub_selection = Selection(label, *keys, **properties)
        sub_selection.select_from = self
        sub_selection._direction = "->()" if self.direction == "->" else "<-()"
        return sub_selection



    # def __init__(self, label:str=None, *keys, **properties):

# lovers = rain.Action.select("LOVES")("<-[:DOES]-")("Expression")("-[:SUBJECT]->")("Character")
# lovers = rain.Select("Action", "LOVES")("<-[:DOES]-")("Expression")("-[:SUBJECT]->")("Character")

# lovers = rain.Action.select("LOVES").r("<-", "DOES").n("Expression").r("->", "SUBJECT").n("Character")

# cells_in_phrase = rain.Select("ROW_AB").r("<-")

# cell_a = rain.Cell("CELL_A", pitch=(0,2,5,4), dur=(1,2,2,1))
# cell_a_bass = rain.Cell("CELL_A_BASS", pitch=(-7,-5), dur=(3,3))
# cell_b = rain.Cell("CELL_B",pitch=(7,5,4), dur=(3,3,2))

# cue_a = rain.Cue(cell_a)
# cue_a_bass = rain.Cue(cell_a_bass)
# cue_b = rain.Cue(cell_b)

# sync_a = rain.Sync(cue_a, cue_a_bass)

# row_ab = rain.Row(sync_a, cue_b)

# #CONTAINS IS AN IMPORTANT RELATIONSHIP FOR PATTERN MATERIAL!!!

# #SHORTCUT

# rain.Cell("CELL_A", pitch=(0,2,5,4), dur=(1,2,2,1)).merge()
# rain.Cell("CELL_A_BASS", pitch=(-7,-5), dur=(3,3)).merge()
# rain.Cell("CELL_B", pitch=(7,5,4), dur=(3,3,2)).merge()

# row_ab = rain.Row(
#     rain.Sync(
#         rain.Cell("CELL_A").cue(machine="flute", engrave_tags=((">","("),None,None,(")",))),
#         rain.Cell("CELL_A_BASS").cue(machine="cello", engrave_tag=("_",)),
#     ), 
#     rain.Cell("CELL_B").cue(machine="flute"),
#     ).merge()

# # OR EVEN MORE:

# rain.Cell("CELL_B", pitch=(7,5,4), dur=(3,3,2)).merge()



# calliope.translate_score(row_ab)

# b = Bubble()

# lovers = rain.Action.select("LOVES")("<-[:DOES]-")("Expression")("-[:SUBJECT]->")("Character")

# lovers_ = Selection("Action", "LOVES", "HATES")("<-[:DOES]-")("Expression")("-[:SUBJECT]->")("Character")


# class Selectable():

#     def related_to(self): pass

#     def related_from(self): pass

#     def relationships_to(self): pass

#     def relationships_from(self): pass

#     @classmethod
#     def select(cls): pass

# class Select(Selectable):

#     def __init__(self): pass

#     def __getitem__(self, k): pass

#     def __call__(self, *args, **kwargs): pass


# Character.select("AWN", "CEP").relationships_from("Subject").sources("Expression")
# Expression.select("AWN")

# # get any set of data by:

# # - label(s)
# Language.select("Character", "Action") # (all characters and actions)
# Character.select # (another way to express all characters)

# # - key(s)
# Language.select["AWN", "CEP", "LOVING"] # any type of data with keys, AWN, CEP, or LOVING

# # - property value(s)
# Language.select(fancy=True) # any type of data with "fancy" property having value of True

# # can chain together... e.g.
# Node.select("Character", "Action")["AWN", "CEP", "LOVING"](fancy=True)
# # within parens/prackets = OR relationship, separate quotes/brackets = AND relationship

# # sorting
# Language.select("Character").sort_by("name")

# # related - for nodes
# Character.select["AWN", "CEP"].related_to # all nodes related to either AWN or CEP, where AWN or CEP is the source of the relationship
# Character.select["AWN", "CEP"].related_from # all nodes related to either AWN or CEP, where AWN or CEP is the target of the relationship

# Expression.select["AWN", "CEP"].relationships_to # all relationships where AWN or CEP is source
# Character.select["AWN", "CEP"].relationships_from # all relationships where AWN or CEP is the target

# # related - for relationships
# Subject.select(fancy=True).targets # targets (i.e. characters acting as subject) for all fancy subjects
# Subject.select(fancy=True).sources # sources (i.e. expressions with a subject) for all fancy Subject relationships
