'''
Write a function has_adjacent(n) that takes a pointer to the first Node in a linked list and returns True 
if any two adjacent elements in the list have the same value, otherwise False.
'''

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

tail = Node(4, None)
# n4 = Node(3, tail)
n3 = Node(3, tail)
n2 = Node(2, n3)
head = Node(1, n2)

def has_adjacent(n):
    while n.next != None:
        if n.val == n.next.val:
            return True
        n = n.next
    return False

print(has_adjacent(head))