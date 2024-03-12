"""
Solving Date    : 2024.02.19
Solving Time    : 1m
Title           : 덧칠하기
tags            : 
url             : https://school.programmers.co.kr/learn/courses/30/lessons/161989
runtime         : -
memory          : -
"""

def solution(n, m, section):
    p = section[0] + m
    answer = 1
    for i in section[1:]:
        if i < p:
            continue
        p = i+m
        answer += 1
    return answer