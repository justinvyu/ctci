from node import Node

class LinkedList:
    def __init__(self, root):
        assert isinstance(root, Node)
        self.root = root

    def __len__(self):
        end = self.root
        length = 0
        while end:
            end = end.rest
            length += 1
        return length

    def append(self, node):
        end = self.root
        while end.rest:
            end = end.rest
        end.rest = node

    def remove(self, i):
        assert i >= 0 and i < len(self)
        if i == 0:
            self.root = self.root.rest
        else:
            curr, prev = self.root, Node.empty
            while i > 0:
                prev = curr
                curr = curr.rest
                i -= 1
            prev.rest = curr.rest

