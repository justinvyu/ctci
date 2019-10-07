from collections import defaultdict

class Graph:
    NOT_FOUND_ERROR = 'Error: node not in the graph'
    def __init__(self, connections, directed=True):
        self.nodes = {}
        self._graph = defaultdict(set)
        self.directed = directed
        self.add_edges(connections)

    def add_edges(self, edges):
        for a, b in edges:
            if a not in self.nodes:
                self.nodes[a] = GraphNode(a)
            if b not in self.nodes:
                self.nodes[b] = GraphNode(b)
            self._graph[a].add(b)
            # If undirected, the graph add an edge in both directions
            if not self.directed:
                self._graph[b].add(a)

    def has_visited(self, node):
        assert node in self.nodes, Graph.NOT_FOUND_ERROR
        return self.nodes[node].visited

    def visit(self, node):
        assert node in self.nodes, Graph.NOT_FOUND_ERROR
        self.nodes[node].visited = True

    def get_adjacent_nodes(self, node):
        assert node in self.nodes, Graph.NOT_FOUND_ERROR
        return self._graph[node]

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.visited = False
