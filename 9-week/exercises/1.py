import sys
import os
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from hash_table import HashSet

class HashSet(HashSet):
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

hash_set = HashSet(10)


hash_set.add("hello")
hash_set.add("world")
hash_set.add("foo")
hash_set.add("bar")


hash_set.display()

hash_set.remove("hello")

hash_set.display()