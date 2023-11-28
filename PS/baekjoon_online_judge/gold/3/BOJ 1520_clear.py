import sys
input = sys.stdin.readline

r = [[0,1],[0,-1],[1,0],[-1,0]]

def dfs(i,j):
    if paths[i][j]!=-1:
        return paths[i][j]
    paths[i][j] = 0
    for x,y in r:
        nx = i+x
        ny = j+y
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if maps[i][j]<maps[nx][ny]:
            paths[i][j] += dfs(i+x,j+y)
    return paths[i][j]

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
paths = [[-1 for _ in range(m)] for _ in range(n)]
paths[0][0] = 1
print(dfs(n-1,m-1))

'''
내리막 길
더 깰끔버전

앞 코드보다 속도
  316ms -> 192ms
'''
