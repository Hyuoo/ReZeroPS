"""
Solving Date    : 2023.10.03
Solving Time    : 20m
Title           : 컴백홈
tags            : 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 깊이 우선 탐색, 백트래킹
url             : https://www.acmicpc.net/problem/1189
runtime         : 88 ms
memory          : 31256 KB
"""

rot = [[1,0],[-1,0],[0,1],[0,-1]]

def scatter(i, j, k):
    if i==0 and j==c-1:
        return 0 if k else 1

    ret = 0
    for x, y in rot:
        ni, nj = i+x, j+y
        if ni<0 or ni>=r or nj<0 or nj>=c or g[ni][nj]==-1:
            continue
        g[ni][nj] = -1
        ret += scatter(ni, nj, k-1)
        g[ni][nj] = 0

    return ret

r, c, k = map(int, input().split())
g = [list(map(lambda x:(0 if x=="." else -1), input())) for _ in range(r)]
# 거의 99%에서 틀린다면 시작점 방문 체크하는지
g[r-1][0] = -1

print(scatter(r-1, 0, k-1))