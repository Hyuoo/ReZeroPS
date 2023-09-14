import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

m,n = map(int,input().split())
maps = [list(map(int,list(input().rstrip()))) for _ in range(n)]
ans = [[222 for _ in range(m)] for _ in range(n)]

r = [[0,1],[0,-1],[1,0],[-1,0]]
q = [[0,0,0]]

while q:
    w,x,y= heapq.heappop(q)
    if ans[x][y]<=w:
        continue
    if x==n-1 and y==m-1:
        print(w)
        break
    ans[x][y] = w
    for i,j in r:
        nx = x+i
        ny = y+j
        if nx<0 or nx>=n or ny<0 or ny>=m or ans[nx][ny]<=w:
            continue
        heapq.heappush(q,[w+maps[nx][ny],nx,ny])

'''
알고스팟
풀이시간 : 40m

격자맵에서 벽을 부수고 (0,0)에서 (n,m)으로 이동하는 문제
벽을 가장 적게 부수고 이동하면 몇개부숨?

벽을 부수는 제한이 없기 때문에 모든 이동을 고려해야함.

처음 틀린 접근은
오른쪽, 아래 이렇게만 진행해서 한줄dp로 그냥 풀면 풀리는거 아닌가?
했는데, 꼭 한방향으로 가는 문제가 아니라서 dp불가능

그래서 bfs로 다시 푸름
1. 처음 풀이는 그냥 큐로 단순 bfs했는데 간당간당하게 통과
2. 큐 -> 힙으로 바꾸니까 속도 빨라짐
    (근데 거리기준으로 안해서 빨리가는길 우선으로 안했는데 암튼 빨라짐)
3. 우선순위 거리기준으로 바꾸고, 골인점 도달시 조기종료
    -> 다익스트라 느낌의 풀이가 되어버림

-----------------------
1     -> 2     -> 3
820ms -> 116ms -> 76ms
'''
