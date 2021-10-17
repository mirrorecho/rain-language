from dataclasses import dataclass, field

import rain

# --------------------------------------------------------------------

class Instrument(rain.Machine): 
    short_name = ""

    def trigger(self, **kwargs):
        print(self.key, kwargs)
        