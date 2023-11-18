#https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0
    # di = {"U":[1,0],"D":[-1,0],"L":[0,-1],"R":[0,1]}
    hor = [[0 for _ in range(10)] for _ in range(11)]
    ver = [[0 for _ in range(11)] for _ in range(10)]
    ch = [5,5]
    for d in dirs:
        if d=="U" and ch[0]+1<11:
            ver[ch[0]][ch[1]] = 1
            ch[0]+=1
        elif d=="D" and ch[0]-1>=0:
            ch[0]-=1
            ver[ch[0]][ch[1]] = 1
        elif d=="L" and ch[1]-1>=0:
            ch[1]-=1
            hor[ch[0]][ch[1]] = 1
        elif d=="R" and ch[1]+1<11:
            hor[ch[0]][ch[1]] = 1
            ch[1]+=1
    
    for i in hor:
        answer+=i.count(1)
    for i in ver:
        answer+=i.count(1)
    
    return answer
'''
방문길이
#KDT_코테스터디

좌하단이 0,0이라고 취급하고

교차로부분 기준이 아니라
가로 경로, 세로 경로 나눠서 생각.

갈 수 있으면 모두 체크하고
명령 실행 후 체크 수 카운트
'''
