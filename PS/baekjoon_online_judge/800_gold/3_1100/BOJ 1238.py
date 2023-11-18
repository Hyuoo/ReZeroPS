import heapq
import sys
input = sys.stdin.readline

INF = 1000*100
def dstr(g,src):
    global n
    shortest = [INF for _ in range(n)]
    shortest[src] = 0
    q = [(0,src)]
    while q:
        dist, now = heapq.heappop(q)
        if shortest[now]<dist:
            continue
        for next in range(n):
            if now!=next and g[now][next]!=INF:
                if shortest[next] > dist+g[now][next]:
                    shortest[next] = dist+g[now][next]
                    heapq.heappush(q,(shortest[next],next))
    return shortest

n,m,x = map(int,input().split())
x-=1
go = [[INF if i!=j else 0 for j in range(n)] for i in range(n)]
back = [[INF if i!=j else 0 for j in range(n)] for i in range(n)]
for _ in range(m):
    a,b,t = map(int,input().split())
    a-=1
    b-=1
    go[a][b] = t
    back[b][a] = t
max = 0
for a,b in zip(dstr(go,x),dstr(back,x)):
    if max<a+b:
        max = a+b
print(max)
'''
파티
풀이시간 : 55m

다익스트라 문제.
그래프에서 각 점마다,
한 점으로 모이고 한 점에서 흩어지는 거리 최대인 값 출력하기.

일단 다익스트라 구현해놓고,
단순 생각으로 다익스트라 n번 돌리고, x에서 흩어지는거 한번 돌리고
다익스트라 n+1번 돌리는데 역시나 시간초과가 나서

머리가 안돌아가서 질문게시판 제목 스윽,,보고 다익스트라 두번이면 된대서
어케 두번 해야되냐 하고
두번이면 x위치밖에 없는데 해서
a->b 반대인 b->a 그래프 만들고 2다익으로 풀이.
'''
