import sys
sys.setrecursionlimit(10**9)

def dfs(i, j, numbering):
    if (i<0 or j<0 or i>=n or j>=m) or (origin[i][j]!=0):
        return 0
    origin[i][j] = -1
    groups[i][j] = numbering
    s=1
    for x,y in [[0,-1],[-1,0],[0,1],[1,0]]:
        s+=dfs(i+x, j+y, numbering)
    return s

n,m = map(int,input().split())
origin = []
groups = [[0 for j in range(m)]for i in range(n)]

for i in range(n):
    origin.append(list(map(int,list(input()))))

numbering = 1
group = [0]
for i in range(n):
    for j in range(m):
        if origin[i][j] == 0:
            group.append(dfs(i, j, numbering))
            numbering += 1

for i in range(n):
    for j in range(m):
        if origin[i][j] == 1:
            seq = set()
            sub = 1
            for x,y in [[0,-1],[-1,0],[0,1],[1,0]]:
                if i+x<0 or j+y<0 or i+x>=n or j+y>=m:
                    continue
                seq.add(groups[i+x][j+y])
            for s in seq:
                sub+=group[s]
            origin[i][j] = sub%10

for i in origin:
    print(*map(lambda x:0 if x==-1 else x,i),sep="")

'''
벽 부수고 이동하기 4
풀이시간 : 1h 37m

일단 문제보고 든 생각. 4씩이나 있는데 4를 처음푸네?!

진짜 문제부분 읽고 그냥 단순한 탐색문제 아녀?하고 생각했다가
시간초과가 났다
그래서 매번 탐색이 아니라 공간 별 넓이를 아예 구해놓고,
벽 주변 4방 합을 구하면 되겠구나 생각했다가

아니그럼 이어진벽은 또 처리를 해줘야하잖아 해서
그게 귀찮아서 이짓저짓 해봐도 시간초과가 나서 방법을 찾아서
아예 이어진 크기만 세는게 아니라,
번호를 부여해서 그룹별로 한번씩만 세도록 했다.

처음엔 그냥 그룹을 별도로 안만들고 하고싶어하다 애먹어서
정신차리고 그냥 그룹별로 만들어줬다.

그리고 풀이를 고치는걸 서너번 하다보니
다 풀고나서 제출형식이 %10인걸 까먹고
아 왜틀렸어 하고 한참을 더 고민했다.

%10만 붙여주니 끝났다. 젠장.
'''
