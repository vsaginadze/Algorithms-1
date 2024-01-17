class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l = Node(12, Node(4), Node(6))
r = Node(10, Node(5), Node(8))
root = Node(6, l, r)

