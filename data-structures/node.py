class Node:
    empty = ()

    def __init__(self, data, rest=empty):
        assert rest is Node.empty or isinstance(rest, Node)
        self.data = data
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest = ", " + repr(self.rest)
        else:
            rest = ""
        return "Node("+repr(self.data)+rest+")"

