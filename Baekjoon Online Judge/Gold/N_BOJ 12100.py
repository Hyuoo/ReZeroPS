import math

def process_line(dir):
    global n
    new_maps = [[0 for _ in range(n)] for _ in range(n)]
    if dir in "LlRr":
        for i in range(n):
            tmp = process_line_hor(i, dir)
            for j in range(n):
                new_maps[i][j] = tmp[j]
    elif dir in "UuDd":
        for i in range(n):
            tmp = process_line_ver(i, dir)
            for j in range(n):
                new_maps[j][i] = tmp[j]
    else:
        return -1
    return new_maps

def process_line_hor(line_number, dir):
    global maps, n
    l = [0 for _ in range(n)]
    if dir in "Ll":
        idx = 0
        t = 1
        direction = range(n)
    elif dir in "Rr":
        idx = n-1
        t = -1
        direction = reversed(range(n))
    else:
        return -1

    for i in direction:
        if maps[line_number][i]:
            if l[idx]==0:
                l[idx] = maps[line_number][i]
            elif l[idx]==maps[line_number][i]:
                l[idx]+=1
                idx+=t
            else:
                idx+=t
                l[idx] = maps[line_number][i]
    return l

def process_line_ver(line_number, dir):
    global maps, n
    l = [0 for _ in range(n)]
    if dir in "Uu":
        idx = 0
        t = 1
        direction = range(n)
    elif dir in "Dd":
        idx = n-1
        t = -1
        direction = reversed(range(n))
    else:
        return -1

    for i in direction:
        if maps[i][line_number]:
            if l[idx]==0:
                l[idx] = maps[i][line_number]
            elif l[idx]==maps[i][line_number]:
                l[idx]+=1
                idx+=t
            else:
                idx+=t
                l[idx] = maps[i][line_number]
    return l

def pp(maps):
    global n
    print("="*(2*n+1))
    for i in maps:
        print("",*i)
    print("="*(2*n+1))

n=int(input())
maps = [list(map(lambda x:int(math.log2(int(x))+1) if x!="0" else 0,input().split())) for _ in range(n)]

pp(maps)
pp(process_line("d"))

'''
2048 (Easy)
풀이시간 :
1h 10m - 기본기능구현 [process_line, process_line_hor, process_line_ver]


대충 아무 데이터
7
8 4 4 2 2 4 4
0 2 8 4 0 0 8
4 2 8 2 4 4 8
0 0 0 2 2 4 8
4 2 8 8 2 2 4
1 2 4 0 0 0 4
1 2 8 8 0 4 1

'''
