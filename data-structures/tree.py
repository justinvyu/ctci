
class Tree:
    def __init__(self, label, branches=None):
        self.label = label
        self.branches = branches
        if not branches:
            self.branches = []

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.is_leaf():
            return "Tree({0})".format(self.label)
        else:
            return "Tree({0}, {1})".format(self.label, repr(self.branches))

    def __str__(self):
        return "\n".join(self.indent())

    def indent(self, indentation=0):
        if self.label is None:
            return ""
        indented = ["  " * indentation + str(self.label)]
        for b in self.branches:
            indented.extend(b.indent(indentation + 1))
        return indented

class BinaryTree(Tree):
    empty = Tree(None)

    def __init__(self, label, left=empty, right=empty):
        Tree.__init__(self, label, [left, right])

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return self.branches == [BinaryTree.empty] * 2

