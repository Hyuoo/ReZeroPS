import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(r,c,x,y,n):
    global a
    if x<0 or x>=r or y<0 or y>=c:
        return 0
    if a[x][y] == n:
        return 0
    if a[x][y] == 1:
        a[x][y] = n
        return 1
    a[x][y] = n
    d = 0
    for i,j in [[0,-1],[0,1],[-1,0],[1,0]]:
        d+=dfs(r,c,x+i,y+j,n)
    return d

r,c = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(r)]
ans = [0]
i=2
while 1:
    ans.append(dfs(r,c,0,0,i))
    if ans[-1]==0:
        break
    i+=1
print(i-2,ans[-2],sep="\n")
'''
치즈
풀이시간 : 26m

2차원배열에 치즈가 있는데 외부로 노출된부분은 단위시간마다 증발
1 1 1
1 0 1
1 1 1
이런식으로 안에 공간이 있어도 외부에서 닿는 부분만 증발이기 때문에
밖에서 탐색 돌린다.

탐색돌리면서 지운 1갯수 계속 저장해놓고,
0이 되기 이전 값 리턴
'''
