class Selectable():

    def related_to(self): pass

    def related_from(self): pass

    def relationships_to(self): pass

    def relationships_from(self): pass

    @classmethod
    def select(cls): pass

class Select(Selectable):

    def __init__(self): pass

    def __getitem__(self, k): pass

    def __call__(self, *args, **kwargs): pass


Character.select("AWN", "CEP").relationships_from("Subject").sources("Expression")
Expression.select("AWN")

# get any set of data by:

# - label(s)
Language.select("Character", "Action") # (all characters and actions)
Character.select # (another way to express all characters)

# - key(s)
Language.select["AWN", "CEP", "LOVING"] # any type of data with keys, AWN, CEP, or LOVING

# - property value(s)
Language.select(fancy=True) # any type of data with "fancy" property having value of True

# can chain together... e.g.
Node.select("Character", "Action")["AWN", "CEP", "LOVING"](fancy=True)
# within parens/prackets = OR relationship, separate quotes/brackets = AND relationship

# sorting
Language.select("Character").sort_by("name")

# related - for nodes
Character.select["AWN", "CEP"].related_to # all nodes related to either AWN or CEP, where AWN or CEP is the source of the relationship
Character.select["AWN", "CEP"].related_from # all nodes related to either AWN or CEP, where AWN or CEP is the target of the relationship

Expression.select["AWN", "CEP"].relationships_to # all relationships where AWN or CEP is source
Character.select["AWN", "CEP"].relationships_from # all relationships where AWN or CEP is the target

# related - for relationships
Subject.select(fancy=True).targets # targets (i.e. characters acting as subject) for all fancy subjects
Subject.select(fancy=True).sources # sources (i.e. expressions with a subject) for all fancy Subject relationships
