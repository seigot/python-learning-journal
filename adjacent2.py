class GraphAdjMatrix:
    def __init__(self, arrayVert):
        # construct graph, end result, a whole bunch of unconnected vertices
        self.arrayVert = arrayVert

    def add_vertex(self, vert):
        current = len(self.arrayVert)
        if vert < current:
            return
        # update
        offset = vert - current + 1
        size = current + offset
        # add columm
        for row in self.arrayVert:
            row.extend([0] * offset)
        # add row
        for _ in range(offset):
            self.arrayVert.append([0] * size)

    def add_edge(self, source, dest):
        if source >= len(arrayVert[0]) and dest >= len(arrayVert[0]):
            print("out of range")
            return
        self.arrayVert[source][dest] = 1
        self.arrayVert[dest][source] = 1

    def print_edge(self):
        for ii in range(len(self.arrayVert)):
            print(self.arrayVert[ii])
N = 10
arrayVert = [[0]*N for _ in range(N)]
g = GraphAdjMatrix(arrayVert)
g.add_edge(0,1)
g.add_edge(10,11)
g.print_edge()
print("--")
g.add_vertex(10)
g.add_vertex(11)
g.add_edge(10,11)
g.print_edge()

