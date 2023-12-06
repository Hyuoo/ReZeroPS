"""
Solving Date    : 2023.11.30
Solving Time    : 19m
Title           : 미로 만들기
tags            : 구현, 시뮬레이션
url             : https://www.acmicpc.net/problem/1347
runtime         : 44 ms
memory          : 31120 KB
"""

input()
maze = [["#" for _ in range(100)] for _ in range(100)]
maze[50][50] = "."
dr = 3  # 서쪽부터 0, CW; 0 1 2 3
# 현재 위치 (50, 50)
now_i = 50
now_j = 50
# 상하, 좌우 최대 넓이 체크
bound_i = [50, 50]
bound_j = [50, 50]

for op in input():
    if op == "F":
        # 01, 11은 상하 이동
        if dr&1:
            # 1은 감소--, 3은 증가++
            now_i += (dr == 3)*2-1
            # 상하 바운드 갱신
            bound_i = [min(bound_i[0], now_i), max(bound_i[1], now_i)]
        # 00, 10은 좌우 이동
        else:
            # 0은 감소--, 2는 증가++
            now_j += (dr == 2)*2-1
            # 좌우 바운드 갱신
            bound_j = [min(bound_j[0], now_j), max(bound_j[1], now_j)]
        # 현재 위치 벽 없애기
        maze[now_i][now_j] = "."
    elif op == "L":
        dr = (dr - 1) % 4
    elif op == "R":
        dr = (dr + 1) % 4

for i in maze[bound_i[0]:bound_i[1]+1]:
    print(*i[bound_j[0]:bound_j[1]+1], sep="")

"""
구현+시뮬레이션 ㄷ
"""