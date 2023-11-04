"""
Solving Date    : 2023.10.30
Solving Time    : 14m
Title           : Strongly Connected Component
tags            : 그래프 이론, 강한 연결 요소
url             : https://www.acmicpc.net/problem/2150
runtime         : 172 ms
memory          : 36668 KB
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(n):
    global id
    roots[n] = (id:=id+1)
    s.append(n)

    p = roots[n]
    for nxt in g[n]:
        if roots[nxt] == 0:
            p = min(p, dfs(nxt))
        elif not fin[nxt]:
            p = min(p, roots[nxt])

    if p == roots[n]:
        scc_tmp = []
        while 1:
            t = s.pop()
            scc_tmp.append(t)
            fin[t] = True
            if t == n:
                break
        scc.append(scc_tmp)

    return p

v, e = map(int, input().split())
g = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    g[a].append(b)

id = 0
roots = [0 for _ in range(v+1)]
fin = [False for _ in range(v+1)]
scc = []
s = []

for i in range(1, v+1):
    if roots[i] == 0:
        dfs(i)

print(len(scc))
for i in sorted(map(lambda x:sorted(x)+[-1], scc)):
    print(*i)

"""
이름부터 SCC 알고리즘 정석 문제.

블로그에서 SCC 알고리즘을 보고,
구현 해보고 나서 바로 푼 문제.

그래서 풀이 시간은 의미가 없는듯.
"""