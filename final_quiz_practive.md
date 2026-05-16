# Q1

Q1 Hash Table

```
There are two main ways to implement a hash table:

1. Separate Chaining
Store multiple elements in the same bucket using a linked list.
Collision → add the new element to the linked list.
Pros: simple, can store more elements than buckets
Cons: extra memory usage, slower due to linked list traversal

2. Open Addressing
Store all elements directly in the array and probe for an empty slot.

Linear Probing:
Check next slot sequentially (+1)
Problem: primary clustering

Quadratic Probing:
Check using square jumps (+1², +2²...)
Reduces clustering but still has secondary clustering

Double Hashing:
Use a second hash function for step size
Best at avoiding clustering but more complex
```

Q2 Dijkstra
```
No, we cannot use Dijkstra’s Algorithm.
This graph has a negative edge (-300).
Dijkstra assumes once a shortest path is finalized, it will not be updated again.
With negative edges, a shorter path may be found later, so Dijkstra can return the wrong answer.
```
