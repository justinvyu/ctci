import sys
sys.path.insert(0, '../data-structures/')
from linkedlist import LinkedList, Node

# 2.1 Remove Dups

def remove_dups(lst):
    """
    Removes duplicate values from an unsorted linked list.
    >>> a = Node(1, Node(4, Node(5, Node(2, Node(4, Node(1))))))
    >>> remove_dups(a)
    >>> a
    Node(1, Node(4, Node(5, Node(2))))
    """
    curr, prev = lst, lst
    vals = set()
    while curr:
        if curr.data in vals:
            prev.rest = curr.rest
            curr = curr.rest
        else:
            vals.add(curr.data)
            prev = curr
            curr = curr.rest

# 2.2 Return Kth to Last

def get_kth_to_last(lst, k):
    """
    Returns the kth to last element of a singly linked list.
    >>> a = Node(0, Node(1, Node(2, Node(3, Node(4, Node(5))))))
    >>> get_kth_to_last(a, 3)
    3
    """
    length = 0
    end = lst
    while end:
        end = end.rest
        length += 1
    i = length - k
    end = lst
    while i > 0:
        end = end.rest
        i -= 1
    return end.data

# 2.3 Delete Middle Node

def delete_middle_node(node):
    """
    Deletes a 'middle' node given only that node. The node passed in will not be the
    first or last: node.rest must not be empty.
    >>> to_delete = Node(4, Node(5, Node(6)))
    >>> lst = Node(1, Node(2, to_delete))
    >>> delete_middle_node(to_delete)
    >>> lst
    Node(1, Node(2, Node(5, Node(6))))
    """
    node.data = node.rest.data
    node.rest = node.rest.rest

# 2.4 Partition

def partition(lst, threshold):
    """
    Returns a partitioned linked list where all values below the threshold come
    before the vlaues greater than or equal to the threshold.
    >>> lst = Node(3, Node(5, Node(8, Node(5, Node(10, Node(2, Node(1)))))))
    >>> partition(lst, 5)
    Node(1, Node(2, Node(3, Node(10, Node(5, Node(8, Node(5)))))))
    """
    left = Node.empty
    right = Node.empty
    end = left
    while lst:
        if lst.data >= threshold:
            right = Node(lst.data, right)
        else:
            left = Node(lst.data, left)
            if not end:
                end = left
        lst = lst.rest
    end.rest = right
    return left

