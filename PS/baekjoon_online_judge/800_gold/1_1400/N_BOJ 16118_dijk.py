import sys
input = sys.stdin.readline
INF = 4000*100001

def hatiho():
    global n, maps
    visit = [0 for i in range(n)]
    shortest = [INF for i in range(n)]
    now = 0
    shortest[0] = 0
    visit[0] = 1
    while 1:
        visit[now] = 1
        for next, dist in maps[now]:
            if visit[next]:
                continue
            shortest[next] = min(shortest[next], shortest[now]+dist)
        minv = INF
        next = now
        for i in range(n):
            if visit[i]==0 and shortest[i]<minv:
                minv = shortest[i]
                next = i
        if next==now:
            break
        now = next
    return shortest

def woo():
    global n, maps
    visit = [0 for i in range(n*2)]
    shortest = [INF for i in range(n*2)]
    now = 0
    shortest[now+1] = 0
    visit[now+1] = 1
    flag = 1
    while 1:
        visit[now*2+flag] = 1
        for next, dist in maps[now]:
            next*=2
            if visit[next+flag^1]:
                continue
            if flag==1:
                dist>>=1
            else:
                dist<<=1
            shortest[next+flag^1] = min(shortest[next+flag^1], shortest[now*2+flag]+dist)
        minv = INF
        next = now
        f = flag
        for i in range(n*2):
            if visit[i]==0 and shortest[i]<minv:
                minv = shortest[i]
                next = i//2
                f = i%2
        if next==now and flag==f:
            break
        now = next
        flag = f
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

#hatiho =
#print(hatiho())
#print(woo())
a = [hatiho(),woo()]
c = 0
for i in range(n):
    if a[0][i]<a[1][i]:
        c+=1
print(c)
'''
달빛 여우
풀이시간 : 이거까진 2h 25m

# 중복 방문이 가능하다는 점 간과 늑대시작점경우
# 못가는 땅이 있을 경우?
# 95% 실패
# 다른 파일 코드인 > 힙 쓰는걸로 바꿨더니 95%에서 틀렸였던게 45%인가 40%쯤에서 시간초과가 나온다

'''
