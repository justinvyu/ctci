from node import Node

class Queue:
    def __init__(self):
        self.first = Node.empty
        self.last = Node.empty

    def enqueue(self, item):
        node = Node(item)
        if self.last:
            self.last.rest = node
        self.last = node # Update last node to the node just added
        if not self.first:
            self.first = self.last # First = last for the first item

    def dequeue(self):
        assert not self.is_empty(), "Error: queue is empty"
        data = self.first.data
        self.first = self.first.rest
        if not self.first:
            self.last = Node.empty
        return data

    def peek(self):
        assert not self.is_empty(), "Error: queue is empty"
        return self.first.data

    def is_empty(self):
        return not self.first
