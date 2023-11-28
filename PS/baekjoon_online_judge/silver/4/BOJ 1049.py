n,m = map(int,input().split())
pack, unit = 1000, 1000
for _ in range(m):
    a,b = map(int, input().split())
    pack = min(pack,a)
    unit = min(unit,b)
ans = 0
if pack<unit*6:
    ans+=n//6*pack
    n%=6
print(min(ans+(n//6+1)*pack,ans+n*unit))

'''
기타줄

이거 푸는데 40분인가 걸림;;
에바다
'''
