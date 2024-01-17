class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedStack:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def push(self, val):
        node = Node(val, self.head)
        self.head = node
    
    def pop(self):
        assert not self.is_empty(), "stack is empty"
        val = self.head.val
        self.head = self.head.next
        return val