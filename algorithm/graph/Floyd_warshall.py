from copy import deepcopy


def Floyd_warshall(maps:list):
    n = len(maps)
    floyd_maps = deepcopy(maps)

    # 플로이드 워셜은 경유하는 노드가 가장 바깥 for문이다
    for k in range(n):
        for src in range(n):
            for dest in range(n):
                if floyd_maps[src][dest] > (dist := floyd_maps[src][k] + floyd_maps[k][dest]):
                    floyd_maps[src][dest] = dist

    return floyd_maps



if __name__ == "__main__":
    import Graph
    g = Graph.get_graph_matrix()

    for i in g:
        print(i)

    fg = Floyd_warshall(g)

    print("="*60)

    for i in fg:
        print(i)


