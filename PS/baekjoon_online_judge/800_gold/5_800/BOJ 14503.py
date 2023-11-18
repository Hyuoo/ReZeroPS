inputs=lambda:map(int,input().split())

n,m=inputs()
x,y,d=inputs()

dr=[[-1,0],[0,1],[1,0],[0,-1]]
maps=[[*inputs()] for _ in range(n)]
dirty=[[1^maps[i][j] for j in range(m)] for i in range(n)]

c=0
while 1:
    if maps[x][y]:
        break
    if dirty[x][y]:
        dirty[x][y]=0
        c+=1
    if sum([dirty[x+tx][y+ty] for tx, ty in dr])==0:
        tx,ty=dr[d]
        x-=tx
        y-=ty
    else:
        while 1:
            d=(d-1)%4
            tx,ty=dr[d]
            if dirty[x+tx][y+ty]:
                x+=tx
                y+=ty
                break
print(c)
'''
로봇 청소기
풀이시간 : 34m
#KDT_코테스터디

일단 고려 :
1. 가장자리가 모두 벽. 예외처리 X
2. 후진하는 경우 아니면, 벽 갈 일 X
3. 후진하는 경우 아니면, 중복방문 X

접근 :
벽인지 아닌지 여부 상관없이 접근하고,
청소가 되어있는지 안되어있는지 여부로 맵 순회. (벽 = 청소완료)

풀이 :
0. 현재위치가 벽이면 후진하다 막힌거니 종료
1. 현재위치가 더러우면 청소하고,
2. 4칸 청소할 칸 여부??
  2.1 4칸 다 깨끗
    - 무조건 후진. 어차피 멈추면 (0.)조건에서 멈춤.
    -- 어 근데 이 안에서 여부 체크해주는게 실행시간 적게 들지않을까?
      -- 백준채점에선 일단 아님
  2.2 더럽
    - 반시계 회전
    2.2.1 더럽? 앞으로
'''
