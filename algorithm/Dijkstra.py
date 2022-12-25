

#그래프와 시작점, 도착점 입력받아 그 최단거리만을 리턴.
def Dijkstra(maps:list, start:int, dest:int)->int:
  pass






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
