class Node():
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

class HashDictionary():
    def __init__(self, num_buckets):
        self.a = num_buckets * [None]

    def lookup(self, key):
        i = hash(key) % len(self.a)
        p = self.a[i]
        while p != None:
            if p.key == key:
                return p.value
            p = p.next
        return False

    def add(self, key, value):
        if not self.lookup(key):
            i = hash(key) % len(self.a)
            self.a[i] = Node(key, value, self.a[i])
    
    def remove(self, key):
        i = hash(key) % len(self.a)
        p = self.a[i]
        
        if p.key == key:
            self.a[i] = p.next
            return
        
        p = p.next
        while p.next != None:
            if p.key == key:
                self.a[i] = p.next
                return
            p = p.next

        return f"No such keu as {key}"

    def display(self):
        print("Your hash table is:", end=" ")
        for bucket in self.a:
            p = bucket
            while p != None:
                print(f"|{p.key} <-> {p.value}|", end="->" if p.next else " ")
                p = p.next
        print()
        print()
    


dic = HashDictionary(10)

dic.add("cat", "animal")
dic.add("hello", "world")
dic.add("foo", "bar")
dic.add("apple", "fruit")
dic.add("carrot", "vegetable")


dic.display()

dic.remove("apple")
dic.remove("cat")
dic.remove("foo")

dic.display()