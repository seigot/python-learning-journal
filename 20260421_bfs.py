class GraphAdjList:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination):
        if source not in self.graph:
            self.graph[source] = set()
        if destination not in self.graph:
            self.graph[destination] = set()

        if destination in self.graph[source] and source != destination:
            print("No non-simple graphs")
            return
        else:
            self.graph[source].add(destination)
            self.graph[destination].add(source)

    def bfs(self, start_vertex):
        from collections import deque
        if start_vertex not in self.graph:
            return []
        visited = set()
        dq = deque()
        dq.append(start_vertex)
        visited.add(start_vertex)
        result = []

        while dq:
            cx = dq.popleft()
            result.append(cx)
            for nx in self.graph[cx]:
                if nx not in visited:
                    dq.append(nx)
                    visited.add(nx)
        return result

myGraph = GraphAdjList()
myGraph.add_edge(1,2)
myGraph.add_edge(2,3)
myGraph.add_edge(3,4)
myGraph.add_edge(4,5)
myGraph.add_edge(3,5)
print(myGraph.bfs(1))
print(myGraph.bfs(5))
print(myGraph.bfs(3))
print(myGraph.bfs(0))

class GraphAdjMatrix:
    def __init__(self, arrayVert):
        self.vertex = {}
        self.matrix = []

        if arrayVert is not None:
            for vertex in arrayVert:
                self.add_vertex(vertex)