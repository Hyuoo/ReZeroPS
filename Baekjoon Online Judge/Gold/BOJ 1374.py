import heapq
import sys
input = sys.stdin.readline
a = []
r = []
ans = 0
n = int(input())
for _ in range(n):
    _,b,c = map(int,input().split())
    a.append([b,c])
a.sort()
for i in range(n):
    s,e = a[i]
    if r and r[0]<=s:
        heapq.heappop(r)
        heapq.heappush(r,e)
    else:
        heapq.heappush(r,e)
        ans+=1
print(ans)
'''
강의실
풀이시간 : 26m

그냥 그리디인데 왜 골드지 하고 생각했는데
시간초과 해결하는 문제
'''
