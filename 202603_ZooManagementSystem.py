# chatGPT: https://chatgpt.com/share/69b4dbde-fe6c-8009-bc76-4acbc70dbc2b

# #####
# Class: Animal
# #####
class Animal:
    def __init__(self, name, species, care_level):
        self.name = name
        self.species = species
        self.care_level = care_level

    def __str__(self):
        return f"{self.name} ({self.species}) - Care Level: {self.care_level}"

# #####
# Class: HashNode 
#   This is for HashTable chaining for collision resolusion.
# #####
class HashNode:
    def __init__(self, key, value):
        self.key = key              # animal name
        self.value = value          # Animal object
        self.next = None

# #####
# Class: HashTable
# #####
class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        # Hash function : 
        #   It sums the ASCII values of all characters in the key and uses 
        #   the remainder after dividing by the table size.
        return sum(ord(c) for c in key) % self.size

    # [Requirement]: insertion
    #  average: O(1)
    #  worst: O(n)
    def insert(self, animal):
        # 1.Get Hash value and Head Pointer
        index = self._hash(animal.name)
        head = self.table[index]
        # 2.Search Insertion point
        current = head
        while current:
            if current.key == animal.name:
                raise ValueError(f"Animal '{animal.name}' already exists.")
            current = current.next
        # 3.Main insertion Process
        new_node = HashNode(animal.name, animal)
        new_node.next = head
        self.table[index] = new_node

    # [Requirement]: searching by animal name.
    #  average: O(1)
    #  worst: O(n)
    def search(self, name):
        index = self._hash(name)
        current = self.table[index]

        while current:
            if current.key == name:
                return current.value
            current = current.next
        return None

    # [Requirement]: deletion.
    #  average: O(1)
    #  worst: O(n)
    def delete(self, name):
        index = self._hash(name)
        current = self.table[index]
        prev = None
        # find animal name from chained object
        while current:
            if current.key == name:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return current.value
            prev = current
            current = current.next

        raise ValueError(f"Animal '{name}' not found in HashTable.")

    # Helper function to get all animals.
    def get_all_animals(self):
        animals = []
        for head in self.table:
            current = head
            while current:
                animals.append(current.value)
                current = current.next
        return animals

    # Helper function to display all animals.
    def display(self):
        for i, head in enumerate(self.table):
            print(f"Bucket {i}:", end=" ")
            current = head
            if not current:
                print("-")
                continue
            chain = []
            while current:
                chain.append(current.key)
                current = current.next
            print(" -> ".join(chain))

# #####
#  Class: BSTNode, 
#    The node for Binary search tree, store animals by linked list which have same priority. 
# #####
class BSTNode:
    def __init__(self, care_level):
        self.care_level = care_level
        self.animals = []
        self.left = None
        self.right = None

# #####
#  Class: BST, Binary Search tree to find animals.
# #####
class BST:
    def __init__(self):
        self.root = None

    # [Requirement] insertion of animals based on care level.
    def insert(self, animal):
        self.root = self._insert(self.root, animal)

    def _insert(self, node, animal):
        if node is None:
            node = BSTNode(animal.care_level)
            node.animals.append(animal)
            return node

        if animal.care_level < node.care_level:
            node.left = self._insert(node.left, animal)
        elif animal.care_level > node.care_level:
            node.right = self._insert(node.right, animal)
        else:
            if animal not in node.animals:
                node.animals.append(animal)

        return node

    # Remove animals based on the name of the animal.
    def remove(self, animal):
        self.root = self._remove(self.root, animal)

    def _remove(self, node, animal):
        if node is None:
            return None

        if animal.care_level < node.care_level:
            node.left = self._remove(node.left, animal)
        elif animal.care_level > node.care_level:
            node.right = self._remove(node.right, animal)
        else:
            if animal in node.animals:
                node.animals.remove(animal)

            if len(node.animals) == 0:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left

                successor = self._get_min(node.right)
                node.care_level = successor.care_level
                node.animals = successor.animals[:]
                node.right = self._remove_node_by_level(node.right, successor.care_level)

        return node

    def _remove_node_by_level(self, node, care_level):
        if node is None:
            return None

        if care_level < node.care_level:
            node.left = self._remove_node_by_level(node.left, care_level)
        elif care_level > node.care_level:
            node.right = self._remove_node_by_level(node.right, care_level)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self._get_min(node.right)
            node.care_level = successor.care_level
            node.animals = successor.animals[:]
            node.right = self._remove_node_by_level(node.right, successor.care_level)

        return node

    def _get_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # [Requirement] 
    #   Efficiently retrieve animals that urgently need attention within a care level range.
    #   Search BST recursively by refering "min_level" and "max_level".
    def range_search(self, min_level, max_level):
        result = []
        self._range_search(self.root, min_level, max_level, result)
        return result

    def _range_search(self, node, min_level, max_level, result):
        if node is None:
            return

        if node.care_level > min_level:
            self._range_search(node.left, min_level, max_level, result)

        if min_level <= node.care_level <= max_level:
            result.extend(node.animals)

        if node.care_level < max_level:
            self._range_search(node.right, min_level, max_level, result)

    def display_inorder(self):
        print("=== BST Inorder ===")
        self._display_inorder(self.root)

    def _display_inorder(self, node):
        if node is None:
            return
        self._display_inorder(node.left)
        names = [animal.name for animal in node.animals]
        print(f"Care Level {node.care_level}: {names}")
        self._display_inorder(node.right)

