n, m = map(int,input().split())
g = [[] for i in range(n+1)]

for i in range(n-1):
    a,b,c = map(int, input().split())
    g[a].append([b,c])
    g[b].append([a,c])

def dfs(g, now, dest, s):
    global v
    if now in v:
        return 0
    if now == dest:
        return s
    v.add(now)
    for next in g[now]:
        t = dfs(g, next[0], dest, next[1])
        if t!=0:
            return s+t
    return 0

for i in range(m):
    a,b = map(int,input().split())
    v = set()
    print(dfs(g, a, b, 0))
'''
노드사이의 거리
풀이시간 : 37m

난 노드쌍 천개받아서 계속 노드간 거리 출력하길래
플로이드 써서 하면 잘될줄 알았지...

근데 계산해보니가 3제곱의 벽이 고작 천개로는 뚫리지 않음

그리고 그냥 dfs하려다가 재귀없이 스택으로 하려다 헷갈려서 걍 재귀로 구현
'''
