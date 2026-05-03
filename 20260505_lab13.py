# Citation: https://chatgpt.com/share/69f6c1da-3fa0-83e8-898e-cda1e495f07e
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
        # The graph supports string identifiers for vertices because the adjacency list is stored using a dictionary. 
        # This allows vertices to be represented as either strings or integers.

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, source, destination):
        self.addVertex(source)
        self.addVertex(destination)
        self.graph[source].append(destination)  # Directed edge

    def bfs(self, start_vertex):
        # BFS explores vertices level by level using a queue and visits all nearby vertices first. 
        # It is useful for finding the shortest path in an unweighted graph.    
        if start_vertex not in self.graph:
            return []
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start_vertex):
        # DFS explores vertices by going deeper into one path first using a stack before backtracking. 
        # It is useful for exploring all reachable vertices but does not guarantee the shortest path.
        if start_vertex not in self.graph:
            return []

        visited = set()
        stack = [start_vertex]
        result = []

        while stack:
            current = stack.pop()

            if current not in visited:
                visited.add(current)
                result.append(current)

                # reverse is used to visit smaller-numbered vertices first
                for neighbor in reversed(self.graph[current]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    def bfs_to_find_the_shortest_path(self, start_vertex, end_vertex):
        # Error Check
        if start_vertex not in self.graph or end_vertex not in self.graph:
            return []

        # The function performs BFS by storing entire paths in the queue. 
        # It explores paths level by level and returns the first path that reaches the destination.
        # This guarantees the shortest path in terms of the number of edges.
        # [Future Work] As the number of edges increases, 
        # storing entire paths may require more memory. 
        # A parent-tracking method with path reconstruction would be more memory-efficient.
        visited = set()
        queue = deque([[start_vertex]])
        visited.add(start_vertex)

        while queue:
            path = queue.popleft()
            current = path[-1]

            if current == end_vertex:
                return path

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    queue.append(new_path)
        return []

edges = [
    (1, 2),         # 1
    (2, 3), (2, 6), # 2
    (3, 4), (3, 7), # 3
    (4, 5), (4, 8), # 4
    (5, 8), (5, 12), # 5
    (6, 10),         # 6
    (7, 6), (7, 11), # 7
    (8, 7), (8, 11), (8, 12), # 8
    (10, 9),         # 10
    (11, 10),        # 11
    (12, 11)         # 12
]

CityGraph = Graph()
for src, dst in edges:
   CityGraph.addEdge(src, dst)
start = 1
end = 9
# --- BFS/DFS Traversal.
print("BFS result (the order of landmarks visited):")
bfs_result = CityGraph.bfs(start)
print(" -> ".join(map(str, bfs_result)))
print("DFS result (the order of landmarks visited):")
dfs_result = CityGraph.dfs(start)
print(" -> ".join(map(str, dfs_result)))

# --- BFS to find the shortest path.
print("Shortest path using BFS:")
bfs_result = CityGraph.bfs_to_find_the_shortest_path(start, end)
print(" -> ".join(map(str, bfs_result)))
