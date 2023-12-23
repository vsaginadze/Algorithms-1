'''
b) Modify the function to be more efficient if the input tree is known to be a binary search tree.
'''

from node import Node

def max_in_tree(t):
    while t:
        if t.right:
            t = t.right
        else:
            return t.value


root = Node(5, Node(3, Node(2), Node(4)))

l = Node(3, Node(2), Node(6, Node(5), Node(8)))
r = Node(20, Node(15, None, Node(18)), Node(23))
root = Node(10, l, r)

root.display()
print()
print(f" Answer: {max_in_tree(root)}")
print()
root.display()