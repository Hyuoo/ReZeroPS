#인접그래프에서 다익스트라 A->B 최단거리만을 리턴하는 함수

INF = 9999999

#그래프와 시작점, 도착점 입력받아 그 최단거리만을 리턴.
def Dijkstra(maps:list, start:int, dest:int)->int:
  V = len(maps)
  
  visit = [False for _ in range(V)]
  shortest = [INF for _ in range(V)]
  
  now = start
  
  while(now != dest):
    visit[now] = True
    
    for next_idx in range(V):
      if (visit[next_idx]==False) and (now!=next_idx) and (maps[now][next_idx]!=INF):
        if shortest[next_idx] < shortest[now] + maps[now][next_idx]:
          shortest[next_idx] = shortest[now] + maps[now][next_idx]
    
    min_idx = 0
    for idx in range(1,V):
      if (visit[idx]==False) and (shortest[min_idx] > shortest[idx]):
        min_idx = idx
    
    now = min_idx
  
  return shortest[dest]






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
#SOLUTION: 0->3->1->4->6 (3+1+2+4) 10

class Graph:
  def __init__(self,size):
    pass
  def vertex_half_connect(self,from,to,distance):
    pass
  def vertex_full_connect(self,from,to,distance):
    pass
