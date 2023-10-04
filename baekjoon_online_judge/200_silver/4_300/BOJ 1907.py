"""
Solving Date    : 2023.10.04
Solving Time    : 32m
Title           : 탄소 화합물
tags            : 구현, 문자열, 브루트포스 알고리즘, 파싱
url             : https://www.acmicpc.net/problem/1907
runtime         : 40 ms
memory          : 31256 KB
"""

def split_all(string, sep):
    ret = []
    buf = ""
    for ch in string:
        if ch in sep:
            ret.append(buf)
            buf = ""
        else:
            buf += ch
    ret.append(buf)
    return ret

def count_elements(exp):
    ret = {e:0 for e in "CHO"}
    buf = ""
    for c in exp:
        if c>"1" and c<="9":
            ret[buf] += int(c)-1
        else:
            ret[c] += 1
            buf = c
    return ret

new_dict = lambda a, n, b, m: {c: a[c]*n + b[c]*m for c in "CHO"}
mul_dict = lambda a, n: {c: a[c]*n for c in "CHO"}

exp = input()
x = list(map(count_elements, split_all(exp, "+=")))

try:
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                if new_dict(x[0], i, x[1], j) == mul_dict(x[2], k):
                    print(i,j,k)
                    raise
except:
    pass

"""
항상 고정된 원소 3개만 검사하고, 수가 많지 않기때문에
그냥 3*3 배열 만들어서
쉽게 인덱스 순서로 처리하는게 효율적.

-----------
try:
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                for c in "CHO":
                    if x[0][c]*i + x[1][c]*j != x[2][c]*k:
                        break
                else:
                    print(i,j,k)
                    raise
except:
    pass

else쓰는게 왠지 파이써닉... 한가?
"""