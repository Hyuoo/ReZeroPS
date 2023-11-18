import math

m = int(input())
n = int(input())

p = [1 for i in range(n+1)]
p[0], p[1] = 0, 0
for i in range(2, int(math.sqrt(n)+1)):
    if p[i]==1:
        for j in range(i*2,n+1,i):
            p[j] = 0

ans = []
for i in range(n-m+1):
    if p[m+i]==1:
        ans.append(m+i)

if ans:
    print(sum(ans))
    print(ans[0])
else:
    print(-1)
