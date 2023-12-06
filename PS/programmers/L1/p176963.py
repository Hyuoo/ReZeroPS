"""
Solving Date    : 2023.12.01
Solving Time    : 3m
Title           : 추억 점수
tags            : dictionary
url             : https://school.programmers.co.kr/learn/courses/30/lessons/176963
runtime         : -
memory          : -
"""

def solution(name, yearning, photo):
    d = {n:y for n, y in zip(name, yearning)}
    return [sum(d.get(p, 0) for p in pho) for pho in photo]
