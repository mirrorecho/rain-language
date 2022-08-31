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
    
    #TODO EVENTUALLY: this implementation isn't terribly elegant ... KISS
    
    branch._parentage.append(pattern)
    branch._parentage.extend(pattern._parentage)
    # print("PARENTAGE:", [b.key for b in branch._parentage])
    for p in branch._parentage:

        if cue and isinstance(p, rain.Meddle) and cue in p.connected_alters_cues:
            for connected_alter in p.connected_alters:
                my_meddle_chain = list(connected_alter.meddle_chain)
                if my_meddle_chain[-1].alters_cue == cue:
                    # print("ALTERING DESCENDANT!", branch.key, "FROM", p.key)
                    for meddle_alter in reversed(my_meddle_chain):
                        pattern_set_branch_hooks(meddle_alter, branch, None)
    return branch

# ---------------------------------------------------------------

# music cell utils:

def transpose(pitches, value:int=0, octave:int=0):
    value = value + octave*12
    try:
        return [transpose(p, value) for p in pitches]  
    except:
        return pitches + value if pitches is not None else pitches

def key_from_args(args_tuple:tuple):
    args = list(args_tuple)
    if isinstance(args[0], str):
        key = args.pop(0)
    else:
        key = None
    return key, args

def key_from_dict(properties_dict:dict):
    key = properties_dict.pop("key", None)
    return key, properties_dict

def rest(dur:int):
    return rain.RestCell.create(dur=(dur,))

def par(*args) -> "rain.Parallel":
    key, args = key_from_args(args)
    return rain.Parallel.create(key).extend(*args)

def seq(*args) -> "rain.Sequence":
    key, args = key_from_args(args)
    return rain.Sequence.create(key).extend(*args)

def par_ref(key:str) -> "rain.Parallel":
    return rain.Parallel(key)

def seq_ref(key:str) -> "rain.Sequence":
    return rain.Sequence(key)