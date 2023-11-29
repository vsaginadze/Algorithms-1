''' Write a method that prepends a value to a LinkedList. '''

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
        

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def prepend(self, val):
        node = Node(val, self.head)
        self.head = node        
