#https://school.programmers.co.kr/learn/courses/30/lessons/43164
from collections import defaultdict

def solution(tickets):
    g = defaultdict(list)
    for src, dest in tickets:
        g[src].append(dest)
    for i in g.keys():
        g[i].sort(reverse=True)
        
    s = ["ICN"]
    path = []
    while s:
        now = s[-1]
        if g[now] and g[now][-1]:
            s.append(g[now].pop())
        else:
            path.append(s.pop())
    
    return path[::-1]
'''
여행경로

한붓그리기가 반드시 가능하다는 것을 이용해
탐색이 막힌 경로는 맨 뒤에 왔어야 할 곳이므로
위와같이 구현이 가능.
'''
