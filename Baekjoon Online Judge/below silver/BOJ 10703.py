import sys
input = sys.stdin.readline
r,s=map(int,input().split())
pic = [list(input()) for _ in range(r)]
min_gap = r
gap = 0
for h in range(s):
    for v in reversed(range(r)):
        if pic[v][h]=="#":
            gap = 0
        elif pic[v][h]=="X":
            min_gap = min(min_gap, gap)
            break
        else:
            gap+=1
for h in range(s):
    for v in reversed(range(r-1)):
        if pic[v][h]=="X":
            pic[v][h] = "."
            pic[v+min_gap][h] = "X"
print("".join(map(lambda x:"".join(x),pic)).rstrip())
'''
유성
풀이시간 : 1시간넘게?
#KDT_코테스터디

1. 혹시나 갭이 0일 경우가 있을까 마지막에 X>. 순으로 대입하면 안될줄알았는데,
  -> 풀이 완료 후 바꿔서 제출해도 정상 정답
2. 유성이 없이 갭 계산이 끝날 경우 최소값갱신하면 안되어서 elif안으로 넣음.

아무리 생각해도 문제가 없는데 안풀려서 뭐가문제지 했다가
문제 놓고 다시 와서 "."을 굳이 elif로 넣어야되나 해서 else로 옮겼더니
통과함.

뭐지
무조건 [X#.]세개중에 들어오는거면 문제없어야되는거 아닌가?

진짜 혹시나싶어 rstrip도 넣었으나 이건 상관없음. > 시간 다소 줄어들어서 넣음.

암튼 풀이:
1. 수직으로 모든 유성-땅 중 가장 짧은거리 구하기
2. 유성을 1.에서의 거리만큼 내리기.
3. 시간초과땜에 print한번만 쓰도록 합쳐서 출력.
'''
