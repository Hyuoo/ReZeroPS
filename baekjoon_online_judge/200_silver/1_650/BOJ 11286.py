import sys
input = sys.stdin.readline
class heap:
    def __init__(self, l:list = []):
        self.h = l
        self.size = len(l)
        if self.size>1:
            self.heapify()

    def __str__(self):
        if self.isempty():
            return ""
        return ("["+", ".join(map(str,self.h))+"]")

    def push(self, x):
        self.h.append(x)
        self.size += 1
        self.shiftdown(self.size-1)

    def pop(self):
        if self.isempty():
            return 0
        self.size -= 1
        retitem = self.h[0]
        self.h[0] = self.h[self.size]
        self.h[self.size] = retitem
        self.shiftup(0)
        return self.h.pop()

    def isempty(self):
        return self.size==0

    def heapify(self):
        for i in range(self.size,0,-1):
            self.shiftdown(i)

    def shiftdown(self,pos):
        if pos >= self.size:
            return
        newitem = self.h[pos]
        while pos > 0:
            parentpos = (pos-1)>>1
            parent = self.h[parentpos]
            if abs(parent) > abs(newitem) or (abs(parent)==abs(newitem) and parent>newitem):
                self.h[pos] = parent
                pos = parentpos
                continue
            break
        self.h[pos] = newitem

    def shiftup(self,pos):
        newitem = self.h[pos]
        childpos = pos*2+1
        while childpos<self.size:
            if childpos+1 < self.size\
                    and (abs(self.h[childpos])>abs(self.h[childpos+1])\
                        or (abs(self.h[childpos])==abs(self.h[childpos+1])\
                        and self.h[childpos]>self.h[childpos+1])):
                childpos+=1
            if (abs(newitem)>abs(self.h[childpos]))\
                    or (abs(newitem)==abs(self.h[childpos])\
                    and newitem>self.h[childpos]):
                self.h[pos] = self.h[childpos]
                pos = childpos
                childpos = pos*2+1
                continue
            break
        self.h[pos] = newitem

h = heap()
for _ in range(int(input())):
    a = int(input())
    if a==0:
        print(h.pop())
    else:
        h.push(a)
