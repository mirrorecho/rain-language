# --------------------------------------------------------------------



        # for p in pattern_keys:
        #     print(p)
        #     for vein in self._triggers[p]:
        #         print(vein)

        # for v_dict in self._pattern.veins:

        #     if machine_name := v_dict.pop("machine"):
        #         dur = v_dict[dur]
        #         self.palette[machine_name].trigger(self.total_dur, **v_dict)

    # def __init__(self, blueprints:Palette = None):
    #     self._blueprints = blueprints or Palette()

    # @property
    # def blueprints(self) -> Palette:
    #     return self._blueprints

    # def play(pattern_node:"Pattern", realtime=False):

    #     for e in pattern_node:
    #         e.

# --------------------------------------------------------------------

# # TO DO: is an event even needed? should the PatternReader just call the
# # machine's trigger method with arguments?
# class Event(object):
#     dur: float = 0
#     machine: str = "" # TO CONSIDER... maybe this is actually an instance of machine

#     def __str__(self):
#         return


# print("========================================================")

# # print(rain.context._language_type_registry)

# c1 = NotatedMusicCell.create(
#     key="C1",
#     pitch=(0,2,5,4),
#     dur=cycle((1,2,)),
#     machine=cycle(("VIOLA",)),
#     tags = cycle((None,)),
# )
# c2 = NotatedMusicCell.create(
#     key="C2",
#     pitch=(7,0,9,0),
#     dur=(2,2,3,3),
#     machine=cycle(("VIOLIN1", "VIOLIN2"),),
#     tags = cycle((None,)),
# )

# c_pattern = TreePattern.create().extend(c1, c2, c1)

# mp = Palette()
# mp.extend(Machine())


# for d in pa:
#     # d.read()
#     print(d)

# violin1 = Staff.create("VIOLIN1", "Violin 1")
# violin2 = Staff.create("VIOLIN2", "Violin 2")
# viola = Staff.create("VIOLA", "Viola")
# cello = Staff.create("CELLO", "Cello")

# violins = StaffGroup().create("VIOLINS").extend(
#     violin1,
#     violin2,
# )

# quartet_score = Score().create("STRING_QUARTET").extend(
#     violins,
#     viola,
#     cello,
# )

# print(quartet_score)
# for x in quartet_score.nodes:
#     print(x)

# pr = PatternReader(quartet_score.get_palette())
# pr.read(c_pattern)


# --------------------------------------------------------------------

# class Machine(rain.LanguageBase):
#     def __init__(self, 
#         # blueprint:Blueprint, 
#         alias:str, **kwargs
#         ):
        
#         # self._blueprint = blueprint
#         self.properties = kwargs
#         self.alias = alias

#     # @property
#     # def blueprint(self) -> Blueprint: 
#     #     return self.blueprint

#     def trigger(self, event: "Event"): 
#         self._blueprint.trigger(self, event)
