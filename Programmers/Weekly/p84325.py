#LEVEL1
#코딩테스트 연습 > 위클리 챌린지 > 4주차 > 직업군 추천하기
#https://programmers.co.kr/learn/courses/30/lessons/84325

def solution(table, lang, prefer):
    answer = ''
    size = len(lang)
    max = 0
    
    for str in table:
        ar = str.split()
        score=0
        for i in range(5):
            for j in range(size):
                if ar[1+i]==lang[j]:
                    score+=(5-i)*prefer[j]
                    
        if max<score:
            max = score
            answer = ar[0]
        elif max==score:
            answer = answer if answer<ar[0] else ar[0]
            
    return answer
