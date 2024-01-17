class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedQueue:
    def __init__(self):
        self.head = self.tail = None
    
    def is_empty(self):
        return self.head == None

    def enqueue(self, val):
        node = Node(val)
        
        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def dequeue(self):
        assert not self.is_empty(), "queue is empty"
        val = self.head.val
        self.head = self.head.next
        
        if self.head == None:
            self.tail = None
        return val