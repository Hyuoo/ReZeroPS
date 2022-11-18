'''
1949. [모의 SW 역량테스트] 등산로 조성

접근 : 가장높은 좌표에서 시작하여 dfs로 갈수있는 최장 경로 탐색.

1. 맵에서 가장 큰 값 찾아서 그 값 좌표로 dfs함수 시작
>> dfs(h:현재위치높이, i:y좌표, j:x좌표, K:문제에서의 K값 겸 플래그, N:맵사이즈, length:현재길이, route:방문좌표리스트)
2. dfs함수 내
2.1 i,j 좌표에서 4방위 갈수있는곳 탐색
2.2 if방문하지않았고 if범위초과아니면
2.3 해당위치가 현재위치h보다 낮으면 방문(재귀dfs)
2.3.2 만약 현재위치h보다 높은데, K로 깎아서 낮아져도 방문(재귀dfs)
>> 2.3과 2.3.2의 차이는 다음위치의 높이(maps[next_y][next_x], h-1)와, K플래그 여부(K, 0)
2.4 위 과정에서 모든 방문해서 나온 값 length를 리스트l에 집어넣고 제일 긴 length리턴 return max([length]+l)
'''
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
