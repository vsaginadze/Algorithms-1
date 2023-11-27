# Node

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def list_len(head):
    n = head
    count = 0

    while n != None:
        n = n.next
        count += 1
    
    return count

def list_sum(head):
    n = head
    sum = 0

    while n != None:
        sum += n.val
        n = n.next
    
    return sum

def list_1_to_n(n):
    head = None
    for i in range(n, 0, -1):
        p = Node(i, head)
        head = p

    return head
