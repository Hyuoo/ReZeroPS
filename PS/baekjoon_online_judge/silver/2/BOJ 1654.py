k,n = map(int,input().split())
a=[int(input()) for _ in range(k)]
l,r = 1,max(a)
ans = 0
while l<=r:
    m = (l+r)//2
    s = sum(map(lambda x:(x//m),a))
    if s>=n:
        ans = m
        l=m+1
    else:
        r=m-1
print(ans)
'''
랜선 자르기
풀이시간 : 20m

나는 바봉가봉가
'''
