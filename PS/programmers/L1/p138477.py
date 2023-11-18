#https://school.programmers.co.kr/learn/courses/30/lessons/138477
#코딩테스트 연습 > 연습문제 > 명예의 전당 (1)

'''
#그냥 풀이
def solution(k, score):
    answer = []
    mj = []
    for sc in score:
        if len(mj)<k:
            mj.append(sc)
        else:
            if sc>min(mj):
                del mj[mj.index(min(mj))]   # mj.remove(min(mj))
                mj.append(sc)
        answer.append(min(mj))
    return answer
'''
#힙을 이용한 풀이
import heapq as h
def solution(k, score):
    answer = []
    a=[]
    for sc in score:
        if len(a)>=k:
            if a[0]<sc:
                h.heappop(a)
                h.heappush(a,sc)
        else:
            h.heappush(a,sc)
        answer.append(a[0])
    return answer
