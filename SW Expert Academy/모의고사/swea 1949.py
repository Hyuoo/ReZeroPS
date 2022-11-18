x = [0, 0, -1, 1]
y = [-1, 1, 0, 0]
def dfs(h, i, j, K, N, length, route):
    l = [0]
    for ro in range(4):
        next_x = j+x[ro]
        next_y = i+y[ro]
        if [next_y,next_x] not in route:
            if next_x>=0 and next_x<N and next_y>=0 and next_y<N:
                if h>maps[next_y][next_x]:
                    l.append(dfs(maps[next_y][next_x], next_y, next_x, K, N, length+1, route+[[next_y,next_x]]))
                elif h>maps[next_y][next_x]-K:
                    l.append(dfs(h-1, next_y, next_x, 0, N, length+1, route+[[next_y,next_x]]))
    return max([length]+l)

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    maps = [0 for _ in range(N)]
    H = 0
    l = [0]
    for i in range(N):
        maps[i] = list(map(int,input().split()))
        if max(maps[i])>H:
            H = max(maps[i])
    for i in range(N):
        for j in range(N):
            if(maps[i][j] == H):
                l.append(dfs(H, i , j, K, N, 1, [[i,j]]))
    print(f"#{test_case}",max(l))
