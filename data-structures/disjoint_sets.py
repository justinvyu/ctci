
class DisjointSet:
    def __init__(self, n):
        self.n = n
        self.parent = [-1 for _ in range(n)]

    def connect(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        # Connect lighter tree to heavier tree
        if self.parent[root_x] <= self.parent[root_y]:  # x heavier than y
            # Place y under x
            self.parent[root_x] += self.parent[root_y] # Add the number of new elements
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] += self.parent[root_x] # Add the number of new elements
            self.parent[root_x] = root_y

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    def find(self, x):
        if self.parent[x] < 0:
            return x
        return self.find(self.parent[x])
