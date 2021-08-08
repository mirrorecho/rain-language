from dataclasses import dataclass, field

import rain

# --------------------------------------------------------------------

@dataclass
class Instrument(rain.Machine): 
    short_name = ""

    def trigger(self, **kwargs):
        print(self.key, kwargs)
        