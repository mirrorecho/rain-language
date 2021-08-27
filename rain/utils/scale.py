
def get_diatonic_root(
    pitches = (),
    mode_offset = 1, # 1 is major
    ):
    fifths_away = sorted([((pitch * 7) % 12) for pitch in set(pitches)])
    gaps = [(f - fifths_away[i-1]) % 12 for i,f in enumerate(fifths_away)]
    largest_gap_before = max(zip(fifths_away, gaps), key = lambda x:x[1])[0]
    return ((largest_gap_before * 7) + (7*mode_offset)) % 12


# TO DO: consider making this an abstract cyclic thingy
class Scale():
    """ 
    An abstract representation of a scale. Does not necessarily need
    to span a 12-semitone "octave".
    """

    root = 0 # default is middle C
    steps = (0,2,4,5,7,9,11,12) # must start on 0, default is diatonic
    print_kwargs = ("root", "steps")

    # TODO: add methods to swap between iterables of degrees and pitches


    @property
    def octave_size(self):
        """ Gets the size in semitones of the span of the "octave". """
        return self.steps[-1]

    @property
    def num_steps(self):
        return len(self.steps)-1

    def __init__(self, steps=None, pitches=None, root=None):
        if steps:
            self.steps = steps
        elif pitches:
            unrooted_steps = sorted(set(pitches)) # removes dupes and sorts
            self.root = unrooted_steps[0]
            self.steps = tuple([ p-self.root for p in  unrooted_steps])
        if root:
            self.root = root

    def __getitem__(self, arg):
        
        if isinstance(arg, int):
            my_octave_and_step = divmod(arg, self.num_steps)
            return (my_octave_and_step[0] * self.octave_size) + self.steps[my_octave_and_step[1]] + self.root
        elif arg is None:
            return None
        elif isinstance(arg, (list, tuple)): # TODO maybe ... duck typing instead?
            return [self[a] for a in arg]
        elif isinstance(arg, slice):
            return [self[i] for i in range(arg.start, arg.stop, arg.step or 1)]
        else:
            raise(TypeError("Scale indices must be integers, None slices, or tuples/lists"))

    def contains(self, arg):
        return (arg - self.root) % self.octave_size in self.steps

    def pitch_transpose_within(self, pitch, steps):
        return self[self.index(pitch)+steps]

    def pitch_change_scale(self, pitch, new_scale, steps=0):
        return new_scale[self.index(pitch)+steps]

    def mode(self, degrees, keep_root=True) -> "Scale":
        s = Scale(pitches=self[degrees:degrees+self.num_steps+1])
        if keep_root:
            s.root = self.root            
        return s

    def __add__(self, v) -> "Scale":
        return Scale(steps = self.steps, root=self.root+v)

    def index(self, pitch):
        """ Gets index for a pitch number. If pitch is not found in the scale,
        then rounds up."""
        
        rooted_pitch = pitch - self.root
        rooted_octave_and_pitch_class = divmod(rooted_pitch, self.octave_size)
        rooted_pitch_class_index = next(i for i, p in enumerate(self.steps) if p>=rooted_octave_and_pitch_class[1])

        return (rooted_octave_and_pitch_class[0] * self.num_steps) + rooted_pitch_class_index
