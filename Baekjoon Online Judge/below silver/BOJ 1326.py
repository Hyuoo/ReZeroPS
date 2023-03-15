from collections import deque
def f(a,b):
    global n, maps, visit
    q = deque([a])
    visit[a] = 0
    while q:
        a = q.popleft()
        for i in range(a%maps[a],n,maps[a]):
            if visit[i]==-1:
                visit[i] = visit[a]+1
                q.append(i)

n=int(input())
maps=list(map(int,input().split()))
a,b=map(lambda x:(int(x)-1),input().split())
visit = [-1 for i in range(n)]
f(a,b)
print(visit[b])
'''
폴짝폴짝
풀이시간 : 52m

큐 없이 하려다 생고생하고 큐로 푼

'''
