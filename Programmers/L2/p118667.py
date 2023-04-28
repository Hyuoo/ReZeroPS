#https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque
def solution(que1, que2):
    q1 = deque(que1)
    q2 = deque(que2)
    s = sum(que1)-sum(que2)
    tok = len(que1)*3
    count = 0
    while tok:
        if s:
            if s>0:
                s-=q1[0]*2
                q2.append(q1.popleft())
            else:
                s+=q2[0]*2
                q1.append(q2.popleft())
            count+=1
        else:
            break
        tok-=1
    else:
        count = -1
    return count
