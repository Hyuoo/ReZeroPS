#LEVEL2
#코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 메뉴 리뉴얼
#https://programmers.co.kr/learn/courses/30/lessons/72411

#combinations란 놈을 알았다
import itertools
def solution(orders, course):
    answer = []
    for c in course:
        comb = []
        di = dict()
        for o in orders:
            comb += itertools.combinations(sorted(o),c)
        for i in comb:
            if(di.get(i)):
                di[i] +=1
            else:
                di[i] = 1
        if(di):
            answer+=[key for key, val in di.items() if max(di.values())==val and max(di.values())>1]
    return sorted(["".join(a) for a in answer])
#평균적으론 이놈이 더 실행시간이 빠르지만 헤비해질수록 기하급수로 실행시간이 올라감
