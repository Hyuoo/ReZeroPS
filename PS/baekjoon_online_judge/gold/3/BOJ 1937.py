"""
Solving Date    : 2024.01.08
Solving Time    : 20m
Title           : 욕심쟁이 판다
tags            : 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 깊이 우선 탐색
url             : https://www.acmicpc.net/problem/1937
runtime         : 1412 ms
memory          : 77668 KB
"""

import sys
input = sys.stdin.readline
import heapq

n = int(input())
forest = [[0 for _ in range(n+2)]for _ in range(n+2)]
result = [[0 for _ in range(n+2)]for _ in range(n+2)]

q = []
for i in range(n):
    tmp = [*map(int, input().split())]
    forest[i+1] = [0]+tmp+[0]
    for j, v in enumerate(tmp):
        heapq.heappush(q, [v, i+1, j+1])

r = [[0, 1], [0, -1], [1, 0], [-1, 0]]
while q:
    v, i, j = heapq.heappop(q)
    result[i][j] = max([result[i+x][j+y] for x, y in r if forest[i+x][j+y]<v]+[0]) + 1

print(max(map(max, result)))

"""
dfs문제이지만, 구글에 lis로 검색했드니 나온 문제여서 lis로 풀었다.

1차원 배열의 lis 전략을 그대로 써서
작은 숫자부터, +1씩 더해주는 방법으로 풀었다.

2차원 배열이라 한번에 전체 구간을 검사하기가 까다로워서
주변 십자에서 최댓값+1을 했다.
- 이 과정에서 "같은" 수를 가진 칸을 구분하기 위해서 원래 값이 들어있는 배열을 만들어줌.
(같은 값도 이동하면 2차원 배열하나 덜 만들어도 되는데..)
"""