"""
Solving Date    : 2023.10.19
Solving Time    : 13m
Title           : 헌내기는 친구가 필요해
tags            : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
url             : https://www.acmicpc.net/problem/21736
runtime         : 692 ms
memory          : 54328 KB
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
q = []
campus = []

for i in range(n):
    tmp = list(input())
    if not q:
        for j in range(m):
            if tmp[j]=="I":
                q.append([i, j])
                tmp[j] = "X"
    campus.append(tmp)

r = [[1, 0], [-1, 0], [0, 1], [0, -1]]
p = 0

while q:
    x, y = q.pop()

    for i, j in r:
        nx = x+i
        ny = y+j
        if nx>=0 and nx<n and ny>=0 and ny<m and campus[nx][ny]!="X":
            if campus[nx][ny]=="P":
                p += 1
            campus[nx][ny] = "X"
            q.append([nx, ny])

print(p if p else "TT")

"""
단순히 전체 탐색하면서 특정조건("P") 카운트
어차피 모든 공간을 탐색할거라 깊이/너비 관계없다.

---
정수로 안바꾸고 문자열로 연산하는게 더 빠르네
"""