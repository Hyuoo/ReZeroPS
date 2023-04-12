class circular_queue:

    '''
    count를 따로 안만들면
    여럿 head, rear 관계로 연산해야함.
    
    isempty:
        ret head == rear
    isfull:
        ret nextidx(rear) == head
    size:
        if head<rear:
            ret rear - head
        else:
            ret maxsize + rear - head
    '''
    def __init__(self, n=10):
        self.maxsize = n
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
        return self.count == self.maxsize

    def enq(self, x):
        if self.isfull():
            raise IndexError("Queue is full")
        self.rear = self.getnext(self.rear)
        self.data[self.rear] = x
        self.count += 1

    def deq(self):
        if self.isempty():
            raise IndexError("Queue is empty")
        self.front = self.getnext(self.front)
        self.count -= 1
        return self.data[self.front]

    def front(self):
        if self.isempty():
            raise IndexError("Queue is empty")
        return self.data[self.getnext(self.front)]
    
    def back(self):
        if self.isempty():
            raise IndexError("Queue is empty")
        return self.data[self.rear]

    def getnext(self, n):
        return (n+1)%self.maxsize
