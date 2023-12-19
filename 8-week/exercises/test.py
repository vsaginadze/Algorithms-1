from node import Node

# def completeTree(h):
#     if h ...
#         return ...
    
#     # completeTree(h)
#     left = Node()
#     right = Node()
#     # completeTree(h)

#     return Node(val, left, right)

def complete(h, depth=0):
    if h == depth:
        return None
    
    left = complete(h, depth+1)    # generate left subtree
    right = complete(h, depth+1)   # generate right subtree

    return Node(depth, left, right)

def mirror(t):
    if t == None:
        return
    
    temp = t.left
    t.left = t.right
    t.right = temp
    
    mirror(t.left)
    mirror(t.right)

    
def findMax(t, m_prev=0):
    if t.left is None and t.right is None:
        return m_prev
    
    max_in_3 = max(t.val, t.right.val, t.left.val)

    if m_prev > max_in_3:
        max_in_3 = m_prev

    return max(findMax(t.right, max_in_3), findMax(t.left, max_in_3))

def find(t, q):
    if t == None:
        return
    
    if t.val == q.val:
        return True
    
    if find(t.right, q) == True:
        return True
    if find(t.left, q) == True:
        return True

l = Node(1, Node(3, Node(7), Node(8, Node(5))))
r = Node(2, Node(-1))
root = Node(0, l, r)
root.display()
print(f"MAX: {find(root, Node(3))}")
root.display()

# def completeTree(h):
#     current_node = Node(0)
#     for i in range(0, h):
#         if current_node.val == i:
#             left = Node(i+1)
#             right = Node(i+1)
#         current_node.left = left
#         current_node.right = right

        
