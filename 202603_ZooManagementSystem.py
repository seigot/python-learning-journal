# chatGPT: https://chatgpt.com/share/69b4dbde-fe6c-8009-bc76-4acbc70dbc2b

class Animal:
    def __init__(self, name, species, care_level):
        self.name = name
        self.species = species
        self.care_level = care_level

    def __str__(self):
        return f"{self.name} ({self.species}) - Care Level: {self.care_level}"


class HashNode:
    def __init__(self, key, value):
        self.key = key              # animal name
        self.value = value          # Animal object
        self.next = None


class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        # Hash function : 
        #   It sums the ASCII values of all characters in the key and uses 
        #   the remainder after dividing by the table size.
        return sum(ord(c) for c in key) % self.size

    def insert(self, animal):
        # Get Hash value and Head Pointer
        index = self._hash(animal.name)
        head = self.table[index]
        # Search Insertion point
        current = head
        while current:
            if current.key == animal.name:
                raise ValueError(f"Animal '{animal.name}' already exists.")
            current = current.next
        # Insert Process
        new_node = HashNode(animal.name, animal)
        new_node.next = head
        self.table[index] = new_node

    def search(self, name):
        index = self._hash(name)
        current = self.table[index]

        while current:
            if current.key == name:
                return current.value
            current = current.next
        return None

    def delete(self, name):
        index = self._hash(name)
        current = self.table[index]
        prev = None

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

    def get_all_animals(self):
        animals = []
        for head in self.table:
            current = head
            while current:
                animals.append(current.value)
                current = current.next
        return animals

    def display(self):
        print("=== Hash Table ===")
        for i, head in enumerate(self.table):
            print(f"Bucket {i}:", end=" ")
            current = head
            if not current:
                print("Empty")
                continue

            chain = []
            while current:
                chain.append(current.key)
                current = current.next
            print(" -> ".join(chain))


class BSTNode:
    def __init__(self, care_level):
        self.care_level = care_level
        self.animals = []
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

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
#  - search_animal: 
#  - delete_animal: 
#  - update_care_level: 
#  - periodic_increase: 
#  - get_basic_care_animals: 
#  - get_advanced_care_animals: 
#  - get_intensive_care_animals: 
#  - display_all:
#########
class ZooManagementSystem:
    def __init__(self):
        self.hash_table = HashTable()
        self.bst = BST()

    def add_animal(self, name, species, care_level):
        animal = Animal(name, species, care_level)
        self.hash_table.insert(animal)
        self.bst.insert(animal)

    def search_animal(self, name):
        return self.hash_table.search(name)

    def delete_animal(self, name):
        animal = self.hash_table.search(name)
        if animal is None:
            raise ValueError(f"Animal '{name}' not found.")

        self.bst.remove(animal)
        self.hash_table.delete(name)

    def update_care_level(self, animal):
        if animal.care_level >= 10:
            return

        self.bst.remove(animal)
        animal.care_level += 1
        self.bst.insert(animal)

    def periodic_increase(self):
        animals = self.hash_table.get_all_animals()
        for animal in animals:
            self.update_care_level(animal)

    def get_basic_care_animals(self):
        return self.bst.range_search(1, 3)

    def get_advanced_care_animals(self):
        return self.bst.range_search(4, 7)

    def get_intensive_care_animals(self):
        return self.bst.range_search(8, 10)

    def display_all(self):
        self.hash_table.display()
        self.bst.display_inorder()


def print_animals(title, animals):
    print(f"\n{title}")
    if not animals:
        print("No animals found.")
        return
    for animal in animals:
        print(animal)


def main():
    zoo = ZooManagementSystem()

    # Insert 10 sample animals
    zoo.add_animal("Leo", "Lion", 5)
    zoo.add_animal("Penny", "Penguin", 3)
    zoo.add_animal("Ella", "Elephant", 7)
    zoo.add_animal("Milo", "Monkey", 2)
    zoo.add_animal("Zara", "Zebra", 4)
    zoo.add_animal("Tony", "Tiger", 8)
    zoo.add_animal("Gina", "Giraffe", 6)
    zoo.add_animal("Hugo", "Hippo", 5)
    zoo.add_animal("Benny", "Bear", 3)
    zoo.add_animal("Ruby", "Rabbit", 1)

    print("INITIAL DATA")
    zoo.display_all()

    # Search by name
    print("\n=== Search Test ===")
    animal = zoo.search_animal("Leo")
    print(animal)

    # Facility retrieval
    print_animals("Basic Care (1-3):", zoo.get_basic_care_animals())
    print_animals("Advanced Care (4-7):", zoo.get_advanced_care_animals())
    print_animals("Intensive Care (8-10):", zoo.get_intensive_care_animals())

    # Periodic increase
    print("\n=== Before Periodic Increase ===")
    zoo.bst.display_inorder()

    zoo.periodic_increase()

    print("\n=== After Periodic Increase ===")
    zoo.bst.display_inorder()

    # Delete test
    print("\n=== Delete Test ===")
    zoo.delete_animal("Penny")
    deleted = zoo.search_animal("Penny")
    print("Search after delete:", deleted)

    print_animals("Basic Care after deleting Penny:", zoo.get_basic_care_animals())

    # Collision example
    print("\n=== Hash Table Collision View ===")
    zoo.hash_table.display()


if __name__ == "__main__":
    main()