import sys
input = sys.stdin.readline
from collections import deque

def dfs(g, n, v):
    visit = [1 for _ in range(n+1)]
    s = [v]
    ret = []
    while s:
        now = s.pop()
        if visit[now]:
            visit[now] = 0
            ret.append(now)
            for next in sorted(g[now],reverse=True):
                s.append(next)
    print(*ret)

def bfs(g, n, v):
    visit = [1 for _ in range(n+1)]
    q = deque([v])
    ret = []
    while q:
        now = q.popleft()
        if visit[now]:
            visit[now] = 0
            ret.append(now)
            for next in sorted(g[now]):
                q.append(next)
    print(*ret)

n,m,v = map(int,input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

dfs(g,n,v)
bfs(g,n,v)
