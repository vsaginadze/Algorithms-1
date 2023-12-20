from node import Node

class TreeSet:
    def __init__(self, node):
        self.node = node

    def contains(self, val, t = -1):
        if t == -1:
            t = self.node

        if t is None:
            return False
        
        if val < t.val:
            return self.contains(val, t.left)
        elif val > t.val:
            return self.contains(val, t.right)
        else:
            return True
    
    def add()
        

right =  Node(20, Node(15), Node(23))
left = Node(8, Node(5), Node(9))
root = Node(10, left, right)
t_set = TreeSet(root)

t_set.node.display()
print(t_set.contains(7))
