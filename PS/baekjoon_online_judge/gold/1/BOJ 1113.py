"""
Solving Date    : 2024.01.21
Solving Time    : 1h 35m
Title           : 수영장 만들기
tags            : 구현, 그래프 이론, 그래프 탐색, 시뮬레이션, 너비 우선 탐색
url             : https://www.acmicpc.net/problem/1113
runtime         : 80 ms
memory          : 31120 KB
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pool = [[*map(int, list(input().rstrip()))] for _ in range(n)]
ans = 0

# print(*pool, sep="\n")

r = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for height in range(2, 10):
    visit = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visit[i][j] and pool[i][j]<height:
                q = [[i, j]]
                leak = False
                history = set()

                while q:
                    x, y = q.pop()
                    history.add((x, y))
                    if x==0 or x==n-1 or y==0 or y==m-1:
                        leak = True

                    for tx, ty in r:
                        nx = x+tx
                        ny = y+ty
                        if nx<0 or nx>=n or ny<0 or ny>=m:
                            continue
                        if not visit[nx][ny] and pool[nx][ny] < height:
                            visit[nx][ny] = True
                            q.append([nx, ny])

                if not leak:
                    ans += len(history)

print(ans)

"""
한참 헤멤..

1. 제일 먼저 단순하게 가로세로로 물이 고이는 곳을 체크해서 시도
    -> 직선으로만 체크해서 ㄹ자와 같이 굽은경로는 고려안함
2. 각 지점별로 dfs해서 물이 새면 높이 1씩 낮추는 방식으로 시도
    -> 순회 순서 때문에 물이 새는지 여부 확인 전에 함수 끝나서 실패
3. bfs로 풀이

처음엔 높이를 9부터 낮추는 식으로 해서
    - if leak: 물높이 -1
한 뒤, 마지막에 물높이를 순회해서 세는 방식으로 했는데,
1부터 시작해서 
    - if not leak: 안 샌 칸만큼 ans++
하는 편이 코드도 깔끔해져서 바꿨다.
불필요한 물높이 리스트를 만들 필요도 없고
"""