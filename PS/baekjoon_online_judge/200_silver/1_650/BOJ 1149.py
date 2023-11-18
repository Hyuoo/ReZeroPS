a=[0,0,0]
n=int(input())
for _ in range(n):
    r,g,b=list(map(int,input().split()))
    a=[min(a[1],a[2])+r,min(a[0],a[2])+g,min(a[0],a[1])+b]
print(min(a))
