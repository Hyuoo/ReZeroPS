class circular_queue:

    def __init__(self, n=10):
        self.maxcount = n
        self.data = [0 for _ in range(n)]
        self.count = 0
        self.front = 0
        self.rear = 0

    def __repr__(self, sep=", "):
        result = "["
        f = False
        for i in self.data:
            if f:
                result += sep
            result += str(i)
            f = True
        result += "]"
        return result

    def __str__(self):
        return self.__repr__()

    def size(self):
        return self.count

    def isempty(self):
        return self.count == 0

    def isfull(self):
        return self.count == self.maxcount

    def enq(self, x):
        if self.isfull():
            raise IndexError("Queue is full")
        self.data[self.rear] = x
        self.rear = self.getnext(self.rear)
        self.count += 1

    def deq(self):
        if self.isempty():
            raise IndexError("Queue is empty")
        ret = self.data[self.front]
        self.front = self.getnext(self.front)
        self.count -= 1
        return ret

    def peek(self):
        if self.isempty():
            raise IndexError("Queue is empty")
        return self.data[self.front]

    def getnext(self, n):
        return (n+1)%self.maxcount
