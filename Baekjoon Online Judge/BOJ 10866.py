'''
덱 구현 문제. 풀이 시간 : 1h 00m
처음 최대한 직접구현으로 풀려고 본문과 같이 풀었다가 시간초과가 나와서
_____
n = int(input())
dq = []
for _ in range(n):
    i = input().split()
    if i[0] == "push_front":
        dq.insert(0,i[1])
    elif i[0] == "push_back":
        dq.insert(len(dq),i[1])
    elif i[0] == "pop_front":
        print(dq.pop(0) if len(dq) else -1)
    elif i[0] == "pop_back":
        print(dq.pop(-1) if len(dq) else -1)
    elif i[0] == "size":
        print(len(dq))
    elif i[0] == "empty":
        print(0 if len(dq) else 1)
    elif i[0] == "front":
        print(dq[0] if len(dq) else -1)
    elif i[0] == "back":
        print(dq[-1] if len(dq) else -1)
> 이 코드로 바꿔서 풀었는데 또 똑같이 시간초과가 나와서
질문을 찾아보니 입력이 많아서 input()속도가 느려서 그렇단다.
import sys 하고
input() 만 sys.stdin.readline() 로 고쳐주니 두 코드 모두 통과.
'''

import sys
class Node:
    def __init__(self,val=None,front=None,back=None):
        self.value=val
        self.front=front
        self.back=back
class deque:
    def __init__(self):
        self.head = None
        self.rear = None
        self.qsize = 0
    def dqsize(self):
        return self.qsize
    def empty(self):
        if self.qsize==0:
            return 1
        else:
            return 0
    def push_front(self,x):
        if self.head == None:
            self.head = Node(x)
            self.rear = self.head
        else:
            new_node = Node(x,None,self.head)
            self.head.front = new_node
            self.head = new_node
        self.qsize += 1
    def push_back(self,x):
        if self.rear == None:
            self.rear = Node(x)
            self.head = self.rear
        else:
            new_node = Node(x,self.rear,None)
            self.rear.back = new_node
            self.rear = new_node
        self.qsize += 1
    def pop_front(self):
        if self.empty():
            return -1
        val = self.head.value
        del_node = self.head
        if self.head.back:
            self.head = self.head.back
            self.head.front=None
        else:
            self.head = None
            self.rear = None
        self.qsize -= 1
        del del_node
        return val
    def pop_back(self):
        if self.empty():
            return -1
        val = self.rear.value
        del_node = self.rear
        if self.rear.front:
            self.rear = self.rear.front
            self.rear.back=None
        else:
            self.rear = None
            self.head = None
        self.qsize -= 1
        del del_node
        return val
    def front(self):
        if self.empty():
            return -1
        return self.head.value
    def back(self):
        if self.empty():
            return -1
        return self.rear.value
    def print_all(self):
        if self.head==None:
            print("[None]")
        else:
            tmp = self.head
            while(tmp):
                print(f"[{tmp.front}:{tmp.value}:{tmp.back}]", end="-")
                tmp = tmp.back
            print()
n = int(sys.stdin.readline())
dq = deque()
for _ in range(n):
    i = sys.stdin.readline().split()
    #print(i,":")
    if i[0] == "push_front":
        dq.push_front(i[1])
    elif i[0] == "push_back":
        dq.push_back(i[1])
    elif i[0] == "pop_front":
        print(dq.pop_front())
    elif i[0] == "pop_back":
        print(dq.pop_back())
    elif i[0] == "size":
        print(dq.dqsize())
    elif i[0] == "empty":
        print(dq.empty())
    elif i[0] == "front":
        print(dq.front())
    elif i[0] == "back":
        print(dq.back())
    #dq.print_all()
