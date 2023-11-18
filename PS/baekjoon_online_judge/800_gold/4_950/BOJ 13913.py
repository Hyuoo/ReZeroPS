from collections import deque
n,k = map(int,input().split())
s = [-1]*100001
q = deque([[-5, n, 0]])
while q:
    prev, now, t= q.popleft()
    if now < 0 or now > 100000 or s[now]!=-1:
        continue
    s[now] = prev
    if now == k:
        print(t)
        break
    t+=1
    q.append([now, now-1, t])
    q.append([now, now+1, t])
    q.append([now, now*2, t])
p = []
while k!=-5:
    p.append(k)
    k=s[k]
print(*reversed(p))
'''
숨바꼭질 4
풀이시간 : 13m
'''
