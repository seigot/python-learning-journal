import heapq
from collections import defaultdict
from itertools import count


def add_edge(graph, a, b, cost):
    graph[a].append((b, cost))
    graph[b].append((a, cost))


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    counter = count()
    priority_queue = [(0, next(counter), start)]

    while priority_queue:
        current_cost, _, current_node = heapq.heappop(priority_queue)

        if current_cost > distances[current_node]:
            continue

        for neighbor, edge_cost in graph[current_node]:
            new_cost = current_cost + edge_cost

            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous[neighbor] = current_node
                heapq.heappush(
                    priority_queue,
                    (new_cost, next(counter), neighbor)
                )

    return distances, previous


def get_path(previous, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    return path[::-1]


graph = defaultdict(list)

edges = [
    ("Current Location", 15, 5),

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

for a, b, cost in edges:
    add_edge(graph, a, b, cost)


library_edges = [
    ("1. Willow Glen Branch Library", 23, 5),
    ("2. Berryessa Branch Library", 27, 3),
    ("3. Santa Clara City Library", 20, 5),
    ("4. Sunnyvale Public Library", 15, 5),
    ("5. Cupertino Library", 14, 5),
    ("6. Mountain View Library", 15, 5),
    ("7. Milpitas Library", 28, 3),
    ("8. Stanford Cecil H Green Library", 12, 5),
    ("9. SJSU Library", 23, 4),
    ("10. Santa Clara University Library", 25, 5),
]

for library, junction, cost in library_edges:
    add_edge(graph, library, junction, cost)


libraries = [
    "1. Willow Glen Branch Library",
    "2. Berryessa Branch Library",
    "3. Santa Clara City Library",
    "4. Sunnyvale Public Library",
    "5. Cupertino Library",
    "6. Mountain View Library",
    "7. Milpitas Library",
    "8. Stanford Cecil H Green Library",
    "9. SJSU Library",
    "10. Santa Clara University Library",
]


distances, previous = dijkstra(graph, "Current Location")


for library in libraries:
    path = get_path(previous, library)

    print(library)
    print(f"  Minimum Cost: {distances[library]}")
    print(f"  Path: {path}")
    print()