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