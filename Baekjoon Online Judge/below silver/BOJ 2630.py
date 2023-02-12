def devide(i, j, n):
    global ar, color
    if n==1:
        color[ar[i][j]] += 1
        return ar[i][j]
    m = n//2
    blue = 0
    for x,y in [[0,0],[0,m],[m,0],[m,m]]:
        blue += devide(i+x,j+y,m)
    if blue == n**2:
        color[1] -= 3
    elif blue == 0:
        color[0] -= 3
    return blue

N = int(input())
ar = [list(map(int,input().split())) for _ in range(N)]
color = [0,0] #0:w 1:b
devide(0,0,N)
print(*color,sep="\n")
'''
색종이 만들기
풀이시간 : 31m

4분할로 나눠서 1칸단위로 흰/파 갯수 다 세고, (n크기에서 m크기로 4분할, n==1이면 칸 값 셈)
합치면서 전 영역이 흰색이거나 파랑 => (파랑이 n**2개 또는 0개)
이면
나눠서 센 4영역 빼고 (-=4)
합쳐진 영역 1개 추가 (+=1)
해서 -=3 해준다.

끝
'''
