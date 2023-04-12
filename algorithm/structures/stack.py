class Stack:
    def __init__(self, n=100):
        self.stack = [0 for _ in range(n)]
        self.n = n
        self.maximum = n
        self.top = -1

    def is_empty(self):
        return True if self.top == -1 else False

    def is_full(self):
        return True if self.top+1 == self.maximum else False

    def size(self):
        return self.top + 1

    def push(self, data):
        if self.is_full():
            raise IndexError("Stack is full")
        self.top += 1
        self.stack[self.top] = data
        return 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        ret = self.peek()
        self.top -= 1
        return ret

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[self.top]
