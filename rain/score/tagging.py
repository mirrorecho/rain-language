import abjad

articulations_inventory = set((".", "-", ">",".","^"))

dynamics_inventory = set(("ppp","pp","p","mp","mf","f","ff","fff","sfz","sffz", "sfp", "sf", "rfz"))

hairpins_inventory = set( (r"\<", r"\>") )

clefs_inventory = set( ("treble", "alto", "bass", "treble^8", "bass_8", "soprano", "tenor", "bass^15", "percussion") )

# TODO MAYBE: add more bar lines?
bar_lines_inventory = set( ("|", "||", ".|", "..", "|.|", "|.", ";", "!", ":|.", ".|:", ) )

stem_tremolos_inventory = set( (":8",":16",":32") )

tremolos_inventory = set( ("tremolo:1", "tremolo:2", "tremolo:3",) )

colors_inventory = set(("red",         "green",
            "blue",        "cyan",           "magenta",     "yellow",
            "grey",        "darkred",        "darkgreen",   "darkblue",
            "darkcyan",    "darkmagenta",    "darkyellow",))

fermatas_inventory = set( 
    ("fermata", "shortfermata", "longfermata", "verylongfermata",)  
    )

end_leaf_inventory = set( (")", "))", "8va!", "~", "pedal!", "trill!") )

# TODO MAYBE: deal with the set of tags that are NOT allowed

def get_attachment(tag_name:str):

    # TODO: won't work for noteheads that are tied
    def set_note_head(leaf, index, style):
        # abjad.override(leaf).style = style
        # abjad.override(leaf).NoteHead.style = "#'" + style

        if isinstance(leaf, abjad.Chord):
            abjad.tweak(leaf.note_heads[index]).style = "#'" + style
        elif isinstance(leaf, abjad.Note):
            abjad.tweak(leaf.note_head).style ="#'" + style

    direction = None
    if len(tag_name)>1:
        if tag_name[0] == "_":
            direction = abjad.Down
            tag_name = tag_name[1:]
        elif tag_name[0] == "^":
            direction = abjad.Up
            tag_name = tag_name[1:]

    if tag_name in articulations_inventory:
        return abjad.Articulation(name=tag_name, direction=direction)
    elif tag_name in dynamics_inventory:
        return abjad.Dynamic(name=tag_name, direction=direction)
    elif tag_name == "(":
        return abjad.StartSlur(direction=direction)
    elif tag_name == "((":
        return abjad.StartPhrasingSlur(direction=direction)
    elif tag_name == ")":
        return abjad.StopSlur()
    elif tag_name == "))":
        return abjad.StopPhrasingSlur()
    elif tag_name in hairpins_inventory:
        return abjad.StartHairpin(tag_name[1], direction=direction)
    elif tag_name == r"\!":
        return abjad.StopHairpin()
    elif tag_name == "[":
        return abjad.StartBeam(direction=direction)
    elif tag_name == "]":
        return abjad.StopBeam()
    elif tag_name in fermatas_inventory:
        return abjad.Fermata(command=tag_name)
    elif tag_name in stem_tremolos_inventory:
        tremolo_flags = int(tag_name[1:])
        return abjad.StemTremolo(tremolo_flags)
    elif tag_name in tremolos_inventory:
        tremolo_count = int(tag_name[8:])
        print("WARNING: tremolos not implemented")
        # return abjad.Tremolo(beam_count=tremolo_count, is_slurred=True)
    elif tag_name == "~":
        return abjad.Tie(direction=direction)
    elif tag_name == "8va":
        return abjad.Ottava(n=1)
    elif tag_name == "8vb":
        return abjad.Ottava(n=-1)
    elif tag_name == "8va!" or tag_name == "8vb!":
        return abjad.Ottava(n=0, format_slot="after")
    elif tag_name == "pedal":
        return abjad.StartPianoPedal()
    elif tag_name == "pedal!":
        return abjad.StopPianoPedal()
    elif tag_name == "trill":
        return abjad.StartTrillSpan()
    elif tag_name == "trill!":
        return abjad.StopTrillSpan()
    elif tag_name == "{":
        print("WARNING: horizontal bracket not implemented")
        # return abjad.HorizontalBracket() # TO DO - CONSIDER... add markup?
        abjad.Start
    elif tag_name in bar_lines_inventory:
        return abjad.BarLine(tag_name)
    elif tag_name in clefs_inventory:
        return abjad.Clef(tag_name)
    elif tag_name.startswith("tempo:"):
        tempo_indicators = tag_name.split(":")[1:]
        tempo_units_per_minute, tempo_duration_num, tempo_duration_den = tempo_indicators[:3]
        tempo_text = tempo_indicators[3] if len(tempo_indicators)==4 else None
        if tempo_units_per_minute:
            tempo_reference_duration = (int(tempo_duration_num),int(tempo_duration_den))
        else:
            tempo_reference_duration = None
        return abjad.MetronomeMark(tempo_reference_duration, units_per_minute=int(tempo_units_per_minute), textual_indication=tempo_text)
    elif tag_name.startswith("tempo_text:"):
        return abjad.MetronomeMark(textual_indication=tag_name[11:])
    elif tag_name in colors_inventory:
        return lambda x : abjad.label(x).color_leaves(tag_name)
    elif tag_name in colors_inventory:
        return lambda x : abjad.label(x).color_leaves(tag_name)
    elif tag_name.startswith("note_head:"):
        my_data = tag_name.split(":")
        return lambda x: set_note_head(x, int(my_data[1]), my_data[2])
    elif tag_name[0] == "\\":
        return abjad.LilyPondLiteral(tag_name, "before")
    elif tag_name[:2] == "!\\":
        return abjad.LilyPondLiteral(tag_name[1:], "after")
    elif tag_name[:14] == "markup_column:":
        return list(reversed([abjad.Markup(m, direction=abjad.Up) for m in tag_name[14:].split("|")]))
    else:
        return abjad.Markup(tag_name, direction=direction or abjad.Up)


