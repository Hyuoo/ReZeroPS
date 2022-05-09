#LEVEL2
#코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 메뉴 리뉴얼
#https://programmers.co.kr/learn/courses/30/lessons/72411
    #2트 한것보다 얘가 더 성능은 좋음 (빅오낮음)
''' 시간초과로 실패한 코드
import itertools
> itertools의 product를 사용하고, 전처리 하는데에 많은 시간 소요 예상 -> 대체함수 작성 product, rec
def solution(orders, course):
    answer = []
    all_case = []
    
    for i in orders:
        all_case+=list(map("".join,map(sorted,(map(set,itertools.product(i,repeat=max(course)))))))
    all_case = list(set(all_case))
    dekiru = [[] for _ in range(len(course))]
    for case in all_case:
        for i, c in enumerate(course):
            if(len(case) == c):
                dekiru[i] += [case]
    
    for i, deki in enumerate(dekiru):
        check_len = course[i]
        memo_count = []
        for de in deki:
            count = 0
            for order in orders:
                word_len = 0
                for d in de:
                    if d in order:
                        word_len += 1
                if(word_len == check_len):
                    count += 1
            memo_count.append(count)
        if(memo_count):
            memo_max = max(memo_count)
            if(memo_max<2):
                break
            for j, m in enumerate(memo_count):
                if(m == memo_max):
                    answer.append(dekiru[i][j])
    
    return sorted(answer)
'''

def rec(arr,mkstring,origin, n):
    if(n==0 or len(origin)<1):
        arr.append(mkstring)
    else:
        for i, st in enumerate(origin):
            arr.append(mkstring)
            rec(arr,mkstring+st,origin[i+1:],n-1)
            
def product(string,m):  #문자열 카티션곱 만드는 함수, 중복배제
    arr = []
    for i, st in enumerate(string):
        rec(arr,st,string[i+1:],m-1)
    return arr

def solution(orders, course):
    answer = []
    all_case = []   #가장 큰 코스 개수만큼 가능한 경우 전체 저장
    
    for i in orders:
        all_case+=product(sorted(i),max(course))
    all_case = set(all_case)    #굳이 list(set()) 안하고 그냥 set상태로 다음시퀀스
    
    dekiru = [[] for _ in range(len(course))]   #각 코스 개수별로 분리 dekiru[0]는 course[0]개의 메뉴로 가능한 경우의 수
    for case in all_case:
        for i, c in enumerate(course):
            if(len(case) == c):
                dekiru[i] += [case]
    
    for i, deki in enumerate(dekiru):   #가능한 코스별로 몇명이 주문했는지 각 메모 deki-> 같은개수의 모든 코스 list
        check_len = course[i]
        memo_count = []
        for de in deki: # de -> 하나의 코스 str
            count = 0
            for order in orders:
                word_len = 0
                for d in de:
                    if d in order:
                        word_len += 1
                if(word_len == check_len):
                    count += 1
            memo_count.append(count)
        if(memo_count): #가능한 코스가 없을경우 값이 없을 수도 있음
            memo_max = max(memo_count)
            if(memo_max<2):
                break
            for j, m in enumerate(memo_count):
                if(m == memo_max):
                    answer.append(dekiru[i][j])
    
    return sorted(answer)
