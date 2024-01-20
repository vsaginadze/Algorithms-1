class Node:
    def __init__(self, key, next):
        self.key = key
        self.next = next

class HashSet:
    def __init__(self, num_buckets):
        self.a = num_buckets * [None]
    
    def contains(self, x):
        i = hash(x) % len(self.a)
        p = self.a[i]
        while p is not None:
            if p.key == x:
                return True
            p = p.next
        return False
    
    def add(self, x):
        if not self.contains(x):
            i = hash(x) % len(self.a)
            self.a[i] = Node(x, self.a[i])
    

    def display(self):
        print("Your hash table is: ", end=" ")
        for bucket in self.a:
            p = bucket
            while p != None:
                print(p.key, end="")
                if p.next != None:
                    print(" -> ", end="")
                else:
                    print(" ", end="")
                p = p.next
        print()
        print()
    
    def remove(self, x):
        i = hash(x) % len(self.a)
        prev = None
        p = self.a[i]

        while p is not None:
            if p.key == x:
                if prev is None:
                    self.a[i] = p.next
                else:
                    prev.next = p.next
                return
            prev = p
            p = p.next

    
