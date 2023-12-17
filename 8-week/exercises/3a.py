'''
a) Write a function max_in_tree(t) that returns the maximum value in any binary tree.
'''
from node import Node

def check_max(max_left, max_right, max_in_3):
    if max_right == None and max_left == None:
        return max_in_3
    if max_left != None and max_right != None:
        return max(max_left, max_in_3, max_right)
    if max_left == None and max_right != None:
        return max(max_right, max_in_3)
    if max_right == None and max_left != None:
        return max(max_left, max_in_3)

def max_in_tree(t):
    if t == None:
        return
    if t.left != None or t.right != None:
        max_left = max_in_tree(t.left)
        max_right = max_in_tree(t.right)

        if t.right == None:
            max_in_3 =  max(t.val, t.left.val)
        elif t.left == None:
            max_in_3 = max(t.val, t.right.val)
        else:
            max_in_3 = max(t.val, t.right.val, t.left.val)

        return check_max(max_left, max_right, max_in_3)
        

l = Node(2, Node(4, Node(22), Node(9)), Node(5, Node(10), Node(11)))
r = Node(3, Node(6, Node(12), Node(13)), Node(7, Node(14), Node(15)))
root = Node(1, l, r)

root.display()
print()
print(f" Answer: {max_in_tree(root)}")
print()
root.display()