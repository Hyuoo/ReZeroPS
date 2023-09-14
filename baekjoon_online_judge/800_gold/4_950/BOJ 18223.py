'''
다익스트라 문제.
모든 정점이 연결된 양방향 그래프에서
1번->V번 정점으로 가는 최소경로에 P번 정점이 포함될 수 있는지 여부를 찾는 문제.

간단히 다익스트라를 구현해서
(1번->V번) 으로 가는 최소 경로와
(1번->P번 + P번->V번) 각 최소경로의 합이 같으면
V로 가는 길에 P를 들러도 되므로 따로 경로 저장을 하거나 하지않음.

근데 또 python3으로 시간초과 pypy3으로 통과 했다. 읭ㅇㅀ
'''

V, E, P = map(int, input().split())
INF = 999999
P -= 1
maps = [[0 if i==j else INF for j in range(V)] for i in range(V)]

def connect_edge(map, src, dest, dist):
    map[src][dest] = dist
    map[dest][src] = dist

for _ in range(E):
    src, dest, dist = map(int, input().split())
    connect_edge(maps, src-1, dest-1, dist)

def dijkstra(maps, V, start, end):
    visit = [False for _ in range(V)]
    shortest = [INF for _ in range(V)]
    shortest[start] = 0
    now = start
    while(now!=end):
        visit[now] = True
        min = INF
        next = now
        for vtx, dist in enumerate(maps[now]):
            if now == vtx and visit[vtx] and dist==INF:
                continue
            if shortest[vtx] > shortest[now]+dist:
                shortest[vtx] = shortest[now]+dist
        for i in range(V):
            if not visit[i] and shortest[i] != INF and min>shortest[i]:
                min = shortest[i]
                next = i
        now = next
    return shortest[end]

print("SAVE HIM" if dijkstra(maps,V,0,V-1) == dijkstra(maps,V,0,P)+dijkstra(maps,V,P,V-1) else "GOOD BYE")
