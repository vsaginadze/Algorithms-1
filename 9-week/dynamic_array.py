class DynamicArray:
    def __init__(self):
        self.a = 10 * [None]
        self.n = 0
    
    def resize(self):
        b = 2 * (len(self.a)) * [None]
        for k in range(self.n):
            b[k] = self.a[k]
        self.a = b

    def add(self, x):
        if self.n >= len(self.a):
            self.resize()
        self.a[self.n] = x
        self.n += 1
    
    def set(self, i, x):
        if i >= self.n:
            return "Error"
        self.a[i] = x
    
    def get(self, i):
        return self.a[i]