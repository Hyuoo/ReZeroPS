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
def Dijkstra_matrix_simple(maps: list, start: int) -> list:
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
def Dijkstra_matrix_priority(maps:list, start:int)->list:
  V = len(maps)
  
  shortest = [INF for _ in range(V)]
  pq = [[0, start]]
  shortest[start] = 0
  
  while pq:
    dist, now_idx = heapq.heappop(pq)
    if shortest[now_idx]<dist:
      continue
    for next_idx in range(V):
      if next_idx==now_idx or maps[now_idx][next_idx]==INF:
        continue
      if shortest[next_idx] > shortest[now_idx]+maps[now_idx][next_idx]:  #dist + maps[now_idx][next_idx]
        shortest[next_idx] = shortest[now_idx]+maps[now_idx][next_idx]
        heapq.heappush(pq, [shortest[next_idx], next_idx])
  
  return shortest

#아직
def Dijkstra_list_simple(maps:list, start:int):
    n = len(maps)
    visit = [0 for i in range(n)]
    shortest = [INF for i in range(n)]
    now = start
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

def Dijkstra_list_priority(maps:list, start:int):
    n = len(maps)
    shortest = [INF for _ in range(n)]
    # 최소거리 갱신을 for문 안에서 할 경우 필요
    shortest[start] = 0
    pq = [[0, start]]

    while pq:
        now_dist, now_idx = heapq.heappop(pq)
        # 여기서 한번 잡아줘야 훨씬 빨라지고
        if shortest[now_idx] < now_dist:
            continue
        # 방문 처리를 여기서 할 경우엔
        # 위에 shortest[start] = 0이 필요 없음.
        # shortest[now_idx] = now_dist

        for nxt, nxt_dist in maps[now_idx]:
            total = shortest[now_idx] + nxt_dist
            if shortest[nxt] > total:
                # 방문 처리 타이밍 차이
                # 여기서 하는게 더 빠른 듯.
                shortest[nxt] = total
                heapq.heappush(pq, [total, nxt])

    return shortest





if __name__ == "__main__":
    import Graph
    g = Graph.get_graph_list()

    print(Dijkstra_list_priority(g, 0))
    print(Dijkstra_list_simple(g, 0))
