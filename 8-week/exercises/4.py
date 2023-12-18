'''
Write a function isAncestor(p, q) that takes pointers to two nodes 
p and q in a binary tree and returns true if p is an ancestor of q.
'''

from node import Node

def isAncestor(p, q):
    if p.right == q or p.left == q:
        return True
    
    if p.right:
        if isAncestor(p.right, q):
            return True
    if p.left:
        if isAncestor(p.left, q):
            return True
    

node = Node(12)
l = Node(2, Node(4), Node(6, node, None))
r = Node(3)
root = Node(1, l, r)

root.display()
x = isAncestor(root, node)
print(x)