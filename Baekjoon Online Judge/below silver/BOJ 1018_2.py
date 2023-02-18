def check(x,y):
    f=1
    c=0
    for i in range(8):
        for j in range(8):
            if a[x+i][y+j]==f:
                c += 1
            f^=1
        f^=1
    return c
m,n = map(int,input().split())
a = [list(map(lambda x:(1 if x=="W" else 0), input())) for _ in range(m)]
mini = 66
for i in range(m-7):
    for j in range(n-7):
        c = check(i,j)
        mini = min(mini,c,abs(64-c))
print(mini)
'''
체스판 다시 칠하기

진짜로 다시 칠했다.
다시 브루트포스 생각없이 하니까 3분컷 실화냐
'''
