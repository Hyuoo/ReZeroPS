#https://school.programmers.co.kr/learn/courses/30/lessons/92334
'''
2022 KAKAO BLIND RECRUITMENT 신고 결과 받기
풀이시간 : 25m +5m
========================================================
다른 풀이를 보고,
- set을 굳이 다 넣고나서 할 필요가 없고
  report 통째로 set을 하면 문제없이 중복신고가 사라진다.
- return 위의 두 개 블럭과 a_user도 필요가 없었다.
  바로 id_list.index(name)으로 ans변수 만들어서 하면 됐다.
========================================================
해서 수정한 코드.
report를 통째로 set 하는건 굳이 싶어서 안함.
set에 신고내역 만 저장하는게 더 나을 듯 싶어서

신고횟수 k미달도 따로 지우는 로직 없애고
아래에서 한번에 continue 하는걸로 변경.
'''
from collections import defaultdict

def solution(id_list, report, k):
    ans = [0] * len(id_list)
    b_user = defaultdict(set)
    
    for rep in report:
        a, b = rep.split()
        b_user[b].add(a)
    
    for names in b_user.values():
        if len(names) < k:
            continue
        for name in names:
            ans[id_list.index(name)] += 1
    
    return ans
