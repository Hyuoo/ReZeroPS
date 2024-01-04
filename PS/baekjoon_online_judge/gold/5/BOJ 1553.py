"""
Solving Date    : 2024.01.04
Solving Time    : 57m
Title           : 도미노 찾기
tags            : 구현, 백트래킹
url             : https://www.acmicpc.net/problem/1553
runtime         : 292 ms
memory          : 31120 KB
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def select(i, j, x, y):
    if origin[i][j] > 6 or origin[x][y] > 6:
        return False
    a, b = origin[i][j], origin[x][y]
    if a > b: a, b = b, a
    if (a, b) in domino:
        domino.remove((a, b))
        origin[i][j] += 777
        origin[x][y] += 777
        return True
    return False

def undo(i, j, x, y):
    origin[i][j] -= 777
    origin[x][y] -= 777
    a, b = origin[i][j], origin[x][y]
    if a > b: a, b = b, a
    domino.add((a, b))

def foo(i, j):
    i = i + j//7
    j = j%7
    if i>=8 or j>=7:
        return 1
    if origin[i][j] > 6:
        return foo(i, j+1)
    ret = 0
    if j < 6 and select(i, j, i, j+1):
        ret += foo(i, j+1)
        undo(i, j, i, j+1)
    if i < 7 and select(i, j, i+1, j):
        ret += foo(i, j+1)
        undo(i, j, i+1, j)
    return ret


domino = set()
for i in range(7):
    for j in range(i, 7):
        domino.add((i, j))

origin = [list(map(int, input().rstrip())) for _ in range(8)]

print(foo(0, 0))

"""
백트래킹 문제.

도미노 목록이 "가능한 도미노 경우" 가 아니라
전체 칸을 도미노 전체를 1번씩 써서 채우는걸 구하는 문제.

풀이방법:
1. 한칸씩 진행한다.
2. 이미 처리된 칸이면 스킵한다.
    - 처리되지 않은 칸이면
        2-1. 가로로 놓을 수 있는지 체크 후 놓고 한칸 진행
        2-2. 세로로 놓을 수 있는지 체크 후 놓고 한칸 진행
    - 끝나면 원상복구
3. 모든 칸을 뚫고 나왔으면 카운트 +1

---

- 0~6이 값인데 값처리여부를 +6으로 했다가 0이 안걸려서 한참 삽질
- undo를 값을 복구시킨 뒤 처리해야하는데 순서를 반대로해서 한참 삽질

-- 가로로 놓고 1칸 진행을 어차피 다음칸은 스킵되니까 2로 바꿔봤는데
    292ms -> 304ms로 늘었다. 머지
"""