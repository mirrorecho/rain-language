import re
import uuid

def auto_key():
    return uuid.uuid4().hex

def to_snake_case(s):
    return re.sub("([A-Z])", "_\\1", s).lower().lstrip("_")

def to_upper_snake_case(s):
    return re.sub("([A-Z])", "_\\1", s).upper().lstrip("_")

# ---------------------------------------------------------------

# music cell utils:

def transpose(pitches, value:int=0):
    try:
        return [transpose(p, value) for p in pitches]  
    except:
        return pitches + value