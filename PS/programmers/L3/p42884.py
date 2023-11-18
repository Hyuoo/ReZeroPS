#https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    last = -30001
    for s,e in sorted(routes):
        if last<s:
            answer+=1
            last = e
            continue
        last = min(last, e)
    return answer
'''
단속카메라
풀이시간 : 0m

요격시스템(https://school.programmers.co.kr/learn/courses/30/lessons/181188)
문제와 동일한 문제.
근데 요격은 L2, 얘는 L3?

변수 last 값이랑 if비교문 이퀄 두개만 고치면 똑같은코든디
'''
