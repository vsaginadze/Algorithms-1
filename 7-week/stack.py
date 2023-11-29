# Array Stack

# class ArrayStack:
#     def __init__(self):
#         self.a = []

#     def is_empty(self):
#         return len(self.a) == 0

#     def push(self, x):
#         self.a.append(x)

#     def pop(self):
#         assert not self.a.is_empty(), "stack is empty"
#         return self.a.pop()


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

# Linked Stack

class LinkedStack:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None

    def push(self, val):
        node = Node(val, self.head)
        self.head = node

    def pop(self):
        assert self.head != None, "stack is empty"
        x = self.head.val
        self.head = self.head.next
        return x