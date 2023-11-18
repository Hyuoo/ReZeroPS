"""
Solving Date    : 2023.11.04
Solving Time    : 1h 23m
Title           : 도미노
tags            : 그래프 이론, 위상 정렬, 강한 연결 요소, 방향 비순환 그래프
url             : https://www.acmicpc.net/problem/4196
runtime         : 1400 ms
memory          : 73492 KB
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x):
    global id, group
    ids[x] = (id:=id+1)
    s.append(x)

    p = ids[x]
    for nxt in g[x]:
        if ids[nxt] == 0:
            p = min(p, dfs(nxt))
        elif not fin[nxt]:
            p = min(p, ids[nxt])

    if p == ids[x]:
        tmp = []
        group += 1
        while s:
            t = s.pop()
            tmp.append(t)
            fin[t] = group
            if x == t:
                break
        scc.append(tmp)

    return p

for tc in range(int(input())):
    n, m = map(int, input().split())
    g = [[] for _ in range(n+1)]
    ids = [0 for _ in range(n+1)]
    fin = [0 for _ in range(n+1)]
    scc = []
    s = []
    id = 0
    group = 0

    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)

    for i in range(1, n+1):
        if ids[i] == 0:
            dfs(i)

    dep = [0 for _ in range(group)]
    scc_g = [[] for _ in range(group)]
    for i in range(group):
        for node in scc[i]:
            for arw in g[node]:
                if fin[arw]-1 != i:
                    dep[fin[arw]-1] = 1

    print(group-sum(dep))

"""
우왕 첫 플레4 솔브

처음에 그냥 단순 위상정렬이랑 무슨 차이지? 하다가.
- 사이클이 있는 경우 위상정렬만으로는 해결 불가능.
- 반대로 사이클이 없는 경우 SCC만으로는 해결 불가능.

아 근데 위상정렬 식으로 먼저 체크하고
이후에 SCC로 어케어케 하면 될 것 같은데 하다가
머리 굳어서 그대로 포기

그냥 단순하게 풀기로 함.
풀이:
1. 그래프를 SCC알고리즘으로 연결그룹으로 만든다.
    - 각 그룹으로 다시 간소화된 그래프를 형성
2. 1에서 생성한 그래프로 의존성있는 그룹을 세어준다.
    - 단 같은 그룹 내의 노드를 가리키지 않는 경우만
3. return (전체 그룹 수 - 의존성 있는 그룹 수)
"""