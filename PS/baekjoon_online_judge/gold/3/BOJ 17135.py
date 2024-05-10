"""
Solving Date    : 2024.05.10
Solving Time    : 1h 51m
Title           : 캐슬 디펜스
tags            : 구현, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 시뮬레이션, 너비 우선 탐색
url             : https://www.acmicpc.net/problem/17135
runtime         : 156 ms
memory          : 31732 KB
"""

import sys
input = sys.stdin.readline
from itertools import combinations

def seq_gen(x, y, n):
    row_seq = list(range(x, x-n+1, -1)) + list(range(x-n+1, x+1))
    col_seq = list(range(y-n+1, y+n))
    return zip(row_seq, col_seq)

def search(x, y, n):
    for lim in range(1, n+1):
        for i, j in seq_gen(x, y, lim):
            if i>=0 and j>=0 and j<m and enemy_cp[i][j]:
                return (i, j)
    return None
    
n, m, d = map(int, input().split())
enemy = [[*map(int, input().split())] for _ in range(n)]
ret = 0

# print(*enemy, sep="\n")

for a,b,c in combinations(range(m), 3):
    enemy_cp = [list(l) for l in enemy]
    row = n-1
    count = 0
    while row+1:
        for elem_x, elem_y in [t for col in [a,b,c] if (t:=search(row, col, d))]:
            if enemy_cp[elem_x][elem_y]:
                count += 1
                enemy_cp[elem_x][elem_y] = 0
        row -= 1
    
    # print(f"{a}{b}{c}: {count}")
    # print(*enemy_cp, sep="\n")
    ret = max(ret, count)

print(ret)

"""
- 겹치는 경우 다른 타겟쏘지않음
- 턴마다 진행되며, 이후 턴에 영향을 줌.
    - 순서대로 시뮬레이션 해야 함.
- 사거리를 늘리는식으로 계산하면 안됨.
    - 안닿는 적이 닿는다.
    - 사거리는 유지하되 세로방향으로 스캔하는 방식으로 풀이 해야 함.
- 케이스 크기가 작음
    - 완전탐색 고려


접근:
1. 조합까지 완탐 하기는 그래서 어떻게든 각 컬럼별로 구하는 방법 강구
    - 불가: 시간진행마다, 인접칸마다 서로 영향을 줌.
            내 머리로는 그런방법 없음.

2. 혹은 역으로 타겟이 시간에 따라 각 컬럼에 해당되는 경우를 집계하고
    그 중 3칸을 뽑는 방법?
    - 불가: 3칸을 어떻게 뽑느냐에 따라 서로 영향을 줌

3. 그냥 조합까지 완전탐색으로 풀기


풀이:
- 3개 컬럼을 선택하는 모든 조합에 대해서 다음 진행
    - 마지막 행부터 -1 하며 모든 행에 대해서 다음 진행
        - 3개 컬럼에서 이번 턴에 제거할 적 위치 구하기
        - 3개의 적 위치 일괄 제거, 카운팅


중간 실패사유:
- 순회한답시고 [[0, -1], [-1, 0], [0, 1]]로 재귀순회 했더니
    문제에서 주어진 탐색순서가 맞지 않아 실패


여담:
- 제거할 적 위치 구하는 과정에서 필요한칸만 대각선으로 움직이게 하는걸
    짜는데 한-참 걸렸다.
    머리가 굉장히 굳었다.
- 배열 복사 deepcopy -> list(line)하니 156ms -> 108ms
"""