# TODO: CONSIDER RE-IMPLEMENTING PIECES FROM BELOW AS NEEDED
# IN THE NEW CONTEXT OF RAIN PATTERN CUES AND COMBOS

# TO DO... only if needed
# def get_attachments(self, **kwargs):
#     return [AttachmentSetData.get_attachment(a) for a in self._tags]

# def set_tag(self, my_set, *args):
#     for arg in args:
#         if arg[:5] == "attr:":
#             my_set.add(str(getattr(self, arg[5:])))
#         else:
#             # overwrite existing dynamics, hairpins, clefs
#             # bars, and fermatas:
#             if arg in self.dynamics_inventory:
#                 my_set -= self.dynamics_inventory
#             elif arg in self.clefs_inventory:
#                 my_set -= self.clefs_inventory
#             elif arg in self.bar_lines_inventory:
#                 my_set -= self.bar_lines_inventory
#             elif arg in self.hairpins_inventory:
#                 my_set -= self.hairpins_inventory
#             elif arg in self.fermatas_inventory:
#                 my_set -= self.fermatas_inventory
#             my_set.add(arg)        

# def tag(self, *args):
#     self.set_tag(self._tags, *args)

# @property
# def tags(self):
#     # TO DO: this is a little wonky
#     my_tags = self._tags or set()
#     return set(my_tags)

# @tags.setter
# def tags(self, iterable):
#     self._tags = set()
#     self.tag(*iterable)


# def untag(self, *args):
#     for arg in args:
#         if arg in self._tags:
#             self._tags.remove(arg)
#     return self

# TO CONSIDER: are these children methods even worth it?
# def tag_children(self, *args):
#     for child in self.children:
#         child.tag(*args)

# def untag_children(self, *args):
#     for child in self.children:
#         child.untag(*args)
#     return self

def combine_tags(self, new_set, old_set):
    # note, can't do simple union since that could dupe dynamics or hairpins, so need to call set_tag method on each one
    # .... here, new_set values override old_set values for hairpins and dynamics
    combined_set = set(old_set) # makes a copy
    for n in new_set:
        self.set_tag(combined_set, n)
    return combined_set

# @property
# def use_ancestor_attachments(self): 
#     """
#     in general, the first item uses parent attachments (e.g. if event is first item in a segment, and a segment
#     is tagged with "mf", then event is event is also "mf"... but not if event is second item in the segment)
#     ...overriden in LogicalTie so that the first NONREST item uses ancestor attachments (instead of first item)
#     """
#     return self.my_index == 0 

# def get_ancestor_tags(self):
#     # print("YOYO", type(self), type(self.parent))
#     if self.parent and isinstance(self.parent, calliope.Machine) and self.use_ancestor_attachments:
#         parent_tags = getattr(self.parent, "tags", set())
#         parent_ancestor_tags = self.parent.get_ancestor_tags()
#         return self.combine_tags(parent_tags, parent_ancestor_tags)
#     return set()

# def get_all_tags(self):
#     return self.combine_tags(self._tags, self.get_ancestor_tags())

# TO DO... consider implementing this
# # TO DO.. this should be able to work with original_depthwise_index (or fragments should not reset segments)
# def span_children(self, spanner):
#     # TO DO... something more elegant to associate spanners with end spanners
#     if spanner == "(":
#         end_spanner = ")"
#     if spanner == "((":
#         end_spanner = "))"
#     if spanner == "\<" or spanner == "\>":
#         end_spanner = "\!"
#     self.children[0]

# TO DO... remove in favor of always using Transform objects?
# @classmethod
# def span_every(cls, spanner, items, every_count=2):
#     # TO DO... something more elegant to associate spanners with end spanners
#     if spanner == "(":
#         end_spanner = ")"
#     if spanner == "((":
#         end_spanner = "))"
#     if spanner == r"\<" or spanner == r"\>":
#         end_spanner = r"\!"
    
#     for i in range(0, len(items), every_count):
#         items[i].tag(spanner)
#         if len(items) > i+every_count-1:
#             items[i+every_count-1].tag(end_spanner)

# TO DO.. only if needed:
# def get_all_attachments(self):
#     """
#     Funny and slightly confusing method... 
#     """
#     return [self.get_attachment(a) for a in self.get_all_names()]

# TO DO... implement only if needed
# def get_descendant_names(self):
#     if self.children:
#         return self.children[0]._tags | self.get_descendant_names()
#     else:
#         return set()

# def get_consolidated_names(self):
#     return self._tags | self.get_ancestor_names() | self.get_descendant_names()

# def get_consolidated_attachments(self):
#     """
#     Funny and slightly confusing method... 
#     """
#     return [AttachmentSetData.get_attachment(a) for a in self.get_consolidated_names()]