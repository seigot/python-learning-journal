# chatGPT: https://chatgpt.com/share/69ae3179-7bfc-8009-99f0-79f11afaca63

# -----------------------------
# Global variables/constants
# -----------------------------
SATURDAY = "sat" #SATURDAY
SUNDAY = "sun"   #SUNDAY
QUIT = "q"       #QUIT Command

# -----------------------------
# Library classes:
# -----------------------------
class Library:
    def __init__(
        self,
        name,
        address,
        opening_time_sat,
        closing_time_sat,
        opening_time_sun,
        closing_time_sun,
        is_public_access,
    ):
        self.name = name
        self.address = address
        self.opening_time_sat = opening_time_sat
        self.closing_time_sat = closing_time_sat
        self.opening_time_sun = opening_time_sun
        self.closing_time_sun = closing_time_sun
        self.is_public_access = is_public_access
        self.shortest_time = -1 # update dynamically
        self.shortest_path = -1 # update dynamically

    # Return the opening time of the library for the specified day.
    def get_opening_time(self, day):
        if day == SATURDAY:
            return self.opening_time_sat
        elif day == SUNDAY:
            return self.opening_time_sun
        raise ValueError("Invalid day")

    # Return the closing time of the library for the specified day.
    def get_closing_time(self, day):
        if day == SATURDAY:
            return self.closing_time_sat
        elif day == SUNDAY:
            return self.closing_time_sun
        raise ValueError("Invalid day")

    # Convert the closing time of the library into minutes.
    def closing_minutes(self, day):
        return convert_time_to_minutes(self.get_closing_time(day))

    # Return whether the library is accessible to the public.
    def can_access_in_public(self):
        return self.is_public_access

# PublicLibrary Class: This class inherits from the Library base class.
class PublicLibrary(Library):
    def __init__(
        self,
        name,
        address,
        opening_time_sat,
        closing_time_sat,
        opening_time_sun,
        closing_time_sun,
        city,
    ):
        super().__init__(
            name,
            address,
            opening_time_sat,
            closing_time_sat,
            opening_time_sun,
            closing_time_sun,
            True,
        )
        self.city = city

# UniversityLibrary Class: This class inherits from the Library base class.
class UniversityLibrary(Library):
    def __init__(
        self,
        name,
        address,
        opening_time_sat,
        closing_time_sat,
        opening_time_sun,
        closing_time_sun,
        university_name,
        visitor_access_allowed,
        requires_id,
        access_note,
    ):
        super().__init__(
            name,
            address,
            opening_time_sat,
            closing_time_sat,
            opening_time_sun,
            closing_time_sun,
            visitor_access_allowed,
        )
        self.university_name = university_name
        self.visitor_access_allowed = visitor_access_allowed
        self.requires_id = requires_id
        self.access_note = access_note

    # Return a human-readable description of access conditions.
    def get_access_condition(self):
        if not self.visitor_access_allowed:
            condition = "Visitors not allowed"
        elif self.requires_id:
            condition = "Visitors allowed but ID required"
        else:
            condition = "Visitors allowed"
        if self.access_note:
            condition += f" ({self.access_note})"
        return condition

