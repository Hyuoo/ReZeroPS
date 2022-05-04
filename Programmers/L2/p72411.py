#LEVEL2
#코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 메뉴 리뉴얼
#https://programmers.co.kr/learn/courses/30/lessons/72411

import itertools

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
