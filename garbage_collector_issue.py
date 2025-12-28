import gc
import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

# Create nodes
a = Node("A")
b = Node("B")
print(f"Initial ref count for a: {sys.getrefcount(a)}") # Reference from 'a' variable
print(f"Initial ref count for b: {sys.getrefcount(b)}") # Reference from 'b' variable

# Create circular reference
a.next = b
b.next = a
print("\n After creating circular reference:")
print(f"Ref count for a: {sys.getrefcount(a)}") # Increased because b.next points to it
print(f"Ref count for b: {sys.getrefcount(b)}") # Increased because a.next points to it

# Delete references
print("\n Deleting references.....")
del a
del b

# Note: we cant print ref counts here because we cant access a or b anymore!

# Force garbage collection
collected = gc.collect()
print(f"\nGarbage collector collected {collected} objects")