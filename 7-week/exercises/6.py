'''
Write a function split() that takes a pointer to the the first Node in a linked list and splits the list
into two linked lists of roughly equal size. Return a pair containing these lists. 
The elements in the returned lists may appear in any order.
'''

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def print(self):
        n = self.head
        while n != None:
            print(n.val, end = " ")
            n = n.next
        print()
    
    def get_size(self):
        assert self.head != None, "linked list empty"
        size = 0
        current = self.head
        while current.next != None:
            current = current.next
            size += 1
        
        return size
    
    def split(self):
        l1 = LinkedList(self.head)

        size = self.get_size()
        size //= 2
        current = self.head
        while size != 0:
            size -= 1
            current = current.next
        l2 = LinkedList(current.next)
        current.next = None

        return (l1, l2)


tail = Node(4, None)
n4 = Node(3, tail)
n3 = Node(3, n4)
n2 = Node(2, n3)
head = Node(1, n2)

list = LinkedList(head)