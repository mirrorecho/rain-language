import rain

# TO CONSIDER: should this be a node in the graph after all?
# (with relationships to all the nodes the pallete contains)
# ... assume no, but think about it
# ... could also create PaletteNode for specific uses
class Palette(rain.LanguageBase):
    """
    a wrapper around a dictionary of nodes
    """

    def __init__(self, *nodes):
        """
        a cool thing here is that it's easy to create a palette from a selection
        """
        self._nodes = {}
        self.extend(*nodes)

    def items(self):
        return self._nodes.items()

    def add(self, node:rain.Node):
        self._nodes[node.key] = node

    def extend(self, *nodes):
        for n in nodes:
            self.add(n)

    def add_key(self, key:str):
        self._node[key] = None

    def extend_keys(self, *keys):
        for k in keys:
            self.add_key(k)

    def __getitem__(self, key) -> rain.Node:
        if (my_node := self._nodes[key]) is None:
            my_node = self.context.new_by_key(key)
            self._nodes[key] = my_node
        return my_node