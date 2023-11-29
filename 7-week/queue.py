# ArrayQueue

# class ArrayQueue:
#     def __init__(self):
#         self.a = []

#     def is_empty(self):
#         return len(self.a) == 0

#     def enqueue(self, x):
#         self.a.append(x)

#     def dequeue(self):
#         return self.a.pop(0)

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

# Linked Queue

class LinkedQueue:
    def __init__(self):
        self.head = self.tail = None
    
    def isEmpty(self):
        return self.head == None
    
    def enqueue(self, val):
        n = Node(val, self.head)
        if self.head == None: # queue is empty
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n
    
    def dequeue(self):
        assert self.head != None, "queue is empty"
        val = self.head.val
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return val