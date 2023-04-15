#https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    answer = 0
    last = 0
    for s,e in sorted(targets):
        if last<=s:
            answer+=1
            last = e
            continue
        last = min(last, e)
    return answer
'''
요격 시스템
풀이시간 : 15

그대로 s,e순으로 정렬해서 모든 미사일을 다 쏴야하기때문에 그리디하게 접근
앞에서부터 겹치는거 제거하는식

*어라, 그럼 s는 오름차순, e는 내림차순 해야되는거 아님?
  => 어차피 s가 같은 경우에 e가 더 크더라도 더 작은 e 범위에서 고를 수밖에 없다.

새로운 폭격미사일을 만나면 이전 미사일 범위에서부터 줄여나간다.
범위 밖 미사일이 나오면 새 요격미사일.
'''
'''
https://school.programmers.co.kr/learn/courses/30/lessons/42884
프로그래머스 L3 단속카메라 완전 동일문제.
'''
