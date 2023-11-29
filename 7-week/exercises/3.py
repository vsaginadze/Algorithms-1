'''
Write a method that appends a value to a LinkedList.
'''

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def append(self, val):
        node = Node(val, None)
        n = self.head
        while n.next != None:
            n = n.next
        n.next = node
    
    def print(self):
        n = self.head
        while n != None:
            print(n.val, end = " ")
            n = n.next

tail = Node(4, None)
n4 = Node(3, tail)
n3 = Node(3, tail)
n2 = Node(2, n3)
head = Node(1, n2)

list = LinkedList(head)

list.append(5)

list.print()
