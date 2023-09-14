n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
cost = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            continue
        u = 999999999
        l = 999999999
        if i>0:
            u = cost[i-1][j]+(max(maps[i][j]-maps[i-1][j]+1,0))
        if j>0:
            l = cost[i][j-1]+(max(maps[i][j]-maps[i][j-1]+1,0))
        cost[i][j] = min(u,l)
n-=1
print(cost[n][n])
'''
배열 탈출
풀이시간 : 28m

항상 [i][j] 칸에 도착 하는 최소 비용을 갱신.
'''
