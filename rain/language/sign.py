import rain


class Sign(rain.Node): 
    pass


class Character(Sign): 
    pass


class Action(Sign): 
    pass


class Express(rain.Relationship):
    pass


class Doing(Express):
    pass


class Agent(Express):
    pass


class DoingTo(Express):
    pass


class Toward(Express):
    pass


class Expression(Sign):

    # represented by Express relationships that point to other Sign nodes
    # these are JUST propoerties ... 
    doing: Sign = None 
    agent: Sign = None
    doing_to: Sign = None 
    toward: Sign = None
    # situation: Sign = None # MAYBE: think topical particle in Japanese
    # ... to consider, can an expression reference multiple of these? (could be interesting)

    material: rain.Select = None
