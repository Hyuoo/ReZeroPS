#https://school.programmers.co.kr/learn/courses/30/lessons/138477
#코딩테스트 연습 > 연습문제 > 명예의 전당 (1)

def solution(k, score):
    answer = []
    mj = []
    for sc in score:
        if len(mj)<k:
            mj.append(sc)
        else:
            if sc>min(mj):
                del mj[mj.index(min(mj))]
                mj.append(sc)
        answer.append(min(mj))
    return answer
