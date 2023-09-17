"""
Solving Date    : 2023.09.16
Solving Time    : 42m
Title           : 웜홀
tags            : 그래프 이론, 벨만-포드
url             : https://www.acmicpc.net/problem/1865
runtime         : 2356 ms
memory          : 31256 KB
"""

import sys
input = sys.stdin.readline

INF = 1e9

for tc in range(int(input())):
    n, m, w = map(int, input().split())
    node = [[] for _ in range(n)]

    for i in range(m+w):
        s, e, t = map(int, input().split())
        s -= 1
        e -= 1
        if i<m:
            node[s].append([e,t])
            node[e].append([s,t])
        else:
            node[s].append([e,-t])

    dist = [INF for _ in range(n)]
    dist[0] = 0
    for _ in range(n):
        for src in range(n):
            for dest, k in node[src]:
                if dist[dest] > dist[src] + k:
                    dist[dest] = dist[src] + k

    f = False
    for src in range(n):
        for dest, k in node[src]:
            if dist[dest] > dist[src] + k:
                f = True
                break
        if f:
            break

    print("YES" if f else "NO")

"""
벨만포드 알고리즘 문제.

어느 위치든 사이클이 존재하기만 하면된다.
근데 벨만포드를 제대로 이해 못한 상태.

아무튼 이걸 풀 때 이해한 개념은
    '충분히' 최단거리를 갱신했는데도
    최단거리가 '또' 갱신되면 무한싸이클이다.

아니면 각 최단거리들이고

+ for (m+w) 보다
    for (m) for (w) 가 더 빠르다.


이후 추가적인 코멘트.
INF, 시작점 0초기화 등은 안해도 정답.
    오히려 _탐색중_ INF제외 해버리면 실패
왜냐하면
    사이클 발생 X시 최단거리를 구하는 것도 아니고
    시작점에서 갈 수 있는 범위에서 사이클을 찾는것도 아니고
그래서 사이클 유무만 체크하면 되기 때문에 필요없다. 
"""