# Array Stack

class ArrayStack:
    def __init__(self):
        self.a = []

    def is_empty(self):
        return len(self.a) == 0

    def push(self, x):
        self.a.append(x)

    def pop(self):
        assert not self.a.is_empty(), "stack is empty"
        return self.a.pop()

