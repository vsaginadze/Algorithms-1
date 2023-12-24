class Node:
    def __init__(self, key, next):
        self.key = key
        self.next = next

class HashSet:
    def __init__(self, num_buckets):
        # each array element is the head of a linked list of Nodes
        self.a = num_buckets * [None]

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
            i = hash(x) % len(self.a)
            self.a[i] = Node(x, self.a[i])   # prepend to hash chain
    
    def remove(self, key):
        if not self.contains(key):
            return f"{key} Does not exist"
        else:
            i = hash(key) % len(self.a)
            p = self.a[i]
            if p.key == key:
                self.a[i] = p.next
            else:
                while p.next.key != key:
                    p = p.next
                p.next = p.next.next

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

hash_set = HashSet(10)

hash_set.add("hello")
hash_set.add("world")
hash_set.add("python")
hash_set.add("programming")
hash_set.add("data")
hash_set.add("structures")

hash_set.display()

hash_set.remove("hello")
hash_set.remove("world")
hash_set.display()