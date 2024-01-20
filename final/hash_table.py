class Node:
    def __init__(self, key, next):
        self.key = key
        self.next = next

class HashTable:
    def __init__(self, num_buckets):
        self.a = [None] * num_buckets
    
    def contains(self, x):
        i = hash(x) % len(self.a)
        p = self.a[i]

        while p != None:
            if p.key == x:
                return True
            p = p.next
        return False
    
    def add(self, x):
        if not self.contains(x):
            i = hash(x) % len(self.a)
            self.a[i] = Node(x, self.a[i])