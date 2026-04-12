class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def leftRotation(self, currRoot):
        # rotate to left
        newRoot = currRoot.right
        currRoot.right = newRoot.left
        newRoot.left = currRoot

        currRoot.height = self.calcHeight(currRoot)
        newRoot.height = self.calcHeight(newRoot)

        return newRoot

    def rightRotation(self, currRoot):
        # rotate to right
        newRoot = currRoot.left
        currRoot.left = newRoot.right
        newRoot.right = currRoot

        currRoot.height = self.calcHeight(currRoot)
        newRoot.height = self.calcHeight(newRoot)

        return newRoot

    def rightLeftRotation(self, currRoot):
        currRoot.right = self.rightRotation(currRoot.right)
        return self.leftRotation(currRoot)

    def leftRightRotation(self, currRoot):
        currRoot.left = self.leftRotation(currRoot.left)
        return self.rightRotation(currRoot)

    def calcHeight(self, node):
        if node.left is None:
            lh = -1
        else:
            lh = node.left.height

        if node.right is None:
            rh = -1
        else:
            rh = node.right.height

        return max(lh, rh) + 1


# --------------------------
# Test Code
# --------------------------

def print_tree_info(root, title):
    print(f"\n{title}")
    print("-" * 30)
    if root is None:
        print("Tree is empty")
        return

    print(f"Root: {root.data}, height={root.height}")

    if root.left:
        print(f"Left child: {root.left.data}, height={root.left.height}")
    else:
        print("Left child: None")

    if root.right:
        print(f"Right child: {root.right.data}, height={root.right.height}")
    else:
        print("Right child: None")


# Test 1: Left Rotation
tree = AVLTree()

root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

root.right.right.height = 0
root.right.height = tree.calcHeight(root.right)
root.height = tree.calcHeight(root)

print_tree_info(root, "Before Left Rotation")
new_root = tree.leftRotation(root)
print_tree_info(new_root, "After Left Rotation")


# Test 2: Right Rotation
root2 = Node(30)
root2.left = Node(20)
root2.left.left = Node(10)

root2.left.left.height = 0
root2.left.height = tree.calcHeight(root2.left)
root2.height = tree.calcHeight(root2)

print_tree_info(root2, "Before Right Rotation")
new_root2 = tree.rightRotation(root2)
print_tree_info(new_root2, "After Right Rotation")


# Test 3: Right-Left Rotation
root3 = Node(10)
root3.right = Node(30)
root3.right.left = Node(20)

root3.right.left.height = 0
root3.right.height = tree.calcHeight(root3.right)
root3.height = tree.calcHeight(root3)

print_tree_info(root3, "Before Right-Left Rotation")
new_root3 = tree.rightLeftRotation(root3)
print_tree_info(new_root3, "After Right-Left Rotation")


# Test 4: Left-Right Rotation
root4 = Node(30)
root4.left = Node(10)
root4.left.right = Node(20)

root4.left.right.height = 0
root4.left.height = tree.calcHeight(root4.left)
root4.height = tree.calcHeight(root4)

print_tree_info(root4, "Before Left-Right Rotation")
new_root4 = tree.leftRightRotation(root4)
print_tree_info(new_root4, "After Left-Right Rotation")
