#https://school.programmers.co.kr/learn/courses/30/lessons/154540
'''
풀이시간 : 24m
dfs 정석적인 문제.
아나 재귀깊이
'''
import sys
sys.setrecursionlimit(10**5)

a=[]

def dfs(col, row, i, j):
    if (i<0 or i>=col or j<0 or j>=row) or a[i][j] == 0:
        return 0
    sum = a[i][j]
    a[i][j] = 0
    for i_,j_ in [[-1,0],[0,-1],[0,1],[1,0]]:
        sum += dfs(col, row, i+i_, j+j_)
    return sum

def solution(maps):
    ans = []
    row_size = len(maps[0])
    col_size = len(maps)
    for row in maps:
        a.append(list(map(lambda x:0 if x=="X" else int(x),list(row))))

    for i in range(col_size):
        for j in range(row_size):
            s = dfs(col_size, row_size, i, j)
            if s!=0:
                ans.append(s)
                
    if len(ans)==0:
        return [-1]
    return sorted(ans)
