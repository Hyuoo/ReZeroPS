import heapq

def getmid(r,c):
    global img
    h = []
    for i in range(3):
        for j in range(3):
            heapq.heappush(h,img[r+i][c+j])
    for _ in range(4):
        heapq.heappop(h)
    return heapq.heappop(h)

r, c = map(int,input().split())
img = [list(map(int,input().split())) for _ in range(r)]
t = int(input())
gtt = 0
for i in range(r-2):
    for j in range(c-2):
        if getmid(i,j)>=t:
            gtt += 1
print(gtt)
'''
필터
풀이시간 : 20m

그냥 때려박으면 시간초과날것같아서
한참 고민하다가 r, c 범위 보니까 그렇게 안크네?
때려박으라는 문제같은데 혹시싶어서 문제분류 보니까 브루트포스 되어있어서 그냥 때려박음.

근데 힙도 왜쓴거임
'''
