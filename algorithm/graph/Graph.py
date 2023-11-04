import graph_sample_inputs



def get_graph_matrix(n=0):
    # [0:V] 양방향 가중치 그래프 (인접행렬)
    INF = int(1e9)
    graph_input = graph_sample_inputs.graph_inputs[n]
    _input = iter(graph_input.split("\n"))
    input = lambda:next(_input)

    V, E = map(int, input().split())
    g = [[INF for _ in range(V)] for _ in range(V)]

    for i in range(V):
        g[i][i] = 0

    for _ in range(E):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        g[a][b] = c
        g[b][a] = c

    return g

def get_graph_list(n=0):
    # [0:V] 양방향 가중치 그래프 (연결리스트)
    graph_input = graph_sample_inputs.graph_inputs[n]
    _input = iter(graph_input.split("\n"))
    input = lambda:next(_input)

    V, E = map(int, input().split())
    g = [[] for _ in range(V)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append([b, c])
        g[b].append([a, c])

    return g

def get_dag(n=0):
    # [0:V]
    graph_input = graph_sample_inputs.directed_acyclic_graph_inputs[n]
    _input = iter(graph_input.split("\n"))
    input = lambda:next(_input)

    V, E = map(int, input().split())
    g = [[] for _ in range(V)]

    for _ in range(E):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)

    return g

class Graph:
  def __init__(self,size):
    pass
  def vertex_half_connect(self,_from,to,distance):
    pass
  def vertex_full_connect(self,_from,to,distance):
    pass




