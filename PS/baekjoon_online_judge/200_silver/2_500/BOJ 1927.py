import sys
input = sys.stdin.readline

class heap:
    def __init__(self):
        self.h = [-1 for _ in range(100001)]
        self.size = 0

    def push(self,x):
        self.size+=1
        self.h[self.size] = x
        idx=self.size
        while idx>0 and self.h[idx]<self.h[idx//2]:
            tmp = self.h[idx]
            self.h[idx] = self.h[idx//2]
            self.h[idx//2] = tmp
            idx //= 2

    def pop(self):
        if self.isempty():
            return 0
        else:
            ret = self.h[1]
            self.h[1] = self.h[self.size]
            self.size-=1
            idx = 1
            while 1:
                m_idx = idx
                if idx*2<=self.size and self.h[idx*2]<self.h[m_idx]:
                    m_idx = idx*2
                if idx*2+1<=self.size and self.h[idx*2+1]<self.h[m_idx]:
                    m_idx = idx*2+1
                if m_idx!=idx:
                    tmp = self.h[idx]
                    self.h[idx] = self.h[m_idx]
                    self.h[m_idx] = tmp
                    idx = m_idx
                else:
                    break
            return ret
    
    def isempty(self):
        return self.size==0

h = heap()
for _ in range(int(input())):
    x = int(input())
    if x:
        h.push(x)
    else:
        print(h.pop())
