import sys
sys.setrecursionlimit(10**9)
'''
격자칸에서 0:빈칸, 1:집, 2:치킨집
각 집에서 제일 가까운 치킨집까지의 거리가 "치킨 거리"
N*N 크기의 맵에서
M이상의 치킨집이 있는데,
M개의 치킨집 만을 선택할 때
모든 집의 치킨거리의 합이 최소일 때의 [치킨 거리의 합]을 구하는 문제.

접근.
먼저 치킨집을 M개만 선택을 해야하는데..
  제일 먼저 생각 난 것이 그냥 모든 경우의수로 치킨집 선택하면서 총 치킨거리 무식하게 구하기.
  근데 무식한 방법은 언제나 차선책인법
  1. 각 1(집)에서 최소거리인 2(치킨집)의 거리를 기억하기
  2. 각 2(치킨집)에서 모든 1(집)의 거리 합을 기억하기
  3. 각 1(집)에서 최소거리에 있는 2(치킨집)에 가중치를 더해주기
  
  1. => 치킨집을 없앨 때 마다 갱신을 해 줘야 하고, 없앨 치킨집을 그냥 고를수도 없고 다른 절차가 더 필요함.
      모두 갱신을 안 하려면 집과 최소거리인 치킨집을 연결하면 되는데 복잡해짐.
      그냥 도움이 안됨
      예제3같은경우만 봐도 무슨 근거로 없앨 지 불명확.
      (어라 아예 맵이 아니라 집, 치킨집만 있는 가중치 그래프로 만들면? {*1})
  2. => 거리 합이 작은것부터 M개를 고른다. 하면 될 줄 알았는데,
      예제2만 봐도 이 케이스에서 왼쪽아래 (0,1)의 치킨집과 (3,0) (4,1)이 모두 총 합이 같다.
      (0,1)이 남기기 최적임에도 오른쪽아래의 섬에 영향을 많이 받아 선택을 못하는 경우가 생긴다.
      기각.
  3. => 1과 비슷한 맥락.
  
아몰랑 그냥 무식하게 풀어
  1. 전체 치킨집에서 M개의 치킨집만 고르기
    = 재귀+백트래킹으로 모든 경우 다 검사.
  2. 1.에서 만들어진 모든 경우에 대해 모든 치킨거리 계산하여 더하기
  3. 끝

================================
itertools.combinations(LIST, N) 이라는 걸로 쉽게 1.의 경우케이스 만드는게 된다더라.
'''

def get_chick_length(selected):
    min_length=99999
    total_length = 0
    for i in range(len(maps)):
        for j in range(len(maps)):
            if maps[i][j] == 1:
                min_length = 99999
                for y,x in selected:
                    min = abs(y-i)+abs(x-j)
                    if min_length > min:
                        min_length = min
                total_length += min_length
    return total_length

def select_chick_house(selected, M, i, j):
    if selected and len(selected) == M:
        return get_chick_length(selected)
    shortest_chick_length = 9999999
    while(i<len(maps)):
        while(j<len(maps)):
            if maps[i][j]==2:
                chick_length = select_chick_house(selected+[[i,j]], M, i, j+1)
                if shortest_chick_length > chick_length:
                    shortest_chick_length = chick_length
            j+=1
        j=0
        i+=1
    return shortest_chick_length

N, M = map(int, input().split())
maps = [None for _ in range(N)]
for i in range(N):
    maps[i] = list(map(int,input().split()))
print(select_chick_house([], M, 0, 0))
