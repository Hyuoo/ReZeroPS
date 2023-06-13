n=int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))[:-1]
m = 1e9
ans = 0
for i in range(n-1):
    m = min(m,cost[i])
    ans += m*dist[i]
print(ans)

'''
주유소
풀이시간 : 10m
#KDT_코딩테스트

그리디 문제

무조건 지금까지 중 싼곳에서 넣어야 이득.

지나온 곳 중 최소값을 저장한 뒤, 새로운 거리는 항상 이 최소값으로 계산해서 넣는다.

끗
'''
