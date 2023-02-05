'''
택배
풀이시간 : 37m

플로이드워셜을 도는데, 각 최단거리를 갈 때 최초 출발할 방향을 출력하기.
원래 그래프에서 플로이드워셜 적용하면서,
출발방향 저장할 동일한 크기의 2차원배열 만들어서
최초로 갈 수있을 경우(출발방향 없을 때 && 갈 수있을때) 또는 값이 갱신 될 때마다 출발방향을 갱신. 끗
'''
INF = 10000*200
n, m = map(int,input().split())
g = [[INF if i!=j else 0 for j in range(n)] for i in range(n)]
t = [[-1 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    g[a][b] = c
    g[b][a] = c

for k in range(n):
    for src in range(n):
        if src==k:
            continue
        for dest in range(n):
            if dest==src or dest==k:
                continue
            if t[src][dest] == -1 and g[src][dest]!=INF:
                t[src][dest] = dest
            if g[src][dest] > g[src][k]+g[k][dest]:
                g[src][dest] = g[src][k] + g[k][dest]
                if t[src][k]!=-1:
                    t[src][dest] = t[src][k]
                else:
                    t[src][dest] = k

for i in t:
    print(*map(lambda x:x+1 if x!=-1 else "-", i))
