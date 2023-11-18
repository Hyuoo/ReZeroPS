def isCollision():
    global N
    global maps
    global baam_head
    x,y = baam_head
    if x<0 or y<0 or x>=N or y>=N:
        return True
    if maps[x][y]!=0:
        return True
    return False

def apple_check():
    global baam_head
    global apples
    if baam_head in apples:
        apples.remove(baam_head)
        eating_apple()

def eating_apple():
    # print("사과냠")
    global maps
    global baam_length
    n = len(maps)
    baam_length += 1
    for i in range(n):
        for j in range(n):
            if maps[i][j]!=0:
                maps[i][j] += 1

def time():
    global maps
    global global_time
    n = len(maps)
    global_time += 1
    for i in range(n):
        for j in range(n):
            if maps[i][j]!=0:
                maps[i][j] -= 1
    # print("째깍:",global_time)

def move():
    global baam_head
    global baam_ahead
    xx = (1*(baam_ahead%2))*(-2*(baam_ahead//2)+1) # 1, 3
    yy = (1*(baam_ahead%2^1))*(-2*(baam_ahead//2)+1) # 0, 2
    baam_head[0] += xx
    baam_head[1] += yy

def turn_check():
    global global_time
    global inst
    global ic
    if global_time == inst[ic][0]:
        turn(inst[ic][1])
        ic += 1

def turn(rotate):
    global baam_ahead
    r = {"L":3, "D":1}
    baam_ahead = (baam_ahead+r[rotate])%4
    # print("휘릭쓰", baam_ahead)

def game():
    global maps
    global baam_head
    global baam_length
    while True:
        x,y = baam_head
        maps[x][y] = baam_length
        move()
        # print(baam_head)
        if isCollision():
            return -1
        apple_check()
        time()
        turn_check()
        # for i in maps:
        #     print(i)
        # print("="*30)

baam_head = [0,0]
baam_ahead = 0 #rdlu 0123
apples = []
baam_length = 1
ic = 0

N = int(input()) # 보드크기 N
K = int(input()) # 사과 갯수 K

maps = [[0 for j in range(N)] for i in range(N)]
for i in range(K):
    x,y = map(lambda x:int(x)-1,input().split())
    apples.append([x,y])
# print(apples)

global_time = 0
inst = []
for i in range(int(input())):
    interval, rotate = input().split()
    interval = int(interval)
    inst.append([interval,rotate])
    # rotate L: left, D: right
inst.append([-1,""])

f = game()

print(global_time+1)

'''
뱀.
풀이시간 : 1h 33m

스네이크게임 구현하는 문제 (이 게임 이름이 'Dummy'였어?)

큐를 쓰면 맵이 없어도 되는데, 난 몸통 중간에 부딪힐때 큐를 다 돈다는게 싫어서
뱀이 몸통 흘리고다니는 느낌으로다가
맵에 현재길이만큼 시간 뒤 증발하는 몸뚱이를 설정했다.

뭔가 어중간하게 모듈화된것같아서 신경쓰이지만 일단은 문제풀이용이니 뭐

구현문제라 딱히 설명 쓸 게 없구만

'''
