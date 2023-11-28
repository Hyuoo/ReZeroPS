def cutting(n,h):
    global trees
    ret = 0
    i=0
    while i<n and trees[i]>h:
        ret += trees[i]
        i+=1
    return ret-i*h

n,m = map(int,input().split())
trees = sorted(map(int,input().split()),reverse=True)

l = 0
r = trees[0]

while l<=r:
    h = (l+r)//2
    get = cutting(n,h)
    if get<m:
        r = h-1
    else:
        l = h+1
print(r)

'''
나무 자르기
풀이시간 : 18m

나무자른길이로 이분탐색.

고려할톱날 높이 l~r (=0,max())
매 가능한 높이 중간값으로 가져가는 길이 계산해서
같거나 크면 높이 올려보기 (가져가는 값 줄임)
작으면 높이 낮추기 (가져가는 값 늘림)
=================================================
#KDT_코테스터디 재풀이
풀이시간 : 23m

더오래걸렸네
가져가는나무 정렬 안해서 시간초과로 시간걸림.

컷팅 과정에서 연산을 줄여서 실행시간이 단축됨.
=> 3456ms > 3172ms

====== 이전코드
def cut(a, n, m):
    s = 0
    i = n-1
    while i>=0 and a[i]>m:
        s+=a[i]-m
        i-=1
    return s
n,m = map(int,input().split())
a = sorted(map(int,input().split()))
l, r = 0, a[-1]
while l<=r:
    h = (l+r)//2
    c = cut(a,n,h)
    if c>=m:
        l=h+1
    elif c<m:
        r=h-1
print(r)
======

'''
