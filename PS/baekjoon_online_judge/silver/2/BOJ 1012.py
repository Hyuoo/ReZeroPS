import sys
sys.setrecursionlimit(10**9)
'''
그냥 붙어있는건 지우면서 
'''
def clear(maps, i, j):
    if maps[i][j]==1:
        maps[i][j] = 0
        for i_idx, j_idx in ([1,0],[-1,0],[0,1],[0,-1]):
            if i+i_idx>=0 and i+i_idx<len(maps) and j+j_idx>=0 and j+j_idx<len(maps[0]):
                clear(maps, i+i_idx, j+j_idx)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    maps = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x,y = map(int, input().split())
        maps[y][x] = 1

    count = 0
    for i, row in enumerate(maps):
        for j, flag in enumerate(row):
            if flag==1:
                clear(maps,i,j)
                count+=1
    print(count)
