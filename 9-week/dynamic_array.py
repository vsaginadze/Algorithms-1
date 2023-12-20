class DynArray:
    def __init__(self):
        self.a = 10 * [None]
        self.n = 0 # current number of items
    
    def add(self, x):
        if self.n >= len(self.a):
            b = (len(self.a) * 2) * [None]
            for i in range(len(self.a)):
                b[i] = self.a[i]
            self.a = b
        self.a[self.n] = x
        self.n += 1
    
    def get(self, i):
        return self.a[i]

    def set(self, i, x):
        self.a[i] = x

d = DynArray()
for i in range(10):
    d.add(i * i)

print(d.n)