import sys
input = sys.stdin.readline

INF = 1000*100004

n = int(input())
m = int(input())
maps = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b,d = map(int,input().split())
    maps[a][b] = min(maps[a][b],d)
    
a,b = map(int,input().split())
now = a
visit = [0 for _ in range(n+1)]
shortest = [INF for _ in range(n+1)]
visit[0] = 1
shortest[now] = 0

for _ in range(n-1):
    visit[now] = 1
    for i in range(1,n+1):
        if i==now or visit[i] or maps[now][i]==INF:
            continue
        if shortest[i] > shortest[now] + maps[now][i]:
            shortest[i] = shortest[now] + maps[now][i]
    minv = INF
    for i in range(1,n+1):
        if visit[i]==0 and shortest[i]<minv:
            minv = shortest[i]
            next = i
    now = next
print(shortest[b])
'''
최소비용 구하기
풀이시간 : 32m

방향성있는 다익스트라 문제

문제에서 버스가 이게 단방향인지 양방향인지 헷갈려서
양방향으로 풀었는데
코드가 아니라 머리로 해도 도저히 예제출력이 나올 수가 없어서 한참 혼란
'''
