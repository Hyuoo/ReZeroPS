M=0
s=0
for i in range(4):
    m,p = map(int,input().split())
    s+=p-m
    M=max(M,s)
print(M)
