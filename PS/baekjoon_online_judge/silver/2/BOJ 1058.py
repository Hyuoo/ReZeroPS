"""
Solving Date    : 2024.09.09
Solving Time    : 13m
Title           : 친구
tags            : 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 최단 경로, 플로이드–워셜
url             : https://www.acmicpc.net/problem/1058
runtime         : 36 ms
memory          : 31120 KB
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
ar = [input() for _ in range(n)]
ans = 0

for i, q in ((i, [j for j in range(n) if ar[i][j]=="Y"]) for i in range(n)):
    tot = set([i for nxt in q for i in range(n) if ar[nxt][i]=="Y"] + q) - {i}
    ans = max(ans, len(tot))

print(ans)

"""
첫 풀이에서 (큐+2칸인접)까지 조회하는걸 카운트 써서 체크했으나,
처음 순회 할 큐를 초기화 할 때, (0칸인접(자신) -> 1칸인접)으로 하여 1칸인접만 체크하도록 수정
-> 방문체크 필요 X, 몇칸인지 체크 필요 X

- set을 사용하여 방문체크 + 전체 개수 한번에 체크
- 자기자신이 포함되는 경우와 안되는 경우가 혼재하여 -{i}로 차집합 함
"""