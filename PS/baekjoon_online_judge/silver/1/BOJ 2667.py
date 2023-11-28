d = [[1,0],[-1,0],[0,1],[0,-1]]
def dfs(i,j):
    global n
    if i<0 or i>=n or j<0 or j>=n or maps[i][j]=="0":
        return 0
    maps[i][j]="0"
    c = 1
    for x,y in d:
        c+=dfs(i+x, j+y)
    return c

n = int(input())
maps = [list(input()) for _ in range(n)]

ret = []
for i in range(n):
    for j in range(n):
        tmp = dfs(i,j)
        if tmp:
            ret.append(tmp)
print(len(ret),*sorted(ret),sep="\n")

"""
단지번호붙이기
풀이시간 : 9m
#KDT_코테스터디

정석적인 탐색
"""
