from node import Node

def inorder_traversal(t, a):
    if t is None:
        return
    inorder_traversal(t.left, a)
    a.append(t.value)
    inorder_traversal(t.right, a)

l = Node(5, Node(7), Node(9))
r = Node(15, Node(8))
root = Node(10, l, r)

root.display()
a = []
inorder_traversal(root, a)
print(max([abs(a[i+1]-a[i]) for i in range(len(a)-1)]))