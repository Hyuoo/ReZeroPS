#코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방
#https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    ENTER = lambda x: f"{x}님이 들어왔습니다."
    LEAVE = lambda x: f"{x}님이 나갔습니다."
    answer = []
    user_list = dict()
    log = []
    
    for r in record:
        ar = r.split()
        uid = ar[1]
        if(ar[0]=="Enter"):
            user_list[uid] = ar[2]
            log.append([ENTER,uid])
        elif(ar[0]=="Leave"):
            log.append([LEAVE,uid])
        elif(ar[0]=="Change"):
            user_list[uid] = ar[2]
            
    for ent,uid in log:
        answer.append(ent(user_list[uid]))
    return answer