#########
# Class: ZooManagementSystem
# Method:
#  - add_animal: 
#      Adds a new animal to the system and inserts it into both the hash table and the BST 
#      based on its care level.
#  - search_animal:
#      Searches for an animal by its unique name using the hash table for fast lookup.
#  - delete_animal: 
#      Removes an animal from both the hash table and the BST to keep the system data consistent.
#  - update_care_level: 
#      pdates an animal’s care level and reinserts it into the BST at the correct position.
#  - periodic_increase: 
#      Simulates the passage of time by increasing care levels of unattended animals and updating the BST.
#  - get_basic_care_animals: 
#      Retrieves animals with care levels from 1 to 3 for the Basic Care facility.
#  - get_advanced_care_animals: 
#      Retrieves animals with care levels from 4 to 7 for the Advanced Care facility.
#  - get_intensive_care_animals: 
#      Retrieves animals with care levels from 8 to 10 for the Intensive Care facility.
#  - display_all:
#      Displays all animals currently stored in the zoo management system.
#########
class ZooManagementSystem:
    def __init__(self):
        self.hash_table = HashTable()
        self.bst = BST()

    # Adds a new animal to the system and inserts it into both the hash table and the BST 
    # based on its care level.
    def add_animal(self, name, species, care_level):
        if not (1 <= care_level <= 10):
            raise ValueError("Care level must be between 1 and 10.")
        animal = Animal(name, species, care_level)
        self.hash_table.insert(animal)
        self.bst.insert(animal)

    # Searches for an animal by its unique name using the hash table for fast lookup.
    def search_animal(self, name):
        return self.hash_table.search(name)

    # Removes an animal from both the hash table and the BST to keep the system data consistent.
    def delete_animal(self, name):
        animal = self.hash_table.search(name)
        if animal is None:
            raise ValueError(f"Animal '{name}' not found.")

        self.bst.remove(animal)
        self.hash_table.delete(name)

    # Updates an animal’s care level and reinserts it into the BST at the correct position.
    def update_care_level(self, animal):
        if animal.care_level >= 10:
            return
        self.bst.remove(animal)
        animal.care_level += 1
        self.bst.insert(animal)

    # Simulates the passage of time by increasing care levels of unattended animals and updating the BST.
    def periodic_increase(self):
        animals = self.hash_table.get_all_animals()
        for animal in animals:
            self.update_care_level(animal)

    # get_basic_care_animals: 
    def get_basic_care_animals(self):
        return self.bst.range_search(1, 3)

    # get_advanced_care_animals: 
    def get_advanced_care_animals(self):
        return self.bst.range_search(4, 7)

    # get_intensive_care_animals: 
    def get_intensive_care_animals(self):
        return self.bst.range_search(8, 10)

    # display_all:
    def display_all(self):
        self.hash_table.display()
        self.bst.display_inorder()

# Helper Function
def print_animals(title, animals):
    print(f"\n{title}")
    if not animals:
        print("No animals found.")
        return
    for animal in animals:
        print(animal)

def main():

    # 1.Get ZooManagementSystem object instance
    zoo = ZooManagementSystem()

    # 2.1.Insert 10 sample animals
    print("\n=== 2.1. Insertion ===")
    zoo.add_animal("Leo", "Lion", 5)
    zoo.add_animal("Penny", "Penguin", 3)
    zoo.add_animal("Ella", "Elephant", 10)
    zoo.add_animal("Milo", "Monkey", 2)
    zoo.add_animal("Zara", "Zebra", 4)
    zoo.add_animal("Tony", "Tiger", 8)
    zoo.add_animal("Gina", "Giraffe", 7)
    zoo.add_animal("Hugo", "Hippo", 5)
    zoo.add_animal("Benny", "Bear", 3)
    zoo.add_animal("Ruby", "Rabbit", 1)
    zoo.display_all()
    print("[Continue to push Enter...]")
    input()

    # 2.2 Deletion
    print("\n=== 2.2 Deletion ===")
    zoo.delete_animal("Tony")
    zoo.display_all()
    print("[Continue to push Enter...]")
    input()

    # 3.1.Search by name
    print("\n=== 3.1.Search by name ===")
    animal = zoo.search_animal("Leo")
    print(animal)
    animal = zoo.search_animal("Benny")
    print(animal)
    print("[Continue to push Enter...]")
    input()

    # 3.2.Efficiently retrieve animals within a care level range.
    print("\n=== 3.2.Efficiently retrieve animals within a care level range. ===")
    print_animals("Basic Care (1-3):", zoo.get_basic_care_animals())
    print_animals("Advanced Care (4-7):", zoo.get_advanced_care_animals())
    print_animals("Intensive Care (8-10):", zoo.get_intensive_care_animals())
    print("[Continue to push Enter...]")
    input()

    # 3.3 Periodic increase
    print("\n=== 3.3 Periodic increase ===")
    zoo.periodic_increase()
    print("\n=== After Periodic Increase ===")
    zoo.display_all()
    print_animals("Basic Care (1-3):", zoo.get_basic_care_animals())
    print_animals("Advanced Care (4-7):", zoo.get_advanced_care_animals())
    print_animals("Intensive Care (8-10):", zoo.get_intensive_care_animals())
    print("[Continue to push Enter...]")
    input()

if __name__ == "__main__":
    main()