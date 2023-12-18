class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

l = Node(7, None, None)
r = Node(5, None, None)
root = Node(4, l, r) 

def size(n):
    if n == None:
        return 0
    
    return 1 + size(n.left) + size(n.right)

print(size(root))