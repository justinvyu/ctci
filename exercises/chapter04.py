
# Trees and Graphs

import sys
sys.path.insert(0, "../data-structures/")
from graph import Graph
from queue import Queue

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
    """

