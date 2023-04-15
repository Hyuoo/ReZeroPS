def srch(row, col, old, now, new):
    global r,c,img,ans
    if ans[row][col]!=0:
        return
    soted = []
    o, i, j = 0,0, 0
    while i<9:
        if old and o<3 and old[o]==now[i]:
            i+=1
            o+=1
            continue
        if new and j<3 and now[i]>=new[j]:
            soted.append(new[j])
            j+=1
        else:
            soted.append(now[i])
            i+=1
    while new and j<3:
        soted.append(new[j])
        j+=1
    ans[row][col] = soted[4]
    #print("[%2d][%2d] ="%(row, col),old, now, new)
    if col + 1 < c - 2:
        r_old = sorted([img[row + i][col] for i in range(3)])
        r_new = sorted([img[row + i][col + 3] for i in range(3)])
        srch(row, col + 1, r_old, soted, r_new)
    if row + 1 < r - 2:
        d_old = sorted([img[row][col+i] for i in range(3)])
        d_new = sorted([img[row+3][col+i] for i in range(3)])
        srch(row+1, col, d_old, soted, d_new)

r, c = map(int,input().split())
img = [list(map(int,input().split())) for _ in range(r)]
ans = [[0 for _ in range(c-2)] for _ in range(r-2)]
t = int(input())
srch(0,0,[], sorted([img[i//3][i%3] for i in range(9)]),[])
gtt = 0
for a in ans:
    for b in a:
        if b>=t:
            gtt+=1
print(gtt)
'''
필터
재귀버전

혹시 빨라질까 싶었지
속도는 그대로 메모리는 살짝 줄음 (?)

> readline 바꾼게 속도줄이는법...
'''
