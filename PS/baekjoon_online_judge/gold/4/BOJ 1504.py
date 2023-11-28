import sys
input = sys.stdin.readline

def dijkstr(start):
    global g
    visit = [0 for _ in range(n)]
    shortest = [INF for _ in range(n)]
    shortest[start] = 0
    now = start
    while 1:
        visit[now] = 1
        for i in range(n):
            if g[now][i] != 0 and g[now][i] != INF and shortest[i] > shortest[now] + g[now][i]:
                shortest[i] = shortest[now] + g[now][i]
        mval = INF
        next = now
        for i in range(n):
            if visit[i] == 0 and mval > shortest[i]:
                mval = shortest[i]
                next = i
        if now == next:
            break
        now = next
    return shortest

INF = 1000*1000
n,e = map(int,input().split())
g = [[INF if i!=j else 0 for j in range(n)] for i in range(n)]
for _ in range(e):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    g[a][b] = c
    g[b][a] = c

a,b = map(int,input().split())
a-=1
b-=1
d = dijkstr(0)
if INF in (d[a],d[b],d[n-1]):
    ans = -1
else:
    da = dijkstr(a)
    db = dijkstr(b)
    ans = min(d[a]+db[a]+db[n-1], d[b]+da[b]+da[n-1])
print(ans)
'''
특정한 최단 경로
풀이시간 : 50m

다익스트라 구현하고 점마다 적용만 시키면 되는 문제

우선 시작점에서, 두 경유지와 N번정점 갈 수 없으면 -1
아니면 모두 가능

경유정점 v1, v2라고 할 때
1. v1 먼저 경유 할 경우 [ 1 -> v1 -> v2 -> N ]
2. v2 먼저 경유 할 경우 [ 1 -> v2 -> v1 -> N ]
이 각 최단거리

둘 중 작은 값 리턴하면 끝.
---------------------------------
첨에 더 가까운데로 가면 되겠지- 해서
아래 코드처럼 했다가 양 경유지가 동일 거리일 때 오답이라 시간걸림.
if s[a]<s[b]:
    a,b=b,a
ss = dijkstr(a)
ans = s[b]+ss[b]+ss[n-1]
print(ans)

'''
