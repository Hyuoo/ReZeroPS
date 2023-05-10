r=[[0,1],[0,-1],[1,0],[-1,0]]
def dfs(i,j,st,n):
    if i<0 or i>4 or j<0 or j>4:
        return
    if n==6:
        ans.append(st)
        return
    for x,y in r:
        dfs(i+x,j+y,st+maps[i][j],n+1)

maps = [list(input().split()) for _ in range(5)]
ans = []
for i in range(5):
    for j in range(5):
        dfs(i,j,"",0)
print(len(set(ans)))

'''
숫자판 점프
풀이시간 : 18m

싹다 돌려서 중복제거하는 문제
dfs로 모든 경로 싹다 돌려서
set으로 제거 끗

dfs자체를 오랜만에써서 낯설다
'''
