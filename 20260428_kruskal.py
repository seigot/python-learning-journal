class GraphAdjList:
    def __init__(self):
        self.graph = {}
        self.edges = []

    def add_edge(self, source, destination, weight):
        if source not in self.graph:
            self.graph[source] = set()
        if destination not in self.graph:
            self.graph[destination] = set()

        if destination in self.graph[source] and source != destination:
            return
        else:
            self.graph[source].add(destination)
            self.graph[destination].add(source)
            self.edges.append((source, destination, weight))

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

    def setCompress(self, ourSets, vert):
        if ourSets[vert] != vert:
            ourSets[vert] = self.setCompress(ourSets, ourSets[vert])
        return ourSets[vert]

    def kruskal(self):
        # sort edges by weight
        self.edges.sort(key=lambda e: e[2])

        # set each vertex in its own disjoint set
        ourSets = {}
        for vert in self.graph:
            ourSets[vert] = vert

        mst = []

        # Loop through all edges
        for edge in self.edges:
            srcRoot = self.setCompress(ourSets, edge.src)
            desRoot = self.setCompress(ourSets, edge.des)

            # if they are not in the same set, add edge to MST
            if srcRoot != desRoot:
                mst.append(edge)

                # union the two sets together
                ourSets[desRoot] = srcRoot

        return mst

    def show_edge(self):
        print(self.edges)

myGraph = GraphAdjList()
myGraph.add_edge(1,2,1)
myGraph.add_edge(2,3,2)
myGraph.add_edge(3,4,3)
myGraph.add_edge(4,5,4)
myGraph.add_edge(3,5,5)
#print(myGraph.bfs(1))
myGraph.show_edge()
mst = myGraph.kruskal()
mst.show_edge()
