import graph_sample_inputs


def get_graph_matrix(n=0):
    INF = int(1e9)
    graph_input = graph_sample_inputs.graph_inputs[n]
    _input = iter(graph_input.split("\n"))
    input = lambda:next(_input)

    v, n = map(int, input().split())
    g = [[INF for _ in range(v)] for _ in range(v)]

    for i in range(v):
        g[i][i] = 0

    for _ in range(n):
        a, b, c = map(int, input().split())
        g[a][b] = c
        g[b][a] = c

    return g

def get_graph_list(n=0):
    graph_input = graph_sample_inputs.graph_inputs[n]
    _input = iter(graph_input.split("\n"))
    input = lambda:next(_input)

    v, n = map(int, input().split())
    g = [[] for _ in range(v)]

    for _ in range(n):
        a, b, c = map(int, input().split())
        g[a].append([b, c])
        g[b].append([a, c])

    return g

class Graph:
  def __init__(self,size):
    pass
  def vertex_half_connect(self,_from,to,distance):
    pass
  def vertex_full_connect(self,_from,to,distance):
    pass




