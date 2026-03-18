class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        self.root = self._insert_recursive(self.root, data)
    def _insert_recursive(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        return node

    def search(self, data):
        current = self.root
        while current:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

bst = BinarySearchTree()
bst.insert(0)
bst.insert(100)
bst.insert(10)
bst.insert(1000)
print(bst.search(100))
print(bst.search(10000))

