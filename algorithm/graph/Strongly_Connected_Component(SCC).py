"""
Strongly Connected Component
강한 연결 요소

그래프에서 (노드a->노드b) and (노드b->노드a) 가 되는
그룹들을 찾는?

순환요소를 갖는 그룹??
머라카냐

"""

import Graph

g = Graph.get_dag(4)
n = len(g)
print(g)

# Tarjan Algorithm
# 부모노드로 돌아올 수 있어야 한다는 점을 이용
# 모든 정점에 대해 DFS를 적용한다.
def dfs(x):
    # 모든 정점은 무조건 1번씩만 호출됨.
    # id 유니크하게 부여 됨.
    # id는 항상 탐색 순서에 맞게 오름차순으로 부여된다.
    # x+1 이런식으로 부여 하면 틀림. 아래 반례.
    #   >> 방문 순서가 있는데, id는 순서가 고려 됨. 노드번호는 순서 고려 안됨.
    # V E : 4 5
    # 1 4
    # 4 3
    # 3 1
    # 1 2
    # 2 4
    # ++ 매 (첫)탐색마다 id를 초기화 시켜줘도 유효 함.
    global id
    roots[x] = (id:=id+1)
    # 탐색하는 모든 정점은 스택에 쌓는다.
    # 갈 수 있는 모든 정점 탐색(for문) 후, scc그룹 별로 확정시킴.
    s.append(x)

    p = roots[x]
    for nxt in g[x]:
        if roots[nxt] == 0:
            # 아직 초기화가 안되어있으면 재귀적으로 하는 동시에 그룹핑
            p = min(p, dfs(nxt))
        elif not finished[nxt]:
            # 초기화는 되었지만, 그룹 확정이 안된 경우
            p = min(p, roots[nxt])

    # Q: 그냥 p==x 해도 되는거 아냐?
    # A: 노드 번호랑 부여한 id랑 일치하지 않음.
    if p == roots[x]:
        scc_tmp = []
        # SCC 별로 그룹 만들어서 리스트에 저장.
        while 1:
            t = s.pop()
            scc_tmp.append(t)
            # roots 값을 INF로 둬서 finished 리스트를 안 쓰는 방법도.
            finished[t] = True
            if t == x:
                break
        scc.append(scc_tmp)

    return p

id = 0
# 부모 노드를 메모 할 리스트. 0은 아직 초기화되지 않은 상태.
# started 라고도 볼 수 있음.
# 설명을 똑부러지게 못하겠는데, 그냥 자기 정점번호로 union-find처럼 정점번호/루트번호로 하는것보다,..
# 일단 dfs를 들어 가서 체크를 해야 됨.
roots = [0 for _ in range(n)]
finished = [False for _ in range(n)]  # 그룹이 정해졌는지 상태를 기록
scc = []  # 각 결합 그룹별로 리스트 저장
s = []

for i in range(n):
    # 초기화가 되지 않은 상태여야만 탐색 혹은 SCC그룹에 추가 한다.
    # 갈 수 있는 모든 정점은, 여러 그룹이어도 다 한번에 판별됨.
    if roots[i] == 0:
        print("run", i, dfs(i))
    # print(roots, finished, scc)

print(roots)
print(finished)
print(scc)

"""
어우 느낌은 이해 되는데
구현을 혼자서 쌩으로 못하겠넹
"""