#https://school.programmers.co.kr/learn/courses/30/lessons/132265
'''
롤케이크 자르기
풀이시간 : 19m

배열을 한 기준에서 양쪽으로 잘라서 들어있는 "종류의 수"가 같도록하는 경우 구하기.
처음에 count로 날먹하려다 시간초과로 실패

리스트 한번만 돌아도 되게끔 다시 구성.
아래와같이 두번 스캔해서 끝.
딕셔너리만 쓰면 len()할때 또 시간들까봐 변수따로 씀.

근데 이제보니까 꼭 갯수를 세지 않아도 되네
'''
from collections import defaultdict
def solution(topping):
    answer = 0
    lc = 0
    rc = 0
    l = defaultdict(int)
    r = defaultdict(int)
    for i in topping:
        if r[i]==0:
            rc+=1
        r[i]+=1
    for i in topping:
        if l[i]==0:
            lc+=1
        l[i]+=1
        r[i]-=1
        if r[i]==0:
            rc-=1
        if lc==rc:
            answer+=1
    return answer
