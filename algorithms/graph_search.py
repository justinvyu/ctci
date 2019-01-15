
import sys
sys.path.insert(0, '../data-structures/')
from graph import Graph
from queue import Queue

def DFS(graph, root):
    """
    Implementation of depth-first search for a graph.
    Exhaustively searches each branch of a node's neighbor before moving
    onto searching the next neighbor.
    """
    print(root)
    graph.visit(root)
    for n in graph.get_adjacent_nodes(root):
        if not graph.has_visited(n):
            DFS(graph, n)

def BFS(graph, root):
    """
    Implementation of breadth-first search for a graph.
    Searches all neighbors before searching the neighbors' neighbors.
    """
    q = Queue()
    graph.visit(root)
    q.enqueue(root)
    while not q.is_empty():
        r = q.dequeue()
        graph.visit(r)
        print(r)
        for node in graph.get_adjacent_nodes(r):
            if not graph.has_visited(node):
                q.enqueue(node)
                graph.visit(node)
