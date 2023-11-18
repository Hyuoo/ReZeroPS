s = lambda a,b:int((a+b-1)/2*(b-a))
n,l = map(int,input().split())
ans = [-1]
for ll in range(l,101):
    m=0
    M=n//l
    while m<=M:
        a = (m+M)//2
        r = s(a,a+ll)
        if n<=r:
            ret=(r,a)
            M=a-1
        else:
            m=a+1
    if n==ret[0]:
        ans = range(ret[1],ret[1]+ll)
        break
print(*ans)
'''
수열의 합

숫자개수 늘려가면서
ll개일 때 합이 되는 수열이 있는지 이분탐색으로 
'''
