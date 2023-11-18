from collections import deque
n, k = map(int,input().split())
q = deque([[n,0]])
v = [0]*100001
while q:
    now, t = q.popleft()
    if now<0 or now>100000 or v[now]:
        continue
    if now==k:
        print(t)
        break
    v[now] = 1
    j = now
    while j<100001 and j!=0 and j<=k*2:
        if v[j]==0:
            q.appendleft([j,t])
        j*=2
    q.append([now+1,t+1])
    q.append([now-1,t+1])
'''
숨바꼭질 3
풀이시간 : 22m
'''
