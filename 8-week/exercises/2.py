'''Write a function mirror(t) that modifies a binary tree, 
flipping it from left to right so that it looks like a mirror image of the original tree.'''

from node import Node

def mirror(t):
    if t == None:
        return
    
    temp = t.left
    t.left = t.right
    t.right = temp

    mirror(t.right)
    mirror(t.left)


l = Node(2)
r = Node(3, Node(6), Node(7))
root = Node(1, l, r)

root.display()
mirror(root)
print("--------")
root.display()