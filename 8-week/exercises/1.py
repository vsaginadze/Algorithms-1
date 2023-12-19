'''
Write a function completeTree(h) that builds a complete binary tree of height h. 
Every node's value should be that node's depth.
'''

from node import Node

def completeTree(h, d = 0):
    if h == d: return None
    
    l = completeTree(h, d + 1)
    r = completeTree(h, d + 1)

    return Node(d, l, r)


node = completeTree(4)
node.display()

