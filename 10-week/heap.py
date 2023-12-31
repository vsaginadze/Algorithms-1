class BinaryHeap():
    def __init__(self, a):
        self.a = a # list will hold heap elements
        self.n = len(a)

        for i in range(len(self.a)-1, -1, -1):
            self.down_heap(i)

    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def parent(self, i):
        return (i - 1) // 2

    def up_heap(self, i):
        while i > 0:
            p = self.parent(i)
            if self.a[p] <= self.a[i]:
                break
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i = p
    
    def insert(self, x):
        self.a.append(x)
        print(self.a)
        self.up_heap(len(self.a) - 1)

    def down_heap(self, i):
        while True:
            l, r = self.left(i), self.right(i)

            j = i
            if l < len(self.a) and self.a[j] > self.a[l]:
                j = l

            if r < len(self.a) and self.a[j] > self.a[r]:
                j = r
            
            if i == j:
                break

            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = j
    
    def remove_samllest(self):
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

class Heap:
    def __init__(self, a):
        self.a = a
        self.n = len(a)  # current heap size 

        # Heapify the given array.
        for i in range(self.n - 1, -1, -1):
            self.down_heap(i)
    
    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def parent(self, i):
        return (i - 1) // 2

    def down_heap(self, i):
        while True:
            l, r = self.left(i), self.right(i)
            j = i
            if l < self.n and self.a[l] > self.a[j]:
                j = l
            if r < self.n and self.a[r] > self.a[j]:
                j = r
            if j == i:
                break
            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = j

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
    h = Heap(a)
    h.sort()

a = [3, 4, -1, 2, 4, 5, 8]

heap = Heap(a)

def heapsort(a):
    heap = Heap(a)
    heap.sort()
    print(heap.a)

heapsort(a)