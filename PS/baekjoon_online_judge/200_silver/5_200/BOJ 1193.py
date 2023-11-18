'''
S5 분수찾기
풀이시간 : 26m

지그재그다. 항상 우상단에서 내려오는줄 알았다.
'''
x = int(input())
n=1
while x>(n*(n+1))//2:
    n+=1
l=1
r=n
for i in range(x-(n*(n-1))//2-1):
    l+=1
    r-=1
if n%2:
    l,r=r,l
print(f"{l}/{r}")