# -----------------------------
# LibraryFinderSystem Class: This class finds the best matching libraries by sorting and searching the data.
# -----------------------------
class LibraryFinderSystem:
    def __init__(self):
        self.libraries = []
        self.sorted_libraries = {} # Use HashTable for sorted library list.
        self.Travel_Map_Graph = TravelMapGraph() # TravelMap for search distance to the library.

    # Load library data into the system and initialize sorted structures.
    def load_libraries(self):
        data = [
            PublicLibrary("Willow Glen Library","1157 Minnesota Ave, San Jose, CA","09:00","18:00","00:00","00:00","San Jose"),
            PublicLibrary("Berryessa Library","3355 Noble Ave, San Jose, CA","10:00","18:00","12:00","17:00","San Jose"),
            PublicLibrary("Santa Clara City Library","2635 Homestead Rd Santa Clara, CA","10:00", "16:00","13:00","17:00","Santa Clara"),
            PublicLibrary("Sunnyvale Library","665 W Olive Ave, Sunnyvale, CA","10:00", "18:00","13:00","18:00","Sunnyvale"),
            PublicLibrary("Cupertino Library","10800 Torre Ave, Cupertino, CA","10:00","18:30","10:00","18:30","Cupertino"),
            PublicLibrary("Mountain View Library","585 Franklin St, Mountain View, CA","10:00","18:00","13:00","17:00","Mountain View"),
            PublicLibrary("Milpitas Library","160 N Main St, Milpitas, CA","10:00","19:00","10:00","19:00","Milpitas"),
            UniversityLibrary(
                "Stanford Green Library", "557 Escondido Mall, Stanford, CA", "10:00","21:30","12:00","21:30", "Stanford",
                True, True, "ID required at night"
            ),
            UniversityLibrary(
                "SJSU Library", "Dr. Martin Luther King Jr. Library, San Jose, CA", "08:00","18:00","13:00","18:00", "SJSU",
                True, False, "Public access allowed"
            ),
            UniversityLibrary(
                "Santa Clara University Library", "500 El Camino Real Santa Clara, CA", "09:00","22:00","9:00","22:00", "SCU",
                True, True, "Public access allowed",
            )
        ]
        if len(data) == 0:
            raise ValueError("Invalid Data Error")
        self.libraries = data
        self.sorted_libraries[SATURDAY] = self.merge_sort_libraries(self.libraries, SATURDAY)
        self.sorted_libraries[SUNDAY] = self.merge_sort_libraries(self.libraries, SUNDAY)

    # Sort libraries by closing time using merge sort.
    def merge_sort_libraries(self, libraries, day):
        if len(libraries) <= 1:
            return libraries
        mid = len(libraries) // 2
        left = self.merge_sort_libraries(libraries[:mid], day)
        right = self.merge_sort_libraries(libraries[mid:], day)
        return self._merge(left, right, day)

    # Merge two sorted lists of libraries into one sorted list.
    def _merge(self, left, right, day):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].closing_minutes(day) <= right[j].closing_minutes(day):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    # Find the index of the library with the closest closing time that does not exceed the target time.
    def binary_search_closest(self, libraries, time, day):
        target = convert_time_to_minutes(time)
        answer = -1

        left = 0
        right = len(libraries) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_time = libraries[mid].closing_minutes(day)
            if mid_time <= target:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer

    # Return up to k recommended libraries that close before or at the target time.
    def find_recommendations(self, time, day, k=3):
        libraries = self.sorted_libraries[day]
        index = self.binary_search_closest(libraries, time, day)
        if index == -1:
            raise ValueError("No libraries match the requested time.")
        target = convert_time_to_minutes(time)

        result = []
        i = index
        while i >= 0 and len(result) < k:
            library = libraries[i]
            if library.closing_minutes(day) <= target:
                # Update library shortesttime/path.
                library_name = library.name
                shortest_time = self.Travel_Map_Graph.get_distance(library_name)
                path = self.Travel_Map_Graph.get_path(library_name)
                library.shortest_time = shortest_time
                library.shortest_path = path
                # Update result list.
                result.append(library)
            i -= 1
        return result

    # Run predefined test cases for debugging purposes.
    def run_debug_tests(self):
        self.load_libraries()
        print("\n--- DEBUG TESTS ---")
        tests = [
            ("pattern1", SATURDAY, "20:00"),
            ("pattern2", SUNDAY, "18:00"),
            ("pattern3", SATURDAY, "05:00"),
            ("pattern4", SATURDAY, "8pm"),
        ]
        for name, day, time in tests:
            print("--")
            print("[DEBUG]",name, day, time, "===")
            try:
                validate_day(day)
                validate_time_format(time)
                results = self.find_recommendations(time, day)
                q = LibraryResultQueue()
                for r in results:
                    q.enqueue(r)
                q.display_results(day)
            except Exception as e:
                print("Error:", e)
    # Run the main interactive program loop.
    def run(self):
        self.load_libraries()
        self.Travel_Map_Graph.InitializeMapdata()

        while True:
            print("====== Weekend Library Closing Time Finder ======")
            day = input("Day (Sat/Sun): ").lower()
            if day == QUIT:
                break
            time = input("Time HH:MM: ")
            if time.lower() == QUIT:
                break
            try:
                # Input data Validation
                validate_day(day)
                validate_time_format(time)
                # Find recommended library
                results = self.find_recommendations(time, day)
                q = LibraryResultQueue()
                for r in results:
                    q.enqueue(r)
                q.display_results(day)
            except Exception as e:
                print("Error:", e)
                continue

