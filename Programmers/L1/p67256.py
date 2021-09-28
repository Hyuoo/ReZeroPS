#코딩테스트 연습 > 2020 카카오 인턴십 > 키패드 누르기
#https://programmers.co.kr/learn/courses/30/lessons/67256

def distance(now, end, count):
    if count>4:
        return count
    if now==end:
        return count
    count+=1
    count = min(
    distance(now+1,end,count),
    distance(now-1,end,count),
    distance(now+3,end,count),
    distance(now-3,end,count)
    )
    return count
    
def solution(numbers, hand): # 0 -> 11
    answer = ''
    tmp=0
    nowL =10
    nowR =12
    for num in numbers:
        if num in [1,4,7]:
            tmp=0
        elif num in [3,6,9]:
            tmp=1
        elif num in [2,5,8,0]:
            if num==0:num=11
            ld=distance(nowL,num,0)
            rd=distance(nowR,num,0)
            if ld==rd:
                tmp = 1 if hand=="right" else 0
            else:
                tmp = 1 if ld>rd else 0
        if tmp:
            answer+="R"
            nowR=num
        else:
            answer+="L"
            nowL=num
    '''
    for num in numbers:
        if num in [1,4,7]:
            answer+="L"
            nowL=num
        elif num in [3,6,9]:
            answer+="R"
            nowR=num
        elif num in [2,5,8,0]:
            if num == 0:
                num = 11
            ld=distance(nowL,num,0)
            rd=distance(nowR,num,0)
            if ld==rd:
                if hand == "left":
                    answer+="L"
                    nowL=num
                else:
                    answer+="R"
                    nowR=num
                continue
            if ld<rd:
                answer+="L"
                nowL=num
            else:
                answer+="R"
                nowR=num
    '''
    return answer
