"""
Solving Date    : 2023.12.14
Solving Time    : 7m
Title           : 줄 세우기
tags            : 그래프 이론, 위상 정렬, 방향 비순환 그래프
url             : https://www.acmicpc.net/problem/2252
runtime         : 200 ms
memory          : 39584 KB
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
dep = [0 for _ in range(n+1)]
q = set(range(1, n+1))

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    dep[b] += 1
    q.discard(b)

q = list(q)
result = []
while q:
    now = q.pop()
    result.append(now)
    for nxt in g[now]:
        dep[nxt] -= 1
        if dep[nxt] == 0:
            q.append(nxt)

print(*result)

"""
순서가 있지만 모두 순서가 있지는 않다.

순서가 상관없기 때문에
차수가 0인 노드부터 아무 순서대로 위상정렬을 하면 된다.

---
set으로 pop하는 연산이 속도가 엄청 느리다.

set을 그대로 사용했더니 5000ms 이상으로 나왔는데,
set -> list로만 바꿔주니 200ms가 되었다. 
"""