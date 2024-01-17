from pair import Pair

class Map:
    def __init__(self):
        self.root = None
    
    def display(self):
        self.root.display()
    
    def lookup(self, key):
        p = self.root
        while p is not None:
            if p.key == key:
                return p.value
            elif key < p.key:
                p = p.right
            else:
                p = p.left
        
        return False

    def set(self, key, value):
        if self.lookup(key) == value:
            print("Pair already exists")
            return
        
        pair = Pair(key, value)
        p = self.root

        if p is None:
            self.root = pair
            return
        
        while True:
            if key == p.key:
                p.value = value
                return
            elif key < p.key:
                if p.left:
                    p = p.left
                else:
                    p.left = pair
                    return
            else:
                if p.right:
                    p = p.right
                else:
                    p.right = pair
                    return

my_map = Map()

my_map.set(10, "ten")
my_map.set(11, "eleven")
my_map.set(9, "nine")
my_map.set(12, "twelve")
my_map.set(0, "zero")
my_map.set(10, "Ten")
my_map.set(8, "RVUA")

my_map.display()