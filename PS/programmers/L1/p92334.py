#https://school.programmers.co.kr/learn/courses/30/lessons/92334
'''
2022 KAKAO BLIND RECRUITMENT 신고 결과 받기
풀이시간 : 25m

최근 배운 defaultdict라는 녀석을 이용해서 편하게 풀었다.
신고가 유효하든 아니든, 신고를 당한 입장에서 누가 신고했는지 기억해야하고,
유효한 신고이면 신고를 한 이들에겐 유효한신고횟수를 알려줘야한다.

절차적으로 차례차례 처리해서 푼 문제.

파이썬이라 쉽게 풀었다.
==========================================
다른 풀이를 보고,
- set을 굳이 다 넣고나서 할 필요가 없고
  report 통째로 set을 하면 문제없이 중복신고가 사라진다.
- return 위의 두 개 블럭과 a_user도 필요가 없었다.
  바로 id_list.index(name)으로 ans변수 만들어서 하면 됐다.
'''
from collections import defaultdict

def solution(id_list, report, k):
    a_user = defaultdict(int)
    b_user = defaultdict(set)
    
    for rep in report:
        a, b = rep.split()
        b_user[b].add(a)
    
    rm = []
    for name, rep_list in b_user.items():
        if len(rep_list) < k:
            rm.append(name)
    
    for d in rm:
        del b_user[d]
    
    for names in b_user.values():
        for name in names:
            a_user[name] += 1
    
    ans = []
    for name in id_list:
        ans.append(a_user[name])
    
    return ans
