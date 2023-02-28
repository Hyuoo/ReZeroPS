import sys
import heapq
input = sys.stdin.readline

INF = 4000*100001

def hatiho():
    global n, maps
    q = [[0,0]]
    shortest = [INF for i in range(n)]
    shortest[0] = 0
    while q:
        d, now = heapq.heappop(q)
        if shortest[now]<d:
            continue
        for next, dist in maps[now]:
            if shortest[next]>shortest[now]+dist:
                shortest[next] = shortest[now]+dist
                heapq.heappush(q,[shortest[next],next])
    return shortest

def woo():
    global n, maps
    q = [[0,1]]
    shortest = [INF for i in range(n*2)]
    shortest[1] = 0
    while q:
        d, now = heapq.heappop(q)
        if shortest[now]<d:
            continue
        for next, dist in maps[now//2]:
            next = next*2+(now&1^1)
            if now&1:
                dist >>= 1
            else:
                dist <<= 1
            if shortest[next] > shortest[now]+dist:
                shortest[next] = shortest[now]+dist
                heapq.heappush(q,[shortest[next], next])
    #print(shortest)
    return [min(shortest[i*2],shortest[i*2+1]) for i in range(n)]

n,m = map(int,input().split())
maps = [[] for _ in range(n)]

for _ in range(m):
    a,b,d = map(int,input().split())
    a-=1
    b-=1
    d*=2
    maps[a].append([b,d])
    maps[b].append([a,d])

a = [hatiho(),woo()]
#print(*a,sep="\n")
c = 0
for i in range(n):
    if a[0][i]<a[1][i]:
        c+=1
print(c)
