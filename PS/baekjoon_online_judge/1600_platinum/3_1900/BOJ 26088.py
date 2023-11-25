"""
Solving Date    : 2023.11.25
Solving Time    : 1h 13m
Title           : 트리 다듬기
tags            : 자료 구조, 그래프 이론, 그리디 알고리즘, 그래프 탐색, 트리, 깊이 우선 탐색, 우선순위 큐
url             : https://www.acmicpc.net/problem/26088
runtime         : 520 ms
memory          : 80848 KB
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

def far(x):
    visit = {x}
    q = deque([x])
    while q:
        now = q.popleft()
        for nxt in g[now]:
            if nxt not in visit:
                visit.add(nxt)
                q.append(nxt)
    return now


def get_subtree_length(x):
    f = 0
    l = []

    for nxt in g[x]:
        if nxt not in sub_visit:
            f = 1
            sub_visit.add(nxt)
            l.extend(get_subtree_length(nxt))

    if f:
        l.sort(reverse=True)
        l[0] += 1
        return l
    else:
        return [1]


n, k = map(int, input().split())
g = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

idx = far(1)
sub_visit = {idx}
ls = get_subtree_length(idx)

# print(far(1), ls)
print(sum(ls[:k+1])-1)

"""
2022 Sogang Programming Contest > Master (Open) H번

트리를 k번 끊고 연결해서 최대 길이의 지름을 만드는 문제.

서강대 해설지를 사전에 한번 본 뒤,
G4 1967, G2 1167 두 문제를 먼저 풀고 풀었다.

1. 먼저 트리의 지름이 될 수 있는 한 점을 찾고(DFS/BFS)
2. 지름을 포함 한 서브트리의 길이를 모두 구함
    - 단 이 코드에서는 지름(최장길이)은 자기 노드까지 더해져있기 때문에 -1을 해줘야 한다. 
3. 지름 + 최대 k개의 길이를 합침.
"""