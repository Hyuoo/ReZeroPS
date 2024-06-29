"""
Solving Date    : 2024.04.08
Solving Time    : 15m
Title           : [PCCP 기출문제] 2번 / 석유 시추
tags            : prefix_sum, dfs, bfs
url             : https://school.programmers.co.kr/learn/courses/30/lessons/250136
runtime         : -
memory          : -
"""

import sys
sys.setrecursionlimit(10**9)

def solution(land):
    r = [[1, 0],[-1, 0],[0, 1],[0, -1]]
    def oil_group(x, y):
        ret = 1
        for ax, ay in r:
            nx, ny = x+ax, y+ay
            if nx>=0 and nx<n and ny>=0 and ny<m and land[nx][ny]:
                land[nx][ny] = 0
                col_nums.add(ny)
                ret += oil_group(nx, ny)
        return ret
    
    # print(*land, sep='\n')
    
    n, m = len(land), len(land[0])
    psum = [0 for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            if land[i][j]:
                col_nums = set([j])
                land[i][j] = 0
                tmp = oil_group(i, j)
                for c in col_nums:
                    psum[c] += tmp
    
    # print(psum)
    return max(psum)

"""
재귀탐색으로 인접한 석유 싹 모아다가
존재했었던 열에 다 더해줌

그리고 열 중 가장 큰 값 리턴.
"""