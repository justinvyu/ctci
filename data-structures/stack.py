from node import Node

class Stack:
    """
    Stack FIFO data structure implementation
    >>> st = Stack()
    >>> st.push(1)
    >>> st.push(2)
    >>> st.push(3)
    >>> st.pop()
    3
    >>> st.pop()
    2
    >>> st.pop()
    1
    """

    def __init__(self):
        self.top = Node.empty

    def push(self, item):
        node = Node(item)
        node.rest = self.top
        self.top = node
    
    def pop(self):
        assert not self.is_empty, "Error: stack is empty"
        data = self.top.data
        self.top = self.top.rest
        return data

    def peek(self):
        assert not self.is_empty, "Error: stack is empty"
        return self.top.data

    @property
    def is_empty(self):
        return self.top == Node.empty
