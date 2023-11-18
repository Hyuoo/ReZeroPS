"""
Solving Date    : 2023.09.16
Solving Time    : -
Title           : 웜홀
tags            : 그래프 이론, 벨만-포드
url             : https://www.acmicpc.net/problem/1865
runtime         : 2252 ms
memory          : 31256 KB
"""

import sys
input = sys.stdin.readline

# INF = 1e9

for tc in range(int(input())):
    n, m, w = map(int, input().split())
    edge = []

    for i in range(m+w):
        s, e, t = map(int, input().split())
        if i<m:
            edge.append([s,e,t])
            edge.append([e,s,t])
        else:
            edge.append([s,e,-t])

    # INF로 안하고 0으로 해도 됨.
    # dist = [INF for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]
    # dist[0] = 0
    f = False
    for i in range(n):
        for src, dest, k in edge:
            if dist[dest] > dist[src] + k:
                dist[dest] = dist[src] + k
                if i == n-1:
                    f = True

    print("YES" if f else "NO")

"""
벨만포드 알고리즘 문제.

푼거 한번 더 풀기

아예 간선만 다 체크를 하면 되기때문에
간선 단위로만 저장하고 싹 다 순회하는 방식으로
코드가 간결해짐.

n-1만큼에서 체크해도되고,
이후 한번 더 순회해서 체크해도 되고

근데 왜 난 시간이 안줄어드냐
"""