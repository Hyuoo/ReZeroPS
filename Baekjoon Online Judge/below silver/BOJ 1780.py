import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dv(top,left,bot,right):
    global pp, count
    if left==right-1 and top==bot-1:
        return pp[top][left]

    offset = (right-left)//3
    tmp_count = [0,0,0]
    for i in range(3):
        for j in range(3):
            tmp=dv(top+offset*i, left+offset*j, top+offset*(i+1), left+offset*(j+1))
            if tmp!=-1:
                tmp_count[tmp]+=1

    if 9 in tmp_count:
        return tmp_count.index(9)
    else:
        for i in range(3):
            count[i]+=tmp_count[i]
        return -1

n=int(input())
pp=[list(map(lambda x:int(x)+1,input().split())) for _ in range(n)]
count = [0,0,0]

tmp = dv(0,0,n,n)
if tmp!=-1:
    count[tmp]+=1
print(*count,sep="\n")
'''
종이의 개수
풀이시간 : 43m

n^2짜리 비슷한 문제가 있었는디

풀이 :
분할정복으로 접근
좌상단과 우하단 (0,0)~(9,9)좌표를 주면
1칸짜리면 해당 칸 리턴,
3x3칸으로 쪼개지면 쪼갠다.

먼저 한 종이라는거랑 아니라는걸 구분하기위해서 값하나를 할당해야하는데
관례적으로 -1 쓰기위해서
입력받는 값들을 -1, 0, 1에서 +1씩 해서 012로 전환했다.

쪼개는 과정에서 각 9개 칸 판정해서
  - 한 종이라면 (9개가 다 같으면&&not -1)
  호출한 상위함수에서 개수 셀 것이므로 종류 값 리턴
  - 한 종이가 아니면
  모든 개수 다 세고 -1 리턴.
(각 분할에서 -1가 포함되면 어차피 어떤값도 9가 될 수 없으므로 각 개수 그대로 저장됨)


맨 처음 메인함수에서 호출하는것도 상위함수 개념으로 보고
-1이 아니면 해당 값 더해주는 식으로
1이 들어오거나 모든영역이 같을경우도 자연스레 처리된다.

-----
  이전에 2^n 문제를 풀 땐,
  먼저 싹다 더하고나서
  모든 칸이 같으면 -(2^n)을 한 다음 다시 +1을 하는 식으로 했는데
  이번엔 한번에 처리하게끔 다 같으면 해당값, 다르면 -1로 해서
  구역이 모두 일치하지않을때만 개수를 세는 식으로 해서
  마이너스연산 자체를 없앴다.
-----

끗
'''
