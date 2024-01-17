from pair import Pair

class Map:
    def __init__(self):
        self.root = None
    
    def display(self):
        self.root.display()
    
    def lookup(self, key):
        pair = self.root
        while pair is not None:
            if pair.key == key:
                return pair.value
            elif pair.key > key:
                pair = pair.left
            else:
                pair = pair.right
        
        return False

    def set(self, key, value):
        if self.lookup(key):
            print(f"{key} Already Exists")
            return
        
        pair = Pair(key, value)
        p = self.root

        if p is None:
            self.root = pair
            return

        while True:
            if key == p.key:
                p.value = value
                return # update the value and exit
            elif key < p.key:
                if p.left:
                    p = p.left
                else:
                    p.left = pair
                    return # insert the pair if LEFT DNE
            else:
                if p.right:
                    p = p.right
                else:
                    p.right = pair
                    return # insert the pair if RIGHT DNE

my_map = Map()

my_map.set(10, "ten")
my_map.set(11, "eleven")
my_map.set(9, "nine")
my_map.set(12, "twelve")
my_map.set(0, "zero")
my_map.set(10, "Ten")

my_map.display()