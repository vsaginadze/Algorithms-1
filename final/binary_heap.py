def left(i):
        return 2*i + 1
    
def right(i):
    return 2*i + 2

def parent(i):
    return (i - 1) // 2

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

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

