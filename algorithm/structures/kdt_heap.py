class heap:
    def __init__(self):
        self.data = [None]

    def __str__(self):
        return ", ".join(map(str,self.data))

    def insert(self, item):
        pos = len(self.data)
        self.data.append(item)
        while pos>1:
            parent = pos//2
            if self.data[pos] > self.data[parent]:
                self.data[pos], self.data[parent] = self.data[parent], self.data[pos]
                pos = parent
            else:
                break

    def remove(self):
        if len(self.data)<2:
            data = None
        else:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.max_heapify(1)
        return data

    def max_heapify(self, i):
        left = i*2
        right = i*2+1
        smallest = i
        if left < len(self.data) and self.data[i] < self.data[left]:
            smallest = left
        if right < len(self.data) and self.data[left] < self.data[right]:
            smallest = right
        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.max_heapify(smallest)


h = heap()
for i in [10, 20, 5, 6, 30]:
    h.insert(i)
    print(h)
