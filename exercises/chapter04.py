
# Trees and Graphs

from graph import Graph
from queue import Queue
from tree import BinaryTree
from linkedlist import Node

# 4.1 Route Between Nodes

def route_between_nodes(edges, a, b):
    """
    Returns true if there is a path in a directed graph linking from node a to node b.
    >>> a, b = 'a', 'b'
    >>> edges = [('a', 'c'), ('a', 'f'), ('c', 'd'), ('c', 'e'), ('e', 'b'), ('e', 'd'), ('f', 'g')]
    >>> route_between_nodes(edges, a, b)
    True
    >>> edges = [('a', 'c'), ('c', 'd'), ('a', 'd'), ('b', 'e'), ('e', 'd')]
    >>> route_between_nodes(edges, a, b)
    False
    """
    # Build graph data structure
    graph = {} # Map key (node name) -> value (set of neighboring nodes)
    for node1, node2 in edges:
        if node1 not in graph:
            graph[node1] = set()
        graph[node1].add(node2)

    visited = set()
    queue = [a]
    while queue:
        curr = queue.pop(0)
        visited.add(curr)
        if curr == b: # We've found it!
            return True
        if curr not in graph:
            continue
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

# 4.2 Minimal Tree

def minimal_tree(lst):
    """
    Returns a binary search tree with minimal height containing the numbers
    passed in as a sorted array of unique integers.
    >>> lst = [1, 2, 3, 4, 5, 6, 7]
    >>> print(minimal_tree(lst))
    4
      2
        1
        3
      6
        5
        7
    """
    if len(lst) == 1:
        return BinaryTree(lst[0])
    elif not lst:
        return BinaryTree.empty
    else:
        mid = len(lst) // 2
        left = minimal_tree(lst[:mid])
        right = minimal_tree(lst[mid+1:])
        return BinaryTree(lst[mid], left, right)

# 4.3 List of Depths

def list_of_depths(tree):
    """
    Returns a list of D linked lists with the elements of each level in the
    binary tree, where D is the total number of levels/the depth.
    >>> list_of_depths(minimal_tree(list(range(1, 8))))
    [Node(4), Node(6, Node(2)), Node(7, Node(5, Node(3, Node(1))))]
    """
    depths = {}
    def add_node_at_depth(t, depth=0):
        if t is BinaryTree.empty:
            return
        if depth not in depths:
            depths[depth] = Node.empty
        depths[depth] = Node(t.label, depths[depth])
        add_node_at_depth(t.left, depth + 1)
        add_node_at_depth(t.right, depth + 1)
    add_node_at_depth(tree)
    return list(depths.values())
