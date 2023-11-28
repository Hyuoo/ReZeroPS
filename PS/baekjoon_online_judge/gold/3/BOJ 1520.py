import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

r = [[0,1],[0,-1],[1,0],[-1,0]]
def dfs(i,j,p):
    if (i<0 or j<0 or i>=n or j>=m) or p>=maps[i][j]:
        return 0
    if paths[i][j]:
        return paths[i][j]
    now = maps[i][j]
    a = 0
    for x,y in r:
        a += dfs(i+x, j+y, now)
    if a:
        paths[i][j] = a
        return a
    else:
        maps[i][j] = 0
        return 0

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
paths = [[0 for _ in range(m)] for _ in range(n)]
paths[0][0] = 1
dfs(n-1,m-1,-1)
print(paths[n-1][m-1])

'''
내리막 길
풀이시간 : 54m

접근 :
바로 이거 완전 dp문제 아니냐?
근데 내려가는 순방향으로 생각해서 이걸 어케 dp로하지 생각하다가
그냥 dfs만 써도 할만하지않을까 해서 dfs로만 풀었다가 시간초과.

readline 꼼수를 쓰려 했으나 오래 버틸 뿐 시간초과.
dp로 풀어라.

- 특정 칸을 도달하는 경우의 수를 합쳐서 다음칸으로 진행하자.
    -> 순방향으로 한다면 결국 해당지점에 도달하는 경우를 합쳐야되기때문에
      거슬러 올라가는게 필요한디
- 아예 골인지점부터 역탐색 ㄱㄱ
- 시작점은 1로 두고 골인점부터 경로 dp초기화하면서 싹다 탐색.
    (*이것만 하면 여전히 시간초과.)
- 시간초과: 아예 dp가 초기화되지않는, 경로가 되지않는 경로를 계속 탐색해서 문제.
    -> 지도가 칸이 높아서 탐색하니까 그냥 0으로 평탄화 해버림
    -> (line: 7, 18~20)

===========================================
그리고 dfs값 합치는거 sum으로 해봤더니 시간차이 엄청남.
저부분만 sum([dfs for])에서 저렇게 바꿨는데 (line: 12~14)
  392ms -> 316ms

===========================================
근데 내리막길을 오르막길로 바꿔서 시작점부터 탐색하면
완전 대칭문제네?
'''
