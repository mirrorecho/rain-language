# TODO: dumb name!

import re
import uuid
import rain

def auto_key():
    return uuid.uuid4().hex

def to_snake_case(s):
    return re.sub("([A-Z])", "_\\1", s).lower().lstrip("_")

def to_upper_snake_case(s):
    return re.sub("([A-Z])", "_\\1", s).upper().lstrip("_")

def listify(*args):
    return_list = []
    for a in args:
        try:
            return_list.extend(a)
        except:
            return_list.append(a)
    return return_list

def pattern_set_branch_hooks(pattern:"rain.Pattern", branch:"rain.Pattern", cue:"rain.Cue"=None):
    # TODO MAYBE: consider this:
    # if self.node_hooks:
    #     if not branch.node_hooks:
    #         branch.node_hooks = []
    #     branch.node_hooks.extend(self.node_hooks)
    if pattern.leaf_hooks:
        if not branch.leaf_hooks:
            branch.leaf_hooks = []
        branch.leaf_hooks.extend(pattern.leaf_hooks)
    if pattern.vein_hooks:
        if not branch.vein_hooks:
            branch.vein_hooks = []
        branch.vein_hooks.extend(pattern.vein_hooks)
    if not branch._parentage:
        branch._parentage = []
    
    #TODO MAYBE: this implementation isn't terribly elegant
    
    branch._parentage.append(pattern)
    branch._parentage.extend(pattern._parentage)
    # print("PARENTAGE:", [b.key for b in branch._parentage])
    for p in branch._parentage:
        if cue and isinstance(p, rain.Meddle) and cue == p.connected_alter_cue:
            print("ALTERING DESCENDANT!", branch.key, "FROM", p.key)
            # TODO: only a single alteration is handled with this implementation
            # ... would be ideal to be able to chain Meddle alterations together
            pattern_set_branch_hooks(p.connected_alter, branch, None)
    return branch

# ---------------------------------------------------------------

# music cell utils:

def transpose(pitches, value:int=0, octave:int=0):
    value = value + octave*12
    try:
        return [transpose(p, value) for p in pitches]  
    except:
        return pitches + value if pitches is not None else pitches


def rest(dur:int):
    return rain.RestCell.create(dur=(dur,))