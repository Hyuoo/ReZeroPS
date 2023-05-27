a,b=map(int,input().split())
t=iter((" "*9+"\n")*10)
for i in sorted(range(a,b+1),key=lambda n:["jeihcbgfad"[int(i)]for i in str(n)]):print(i,end=next(t))
