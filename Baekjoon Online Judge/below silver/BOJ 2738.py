n,m = map(int,input().split())
a=[]
for i in range(n*2):
    l=list(map(int,input().split()))
    if i<n:
        a.append(l)
    else:
        for j in range(m):
            a[i%n][j]+=l[j]
for i in a:
    print(*i)
