class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class TreeSet:
    def __init__(self):
        self.root = None
    
    def contains(self, x):
        node = self.root
        while node != None:
            if node.val == x:
                return True
            elif node.val > x:
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
