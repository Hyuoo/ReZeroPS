"""
Solving Date    : 2024.03.22
Solving Time    : -
Title           : K-지폐
tags            : 다이나믹 프로그래밍, 그래프 이론, 데이크스트라, 최단 경로
url             : https://www.acmicpc.net/problem/28131
runtime         : 6080 ms
memory          : 220144 KB
"""

import sys
import heapq

line = lambda:map(int, input().split())

# n개 노드, m개 간선, 총합 k배수
# s -> t
n, m, k = line()
s, t = line()

# init
g = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = line()
    g[u].append([v, w])

# solve
dp = [[1e9 for _ in range(k)] for _ in range(n+1)]
dp[s][0] = 0
q = [[0, s]]

while q:
    now_cost, now = heapq.heappop(q)
    if dp[now][now_cost%k] < now_cost:
        continue
    if now == t and now_cost%k == 0:
        # 조기퇴근
        break

    for nxt, nxt_cost in g[now]:
        dist = now_cost + nxt_cost
        if dp[nxt][dist%k] > dist:
            dp[nxt][dist%k] = dist
            heapq.heappush(q, [dist, nxt])

# output
# print(dp)
print(dp[t][0] if dp[t][0] != 1e9 else "IMPOSSIBLE")

"""
컨닝했다.
컨닝 후 문제 이해 완료

언젠가 비슷한 느낌의 문제를 푼 적 있는 듯 한데 생각이 하나도 안났다.
그래프 마다 홀짝 느낌으로 구분했던 문제

대신 각 노드마다 k개(나머지 개수)만큼 칸이 복제되어있는 느낌으로 풀면 된다.
- [다음노드]의 [다음 거리 % k]경우로 이동.

이 외에는 다익스트라와 동일한 풀이.

- dp라고 하기엔 아닌 것 같다.
"""