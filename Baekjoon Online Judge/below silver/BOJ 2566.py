a = [list(map(int,input().split())) for i in range(9)]
m = -1
x,y=0,0
for i in range(9):
    for j in range(9):
        if a[i][j]>m:
            m=a[i][j]
            x=i+1
            y=j+1
print(f"{m}\n{x} {y}")
