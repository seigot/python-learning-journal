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

    def get_opening_time(self, day):
        if day == SATURDAY:
            return self.opening_time_sat
        elif day == SUNDAY:
            return self.opening_time_sun
        raise ValueError("Invalid day")

    def get_closing_time(self, day):
        if day == SATURDAY:
            return self.closing_time_sat
        elif day == SUNDAY:
            return self.closing_time_sun
        raise ValueError("Invalid day")

    def closing_minutes(self, day):
        return convert_time_to_minutes(self.get_closing_time(day))

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
# LibraryFinderSystem Class:
# -----------------------------
class LibraryFinderSystem:
    def __init__(self):
        self.libraries = []
        self.sorted_libraries = {} # Use HashTable for sorted library list.

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
                "Stanford Green Library", "557 Escondido Mall, Stanford, CA", "10:00","21:30","12:00","24:00", "Stanford",
                True, True, "ID required at night"
            ),
            UniversityLibrary(
                "SJSU Library", "Dr. Martin Luther King Jr. Library, San Jose, CA", "08:00","18:00","13:00","18:00", "SJSU",
                True, False, "Public access allowed"
            ),
            UniversityLibrary(
                "Santa Clara University Library", "500 El Camino Real Santa Clara, CA", "09:00","22:00","9:00","23:59", "SCU",
                True, True, "Public access allowed",
            )
        ]
        if len(data) == 0:
            raise ValueError("Invalid Data Error")
        self.libraries = data
        self.sorted_libraries[SATURDAY] = self.merge_sort_libraries(self.libraries, SATURDAY)
        self.sorted_libraries[SUNDAY] = self.merge_sort_libraries(self.libraries, SUNDAY)

    def merge_sort_libraries(self, libraries, day):
        if len(libraries) <= 1:
            return libraries
        mid = len(libraries) // 2
        left = self.merge_sort_libraries(libraries[:mid], day)
        right = self.merge_sort_libraries(libraries[mid:], day)
        return self._merge(left, right, day)

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

    def binary_search_closest(self, libraries, time, day):
        target = convert_time_to_minutes(time)
        left = 0
        right = len(libraries) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_time = libraries[mid].closing_minutes(day)
            if mid_time == target:
                return mid
            elif mid_time < target:
                left = mid + 1
            else:
                right = mid - 1
        if left >= len(libraries):
            return len(libraries) - 1
        if right < 0:
            return 0
        return left

    def find_recommendations(self, time, day, k=3):
        libraries = self.sorted_libraries[day]
        target = convert_time_to_minutes(time)
        index = self.binary_search_closest(libraries, time, day)
        result = []
        i = index
        while i >= 0 and len(result) < k:
            library = libraries[i]
            if library.closing_minutes(day) <= target:
                result.append(library)
            i -= 1
        if not result:
            raise ValueError("No libraries match the requested time.")
        return result

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

    def run(self):
        self.load_libraries()
        while True:
            print("====== Library Finder ======")
            day = input("Day (Sat/Sun): ").lower()
            if day == QUIT:
                break
            time = input("Time HH:MM: ")
            if time.lower() == QUIT:
                break
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
                continue

# -----------------------------
# LibraryResultQueue Class:
# -----------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def pop_left(self):
        if self.head is None:
            raise IndexError("Queue empty")
        node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return node.data

    def is_empty(self):
        return self.head is None

class LibraryResultQueue:
    def __init__(self):
        self.items = LinkedList()

    def enqueue(self, library):
        self.items.append(library)

    def dequeue(self):
        return self.items.pop_left()

    def is_empty(self):
        return self.items.is_empty()

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
            rank += 1
# -----------------------------
# Utility functions
# -----------------------------
def convert_time_to_minutes(time_str: str) -> int:
    hour, minute = map(int, time_str.split(":"))
    return hour * 60 + minute

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

def validate_day(day: str) -> None:
    if day.lower() not in {SATURDAY, SUNDAY}:
        raise ValueError("Day must be Saturday or Sunday")

if __name__ == "__main__":
    system = LibraryFinderSystem()
    system.run_debug_tests()
    system.run()
