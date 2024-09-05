"""
Solving Date    : 2024.09.04
Solving Time    : -
Title           : 놀라운 문자열
tags            : 구현, 자료 구조, 문자열, 해시를 사용한 집합과 맵
url             : https://www.acmicpc.net/problem/1972
runtime         : 32 ms
memory          : 31120 KB
"""

def foo(txt):
    txt = txt.rstrip()
    l = len(txt)
    if l < 3:
        return f"{txt} is surprising."
    t = [*map(lambda x:ord(x)-65, txt)]
    flag = True
    for u in range(1, l):
        tmp = [0] * 677
        for s in range(l-u):
            h = t[s]*26+t[s+u]
            if tmp[h]:
                flag = False
                break
            tmp[h] = 1
        if not flag:
            break
    return f"{txt} is {''if flag else'NOT '}surprising."


print("\n".join([*map(foo, open(0))][:-1]))

"""
- 출력초과 왜 나는데
- 똑같이 2중포문에 set쓰는데 왜 나만 시간초과 나는데
"""