class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Map:
    def __init__(self):
        self.root = None
    
    def contains(self, key):
        node = self.root
        while node != None:
            if node.key == key:
                return node.val
            elif node.key > key:
                node = node.left
            else:
                node = node.right
    
    def add(self, x):
        n = Node(x, None, None)
        p = self.root

        if p == None:
            self.root = n
            return
        
        while True:
            if x == p.val:
                return # already present
            elif x < p.val:
                if p.left == None:
                    p.left = n
                    return
                else:
                    p = p.left
            else:
                if p.right == None:
                    p.right = n
                    return
                else:
                    p = p.right
