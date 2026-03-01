# AI: https://chatgpt.com/share/69a3ba1d-17b4-8009-83b9-e512ad259864

##### ############################# #####
##### Definition of Data Structure  #####
##### ############################# #####

## ################### ##
## 2) Required Classes ##
## ################### ##

# --------------------------------------------- #
# Order class with inheritance + polymorphism.
# 
# order_id  : Order identifier. A sequential number assigned in the customer orders arrive. 
# menu_id   : Identifier of the menu item associated with the order_id. 
#             The definitions are listed in the menu list.
# item_name : Name of the item associated with the menu_id.
# price     : Price of the item associated with the menu_id.
# --------------------------------------------- #
class Order:
    def __init__(self, order_id, menu_id, item_name, price):
        self.order_id = order_id
        self.menu_id = menu_id
        self.item_name = item_name
        self.price = price
        self.prep_stack = Stack()
        for s in reversed(self.prep_steps()):
            self.prep_stack.push(s)
    def prep_steps(self):
        raise NotImplementedError
    def process_step(self):
        return self.prep_stack.pop()
    def is_complete(self):
        return self.prep_stack.is_empty()
class DineInOrder(Order):
    def prep_steps(self):
        return ["cook", "plate", "serve"]
class TakeoutOrder(Order):
    def prep_steps(self):
        return ["cook", "pack"]
    
# --------------------------------------- #
# Node based Stack / Queue / Linkedlist.  #
# --------------------------------------- #
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
# ----- #
# Stack #
# ----- #
class Stack:
    def __init__(self):
        self._top = None
        self._size = 0
    def push(self, item):
        self._top = Node(item, next=self._top)
        self._size += 1
    def pop(self):
        if self._top is None:
            return None
        node = self._top
        self._top = node.next
        self._size -= 1
        return node.data  # type: ignore[return-value]
    def is_empty(self):
        return self._top is None
    def size(self):
        return self._size

# ----- #
# Queue #
# ----- #
class Queue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size: int = 0
    def enqueue(self, item):
        node = Node(item)
        if self._rear is None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1
    def dequeue(self):
        if self._front is None:
            return None
        node = self._front
        self._front = node.next
        self._size -= 1
        if self._front is None:
            self._rear = None  # When this is last index, reset rear as well.
        return node.data
    def is_empty(self):
        return self._front is None
    def size(self):
        return self._size
# ---------- #
# LinkedList #
# ---------- #
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size: int = 0

    def append(self, order):
        node = Node(order)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1
    def head(self):
        if self._head is None:
            return None
        return self._head.data
    def remove_head(self):
        if self._head is None:
            return None
        node = self._head
        self._head = node.next
        self._size -= 1
        if self._head is None:
            self._tail = None
        return node.data
    def is_empty(self):
        return self._head is None
    def size(self):
        return self._size

## ########################### ##
## 3) Required Data Structures ##
## ########################### ##

# Menu list: Store the menu.
menu = [
        (1, "Burger", 12.00),
        (2, "Salad",   9.00),
        (3, "Pizza",  15.00),
]
# Completed orders list: Store the completed orders.
completed_orders = []
# Active kitchen Linkedlist: store active kitchen orders.
active_kitchen = LinkedList()
# Waiting_queue: store waiting customer orders.
waiting_queue  = Queue()

# -------------------
# Main Function
# 4) Required Simulation Cycle
# Each time step must do the following in order:
#  1.Add arriving customers/orders to the queue
#  2.Move the next waiting order from the queue into the active kitchen linked list
#  3.Process prep steps using the stack
#  4.Mark finished orders as complete and move them to the completed orders list
#  5.Print a status log for that time step
# -------------------
def main():

    # arrival customers
    arrivals = [
        # order_id, menu_id, item_name, price
        DineInOrder(1, 1, "Burger", 12.00),
        TakeoutOrder(2, 2, "Salad", 9.00),
        DineInOrder(3, 3, "Pizza", 15.00),
        TakeoutOrder(4, 1, "Burger", 12.00),
        DineInOrder(5, 2, "Salad", 9.00),
    ]

    # Counter for print log
    dinein_count  = 0
    takeout_count = 0
    revenue       = 0.0

    next_order_id = 1
    for t, order in enumerate(arrivals, start=1):

        order_summary = (f"id={order.order_id} item={order.item_name} price={order.price:.2f}")
        # -------------------------
        # 1.Add arriving customers/orders to the queue
        # -------------------------
        waiting_queue.enqueue(order)
        arrived_summary = (f"Successfully add customer order to the queue")

        # -------------------------
        # 2.Move the next waiting order from the queue into the active kitchen linked list
        # -------------------------
        moved_summary = "none"
        moved_order = waiting_queue.dequeue()
        if moved_order is not None:
            active_kitchen.append(moved_order)
            moved_summary = f"[Success] move the order from the queue to kitchen list, dequeued id={moved_order.order_id}"

        # -------------------------
        #  3.Process prep steps using the stack
        # -------------------------
        cook_summary = "none"
        current = active_kitchen.head()
        if current is not None:
            result = []
            while not current.is_complete():
                step = current.process_step()
                result.append(step)
            # step = current.process_step()
            # result.append(step)
            cook_summary = f"[Success] processed prep steps, cur id={current.order_id} step={result}"

        # -------------------------
        #  4.Mark finished orders as complete and move them to the completed orders list
        # -------------------------
        done_summary = "none"
        if current is not None and current.is_complete():
            done = active_kitchen.remove_head()
            if done is not None:
                # Successfully completed orders
                revenue += done.price
                completed_orders.append(done)                
                if isinstance(done, DineInOrder):
                    dinein_count += 1
                else:
                    takeout_count += 1
                done_summary = (f"[Success] completed orders id={done.order_id} revenue+={done.price:.2f}")

        # -------------------------
        # 5.Print a status log for that time step
        # -------------------------
        cur_id = active_kitchen.head().order_id if active_kitchen.head() is not None else "-"
        print(f"----- [Cycle: {t}] -----")
        print(f"ORDER SUMMARY: {order_summary}")
        print(f"CUSTOMER ORDER : {arrived_summary}")
        print(f"  --> {moved_summary}")
        print(f"  --> {cook_summary}")
        print(f"  --> {done_summary}")
        print(f"The number of completed orders is : {len(completed_orders)}")
        print()
        input("Press Enter to continue to next step...")

    # Ptint Summary
    print("==============================")
    print("PRINT SUMMARY")
    print("==============================")
    print(f"Total customers processed : {len(completed_orders)}")
    print(f"Total completed orders    : {len(completed_orders)}")
    print(f"Dine-in orders            : {dinein_count}")
    print(f"Takeout orders            : {takeout_count}")
    print(f"Total revenue             : ${revenue:.2f}")


if __name__ == "__main__":
    main()
