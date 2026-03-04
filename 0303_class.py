
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class StackLinkedList:
    def __init__(self):
        self.top = None
        self.length = 0
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.length += 1
    def pop(self):
        if self.isEmpty():
            print("Error, attempting to pop empty stack!")
            return None
        item = self.top.data
        self.top = self.top.next
        self.length -= 1
        return item
    def isEmpty(self):
        return self.length == 0
    def printstatus(self):
        print("----- Stack Status -----")
        print("Length:", self.length)
        if self.isEmpty():
            print("Stack is empty")
            return
        print("Top:", self.top.data)
        current = self.top
        print("Stack elements (top → bottom):")
        while current is not None:
            print(current.data)
            current = current.next

_LinkedList = StackLinkedList()
_LinkedList.push(1)
_LinkedList.printstatus()
_LinkedList.push(2)
_LinkedList.push(3)
_LinkedList.printstatus()
_LinkedList.pop()
_LinkedList.pop()
_LinkedList.printstatus()

