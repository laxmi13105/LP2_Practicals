from collections import deque

class Graph:

    def __init__(self):
        self.graph = {}

    # Add edge for undirected graph
    def add_edge(self, u, v):

        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    # BFS Traversal
    def bfs(self, start):

        visited = set()

        queue = deque()

        visited.add(start)
        queue.append(start)

        while queue:

            vertex = queue.popleft()

            print(vertex, end=" ")

            for neighbour in self.graph[vertex]:

                if neighbour not in visited:

                    visited.add(neighbour)
                    queue.append(neighbour)


# Create graph
g = Graph()

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("Breadth First Search Traversal:")

g.bfs(0)