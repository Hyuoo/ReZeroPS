import heapq

'''
1. IN(Adjacency matrix, start) PROCESS(simple dijkstra) OUT(shortest list)
  - Dijkstra_m_simple()
2. IN(Adjacency matrix, start) PROCESS(priority dijkstra) OUT(shortest list)
  - Dijkstra_m_priority()
3. IN(Adjacency List, start) PROCESS(simple dijkstra) OUT(shortest list)
  - Dijkstra_l_simple()
4. IN(Adjacency List, start) PROCESS(priority dijkstra) OUT(shortest list)
  - Dijkstra_l_priority()
'''

INF = 9999999

#인접행렬의 그래프와 시작점 정수 입력받아 전체 최단거리 리스트를 리턴.
def Dijkstra_m_simple(maps: list, start: int) -> list:
    V = len(maps)
    
    visit = [0 for _ in range(V)]
    shortest = [INF for _ in range(V)]
    shortest[start] = 0
    now_idx = start

    while 1:
        visit[now_idx] = True
        for next_idx in range(V):
            if now_idx==next_idx or visit[next_idx]==1 or maps[now_idx][next_idx]==INF:
                continue
            if shortest[next_idx] > shortest[now_idx] + maps[now_idx][next_idx]:
                shortest[next_idx] = shortest[now_idx] + maps[now_idx][next_idx]

        next_idx = now_idx
        minv = 999999
        for i in range(V):
            if visit[i]==0 and minv>shortest[i]:
                minv = shortest[i]
                next_idx = i
        if now_idx==next_idx:
            break
        now_idx = next_idx

    return shortest

#인접행렬 그래프와 시작점 정수 입력받아 전체 최단거리 리스트를 리턴.
def Dijkstra_m_priority(maps:list, start:int)->list:
  V = len(maps)
  
  shortest = [INF for _ in range(V)]
  q = [[0, start]]
  shortest[start] = 0
  
  while q:
    dist, now_idx = heapq.heappop(q)
    if shortest[now_idx]<dist:
      continue
    for next_idx in range(V):
      if next_idx==now_idx or maps[now_idx][next_idx]==INF:
        continue
      if shortest[next_idx]>shortest[now_idx]+maps[now_idx][next_idx]:
        shortest[next_idx] = shortest[now_idx]+maps[now_idx][next_idx]
        heapq.heappush(q, [dist, next_idx])
  
  return shortest

#아직
def Dijkstra_l_simple(maps:list):
    n = len(maps)
    visit = [0 for i in range(n)]
    shortest = [INF for i in range(n)]
    now = 0
    shortest[0] = 0
    visit[0] = 1
    while 1:
        visit[now] = 1
        for next, dist in maps[now]:
            if visit[next]:
                continue
            shortest[next] = min(shortest[next], shortest[now]+dist)
        minv = INF
        next = now
        for i in range(n):
            if visit[i]==0 and shortest[i]<minv:
                minv = shortest[i]
                next = i
        if next==now:
            break
        now = next
    return shortest


#tmp graph
graph_input = '''
[
[  0,   5,   2,   3, INF, INF, INF],
[  5,   0, INF,   1,   2, INF, INF],
[  2, INF,   0, INF, INF,   7, INF],
[  3,   1, INF,   0, INF,   3,   8],
[INF,   2, INF, INF,   0, INF,   4],
[INF, INF,   7,   3, INF,   0,   6],
[INF, INF, INF,   8,   4,   6,   0]
]
'''
#SHORTEST(0): [0, 4, 2, 3, 6, 6, 10]
#SOLUTION(0,6): 0->3->1->4->6 (3+1+2+4) 10
graph_link = '''0 1 5
0 2 2
0 3 3
1 3 1
1 4 2
2 5 7
3 5 3
3 6 8
4 6 4
5 6 6
'''

class Graph:
  def __init__(self,size):
    pass
  def vertex_half_connect(self,from,to,distance):
    pass
  def vertex_full_connect(self,from,to,distance):
    pass
