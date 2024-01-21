class BinaryHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def left_child(self, i):
        return 2*i + 1
    
    def right_child(self, i):
        return 2*i + 2
    
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
        self.up_heap(len(self.a) - 1)

    def down_heap(self, i):
        while True:
            l, r = self.left(i), self.right(i)

            j = i
            if l < len(self.a[l]) and self.a[l] < self.a[j]:
                j = l
            if r < len(self.a[r]) and self.a[r] < self.a[j]:
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