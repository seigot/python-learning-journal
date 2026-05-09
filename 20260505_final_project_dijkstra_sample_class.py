import heapq
from collections import defaultdict
from itertools import count

class TravelMapGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.distances = {}
        self.previous = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, a, b, cost):
        self.add_node(a)
        self.add_node(b)

        self.graph[a].append((b, cost))
        self.graph[b].append((a, cost))

    def add_edge_with_list(self, edges):
        for a, b, cost in edges:
            self.add_edge(a, b, cost)

    def dijkstra(self, start):
        self.distances = {node: float("inf") for node in self.graph}
        self.previous = {node: None for node in self.graph}

        self.distances[start] = 0

        counter = count()
        priority_queue = [(0, next(counter), start)]

        while priority_queue:
            current_cost, _, current_node = heapq.heappop(priority_queue)

            if current_cost > self.distances[current_node]:
                continue

            for neighbor, edge_cost in self.graph[current_node]:
                new_cost = current_cost + edge_cost

                if new_cost < self.distances[neighbor]:
                    self.distances[neighbor] = new_cost
                    self.previous[neighbor] = current_node
                    heapq.heappush(
                        priority_queue,
                        (new_cost, next(counter), neighbor)
                    )

    def get_path(self, destination):
        path = []
        current = destination

        while current is not None:
            path.append(current)
            current = self.previous[current]
        return path[::-1]

    def get_distance(self, destination):
        return self.distances[destination]

edges = [
    # Left side
    (12, 11, 6), (12, 13, 6), (12, 15, 25),
    (11, 16, 10),
    (13, 14, 18),    
    # Middle
    (16, 15, 5), (16, 17, 3),
    (15, 17, 5), (15, 14, 10), (15, 20, 10),
    (14, 21, 10),  
    
    (17, 18, 5), (17, 19, 5),
    (18, 19, 5), (18, 28, 10),
    (19, 20, 5), (19, 26, 5),
    (20, 21, 5), (20, 25, 5),

    # Right side
    (21, 22, 10),
    (22, 23, 5),
    (23, 24, 5),
    (24, 29, 5),
    (25, 24, 5),
    (25, 26, 5),
    (26, 27, 5),
    (27, 28, 5),
    (27, 29, 5),
]

library_edges = [
    ("Willow Glen Library", 23, 5),
    ("Berryessa Library", 27, 3),
    ("Santa Clara City Library", 20, 5),
    ("Sunnyvale Library", 15, 5),
    ("Cupertino Library", 14, 5),
    ("Mountain View Library", 15, 5),
    ("Milpitas Library", 28, 3),
    ("Stanford Green Library", 12, 5),
    ("SJSU Library", 23, 4),
    ("Santa Clara University Library", 25, 5),
]
CurrentLocation = [("CurrentLocation", 15, 5)]

libraries = [
    "Willow Glen Library",
    "Berryessa Library",
    "Santa Clara City Library",
    "Sunnyvale Library",
    "Cupertino Library",
    "Mountain View Library",
    "Milpitas Library",
    "Stanford Green Library",
    "SJSU Library",
    "Santa Clara University Library",
]

route_graph = TravelMapGraph()
route_graph.add_edge_with_list(edges)
route_graph.add_edge_with_list(library_edges)
route_graph.add_edge_with_list(CurrentLocation)
route_graph.dijkstra("CurrentLocation")
for library in libraries:
    path = route_graph.get_path(library)
    print(library)
    print(f"  Shortest Time(min): {route_graph.get_distance(library)}")
    print(f"  Path: {path}")
    print()