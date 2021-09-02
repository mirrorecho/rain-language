from dataclasses import dataclass
from typing import Any, Iterable

import rain


# --------------------------------------------------------------------
@dataclass
class TreePattern(rain.Pattern): 

    def __post_init__(self):
        super().__post_init__()
        self._cached_branches = None

    @property
    def is_leaf(self):
        return False

    # TODO maybe: is this COOL?
    @property
    def branches(self) -> Iterable[rain.Pattern]:
        if self._cached_branches is None:
            self._cached_branches = list(self.get_branches())
        return self._cached_branches

    #TODO same method as on Alters ... DRY!
    def set_hooks(self, branch: rain.Pattern):
        if self.leaf_hooks:
            if not branch.leaf_hooks:
                branch.leaf_hooks = []
            branch.leaf_hooks.extend(self.leaf_hooks)
        if self.vein_hooks:
            if not branch.vein_hooks:
                branch.vein_hooks = []
            branch.vein_hooks.extend(self.vein_hooks)
        return branch


    # TO CONSIDER: this is all perfectly fine for a local graph, but would
    # generate lots of queries to a graph DB ... how to optimize?   
    # ALSO TO CONSIDER... would be MUCH COOLER! if this returned a Select
    def get_branches(self):
        if child_cue := self.r("->", "CUE_FIRST").n().first:
            yield self.set_hooks(child_cue.cues_pattern)
            while child_cue := child_cue.r("->", "CUE_NEXT").n().first:
                yield self.set_hooks(child_cue.cues_pattern)

    # DITTO... would be much cooler as a Select
    @property
    def leaves(self) -> Iterable[rain.Pattern]:
        for branch in self.branches:
            yield from branch.leaves

    # DITTO... 
    @property
    def nodes(self) -> Iterable[rain.Pattern]:
        yield self
        for branch in self.branches:
            yield from branch.nodes

    @property
    def veins(self) -> Iterable[Any]:
        for leaf in self.leaves:
            yield from leaf.veins


    def extend_by_key(self, *keys):
        self.extend(*[rain.context.new_by_key(k) for k in keys])
        return self

    def extend(self, *patterns):
        cue_p_first = rain.Cue.create()
        rain.Cues.create(source=cue_p_first, target=patterns[0])

        if not self.r("->", "CUE_FIRST").first:
            rain.CueFirst.create(source=self, target=cue_p_first)

        elif cue_last := self.r("->", "CUE_LAST").first:
            cue_last.read()
            rain.CueNext.create(source=cue_last.target, target=cue_p_first)
            cue_last.delete()

        # FIRST, create all the cues, then iterate over them, pairwise
        cue_nodes = [cue_p_first] + [rain.Cue.create() for p in patterns[1:]]

        for p, c, c_next in zip(patterns, cue_nodes, cue_nodes[1:]+[None]):
         
            rain.Contains.create(source=self, target=c)
            rain.Cues.create(source=c, target=p)

            if c_next:
                rain.CueNext.create(source=c, target=c_next)
            else:
                rain.CueLast.create(source=self, target=c)
        return self

    def append(self, pattern):
        return self.extend(pattern)

    def insert(self, index, pattern):
        raise NotImplementedError()

# --------------------------------------------------------------------
@dataclass
class CellTree(TreePattern): 

    def trigger_hook(self, start_dur=0, **kwargs):
        return kwargs

    # @property
    # def branches(self) -> Iterable[Pattern]:
    #     for branch in super().branches:
    #         yield branch

# --------------------------------------------------------------------
@dataclass
class Sequence(CellTree): 
    
    @property
    def simultaneous(self) -> bool:
        return False

# --------------------------------------------------------------------
@dataclass
class Parallel(CellTree): 
    @property
    def simultaneous(self) -> bool:
        return True

# --------------------------------------------------------------------
@dataclass
class Combo(CellTree): pass

# --------------------------------------------------------------------

@dataclass
class MachineTree(TreePattern): pass
