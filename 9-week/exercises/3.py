class Node:
    def __init__(self, key, next):
        self.key = key
        self.next = next

class HashSet:
    def __init__(self, num_buckets):
        # each array element is the head of a linked list of Nodes
        self.a = num_buckets * [None]
        self.n = 0

    def resize(self):
        b = 2 * (len(self.a)) * [None]
        for k in range(self.n):
            b[k] = self.a[k]
        self.a = b

    def contains(self, x):
        i = hash(x) % len(self.a)     # hash bucket index
        p = self.a[i]
        while p != None:
            if p.key == x:
                return True
            p = p.next
        return False

    def add(self, x):
        if not self.contains(x):
            if self.n >= len(self.a): self.resize()
            
            i = hash(x) % len(self.a)
            self.a[i] = Node(x, self.a[i])   # prepend to hash chain
            self.n += 1

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


