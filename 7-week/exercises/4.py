'''
Write a method that deletes the first node (if any) in a LinkedList
'''

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def delete_first(self):
        assert self.head != None, "linked list is empty"
        self.head = self.head.next
    
    def print(self):
        n = self.head
        while n != None:
            print(n.val, end = " ")
            n = n.next
        print()

tail = Node(4, None)
n4 = Node(3, tail)
n3 = Node(3, tail)
n2 = Node(2, n3)
head = Node(1, n2)

list = LinkedList(head)
