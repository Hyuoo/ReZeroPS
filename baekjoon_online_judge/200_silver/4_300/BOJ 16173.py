def trv(i,j):
    global maps, n
    if i>=n or j>=n or maps[i][j]==0:
        return 0
    if i==n-1 and j==n-1:
        return 1
    c = 0
    c+=trv(i+maps[i][j],j)
    c+=trv(i,j+maps[i][j])
    return c

n=int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
print("HaruHaru" if trv(0,0) else "Hing")

'''
점프왕 쩰리 (Small)
풀이시간 : 5m
'''
