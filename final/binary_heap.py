def left(i):
        return 2*i + 1
    
def right(i):
    return 2*i + 2

def parent(i):
    return (i - 1) // 2

class BinaryHeap:
    def __init__(self, a):
        self.a = a
        self.n = len(self.a)

        # heapify the given array
        for i in range(self.n - 1, -1, -1):
            self.down_heap(i)

    def up_heap(self, i):
        while i > 0:
            p = parent(i)
            if self.a[p] <= self.a[i]:
                break
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i = p
    
    def insert(self, x):
        self.a.append(x)
        self.up_heap(len(self.a) - 1)

    def down_heap(self, i):
        while True:
            l, r = left(i), right(i)

            j = i
            if l < self.n and self.a[l] < self.a[j]:
                j = l
            if r < self.n and self.a[r] < self.a[j]:
                j = r
            
            if j == i:
                break
            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = j
            
    def remove_smallest(self):
        x = self.a[0]
        self.a[0] = self.a.pop()
        self.down_heap(0)
        return x
    
    def remove_largest(self):
        x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n -= 1
        self.down_heap(0)
        return x
    
    def sort(self):
        while self.n > 0:
            x = self.remove_largest()
            self.a[self.n] = x

def heapsort(a):
    h = BinaryHeap(a)
    h.sort()

a = [3, 2, 5, 1, 4, 7, 0]
heapsort(a)
print(a)
