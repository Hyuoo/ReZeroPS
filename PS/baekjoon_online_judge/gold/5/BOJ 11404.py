'''
플로이드워셜 정석문제.
그동안 대충 경유만 해서 다 조회하면 된다-생각해서
for src
  for dest
    for via
이랬다가 실패해서 뭣이 문제여 한참 함.

* 플로이드워셜은 via_ 경유하는게 가장 바깥이다.
'''
def pg(graph):
    for row in graph:
        for i in row:
            print(f"{0 if i==INF else i:}",end=" ")
        print()

INF = 100000*100
n = int(input())
graph = [[0 if i==j else INF for j in range(n)] for i in range(n)]

for _ in range(int(input())):
    a,b,c = map(lambda x:int(x)-1,input().split())
    if graph[a][b] == INF:
        graph[a][b] = c+1
    else:
        graph[a][b] = graph[a][b] if graph[a][b] < c+1 else c+1

for via in range(n):
    for src in range(n):
        for dest in range(n):
            if graph[src][dest] > graph[src][via]+graph[via][dest]:
                graph[src][dest] = graph[src][via] + graph[via][dest]

pg(graph)
