"""
최소 신장 트리 (Minimum Spanning Tree)

먼저 신장트리는 그래프가 다 연결되어 있는데, 연결요소가 최소인 그래프이다.
노드가 n개이면 간선의 수는 n-1개이기 때문에
사이클이 구조적으로 생길 수 없어 트리가 된다.

그 중 최소 신장 트리는 가중치가 있는 그래프에서
연결된 모든 간선의 합이 최소가 되는 트리를 말한다.


최소신장트리 알고리즘으로는
- Kruskal   : 간선 중심
- Prim      : 한 노드 그룹 중심
- Sollin    : 각 노드 그룹 중심
세가지가 있다. 세 방법 모두 그리디(Greedy)한 풀이이다.

일반적으로는 크루스칼이랑 프림만 언급이 되고 솔린은 거의 안된다.

구현은 아래를 참고하고 미리 정리하는 시간복잡도
    (정점 V개, 간선 E개라고 했을 때,)
- Kruskal   : O(ElogE)  # 간선을 정렬하는 시간이 대부분.
- Prim      : O(V^2)    # 정점 수만큼, 각 정점에서 인접 정점만큼 반복
간선이 적은 희소 그래프일 경우 크루스칼,
간선이 많은 밀집 그래프는 프림이 적합하다.


+ 프림 알고리즘은 다익스트라랑 굉장히 비슷하다.
    - 갈수있는 모든 노드의 거리를 계속 갱신하면서 최소거리의 노드를 고른다.
    - 갈수있는 모든 간선 중 최소간선을 고른다.
    는 차이가 있다.

---
관련 문제
- G4 최소 스패닝 트리: https://www.acmicpc.net/problem/1197
    - G4 네트워크 연결: https://www.acmicpc.net/problem/1922
    - 1197, 1922 두 문제가 같은 알고리즘으로 풀린다.
"""

import Graph

g = Graph.get_graph_list()
N = len(g)
# 그래프 출력
print_graph = lambda g: print(*[f"{i}: {g[i]}" for i in range(len(g))], sep="\n")

print("=== origin graph ===")
print_graph(g)

##### 일단 그래프가 이미 갖춰진 상태라서 크루스칼에서 사용할 간선 추출.
edges = []

for src in range(len(g)):
    for to, dist in g[src]:
        edge = ([to, src, dist] if src > to else [src, to, dist])

        if edge not in edges:
            edges.append(edge)

# print(edges, len(edges))


###############################################################################
"""
Kruskal Algorithm

1. 간선 기준으로 정렬한다.
2. 최소비용인 간선부터 선택한다.
    - 그래프에 사이클이 생기는지 검사한다.
        - union-find 사용
    - 사이클이 생기지 않는다면 MST에 추가.
"""

edges.sort(key=lambda x:x[2])

def union(parents, a, b):
    pa = find(parents, a)
    pb = find(parents, b)
    if pa < pb: parents[pb] = pa
    else: parents[pa] = pb

def find(parents, a):
    if parents[a] == a:
        return a
    parents[a] = find(parents, parents[a])
    return parents[a]

# kruskal MST의 결과 저장
k_mst = [[] for _ in range(N)]
k_parents = [i for i in range(N)]
k_total_cost = 0

for edge in edges:
    src, dest, dist = edge
    a = find(k_parents, src)
    b = find(k_parents, dest)
    if a != b:
        union(k_parents, a, b)
        k_mst[src].append([dest, dist])
        k_mst[dest].append([src, dist])
        k_total_cost += dist

print("=== kruskal_mst / total cost:", k_total_cost, "===")
print_graph(k_mst)


###############################################################################
"""
Prim Algorithm

1. 한 정점에서 시작한다.
2. (방문하지않은) 갈 수 있는 모든 정점 중, 최소비용인 정점을 골라 선택한다.
    - 최소 힙 사용
    - 간선이 n-1개가 될 때까지 반복. 
"""
import heapq

p_mst = [[] for _ in range(N)]
visited = [False for _ in range(N)]
# q = []  # heapq
edge_count = 0

PRIM_START = 0
visited[PRIM_START] = True
# 첫 방문 노드를 더미노드로 하기가..
# MST 자체를 필요로 하지 않고, 비용만 필요하다면
# [비용 0, 다음위치 0] 이렇게 더미로 시작할 수 있다.
q = [[dist, PRIM_START, nxt] for nxt, dist in g[PRIM_START]]
heapq.heapify(q)
p_total_cost = 0

while edge_count != N-1:
    # src가 필요 한 이유가 트리 자체를 구성하기 위해서.
    # 비용 계산만 할 경우 src 필요 없음.
    dist, src, dest = heapq.heappop(q)
    if not visited[dest]:
        visited[dest] = True
        p_mst[src].append([dest, dist])
        p_mst[dest].append([src, dist])
        edge_count += 1
        p_total_cost += dist

        for nxt, nxt_dist in g[dest]:
            if not visited[nxt]:
                heapq.heappush(q, [nxt_dist, dest, nxt])

print("=== prim_mst / total cost:", p_total_cost, "===")
print_graph(p_mst)


###############################################################################
"""
Sollin Algorithm

솔린 알고리즘은
반복과정 중 생기는 모든 그래프 집합에서 최소 간선을 선택한다. 
"""