# -----------------------------
# LibraryResultQueue Class: This class manages and displays the results in order using a queue.
# -----------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add a new item to the end of the linked list.
    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # Remove and return the first item in the linked list.
    def pop_left(self):
        if self.head is None:
            raise IndexError("Queue empty")
        node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return node.data

    # Check whether the linked list is empty.
    def is_empty(self):
        return self.head is None

class LibraryResultQueue:
    def __init__(self):
        self.items = LinkedList()

    # Add a library to the queue.
    def enqueue(self, library):
        self.items.append(library)

    # Remove and return the next library from the queue.
    def dequeue(self):
        return self.items.pop_left()

    # Check if the queue is empty.
    def is_empty(self):
        return self.items.is_empty()

    # Display library search results in ranked order.
    def display_results(self, day):
        rank = 1
        while not self.is_empty():
            library = self.dequeue()
            print(f"== Result:{rank}. {library.name} ==")
            print(f"   - Opening: {library.get_opening_time(day)} - Closing: {library.get_closing_time(day)}")
            print(f"   - Address: {library.address}")
            if isinstance(library, UniversityLibrary):
                print("   - Access:", library.get_access_condition())
            else:
                print("   - Access: Public")
            print(f"   - ShortestTime(min): {library.shortest_time}")
            print(f"   - ShortestPath: {library.shortest_path}")
            rank += 1

## Update for FinalProject 
import heapq
from itertools import count
class TravelMapGraph:
    # Store graph connections, shortest distances, using dijkstra algorithm.
    # and previous nodes for path reconstruction.
    def __init__(self):
        self.graph = {}
        self.distances = {}
        self.previous = {}

    def add_node(self, node):
        # Add a new node if it does not exist.
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, a, b, cost):
        # Connect two nodes with travel cost.
        self.add_node(a)
        self.add_node(b)
        self.graph[a].append((b, cost))
        self.graph[b].append((a, cost))

    def add_edge_with_list(self, edges):
        # Add multiple edges with edge lists.
        for a, b, cost in edges:
            self.add_edge(a, b, cost)

    def dijkstra(self, start):
        # Find shortest travel time from start node to all other nodes using Dijkstra's algorithm.
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
                    heapq.heappush( priority_queue, (new_cost, next(counter), neighbor))

    def get_path(self, destination):
        # Reconstruct the shortest path by tracing previous nodes backward.
        path = []
        current = destination

        while current is not None:
            path.append(current)
            current = self.previous[current]
        return path[::-1]

    def get_distance(self, destination):
        # Return the shortest travel time from the start node to destination.
        return self.distances[destination]
    
    def InitializeMapdata(self):
        # InitializeMapData function initializes the map for searching the library.
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

        self.add_edge_with_list(edges)
        self.add_edge_with_list(library_edges)
        self.SetCurrentLocationtoMapdata()

    def SetCurrentLocationtoMapdata(self, CurrentIndex="CurrentLocation", CurrentAdjEdgeIndex=15, CurrentAdjEdgeCost=5):
        # Set the edge to Current Location
        # This function should be updated with actual current location.
        # Currently Set Current location with fixed number.
        CurrentLocation = [(CurrentIndex, CurrentAdjEdgeIndex, CurrentAdjEdgeCost)]
        self.add_edge_with_list(CurrentLocation)
        self.dijkstra(CurrentIndex)

# -----------------------------
# Utility functions
# -----------------------------
# Convert a time string (HH:MM) into total minutes.
def convert_time_to_minutes(time_str: str) -> int:
    hour, minute = map(int, time_str.split(":"))
    return hour * 60 + minute

# Validate that the input time is in HH:MM format and within valid ranges.
def validate_time_format(time_str: str) -> None:
    parts = time_str.split(":")
    if len(parts) != 2:
        raise ValueError("Time must be HH:MM format")
    hour, minute = parts
    if not (hour.isdigit() and minute.isdigit()):
        raise ValueError("Time must contain numbers")
    hour = int(hour)
    minute = int(minute)
    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        raise ValueError("Invalid time")
# Validate that the input day is either Saturday or Sunday.
def validate_day(day: str) -> None:
    if day.lower() not in {SATURDAY, SUNDAY}:
        raise ValueError("Day must be Saturday or Sunday")

if __name__ == "__main__":
    system = LibraryFinderSystem()
#    system.run_debug_tests()
    system.run()
