input()
a=sorted(map(int,input().split()))
t=0
s=0
for i in a:
    t+=i
    s+=t
print(s)
