"""
Solving Date    : 2024.02.24
Solving Time    : 33m
Title           : 파일명 정렬
tags            : string, implement
url             : https://school.programmers.co.kr/learn/courses/30/lessons/17686
runtime         : -
memory          : -
"""

from functools import cmp_to_key

def split_file_name(file_name):
    tmp = ""
    flag = 0
    for ch in file_name:
        if flag == 0 and "0" <= ch <= "9":
            yield tmp.lower()
            tmp = ""
            flag += 1
        elif flag == 1 and not "0" <= ch <= "9":
            yield int(tmp)
            tmp = ""
            flag += 1
        tmp += ch
    if flag == 1:
        yield int(tmp)
    else:
        yield tmp


def cmp_func(a, b):
    if a[1] > b[1]:
        return 1
    elif a[1] < b[1]:
        return -1
    else:
        if a[2] > b[2]:
            return 1
        elif a[2] < b[2]:
            return -1
    return 0


def solution(files):
    # name<= A-Z, a-z, 0-9, " .-"
    # " .-"는 문자열
    # startwsith A-Z, a-z, 숫자 무조건 포함
    # HEAD / NUMBER / TAIL => str / int / None|Any
    # for file in files:
    #     print(file, ":", list(split_file_name(file)))

    return [files[i[0]] for i in sorted([[idx] + list(split_file_name(file)) for idx, file in enumerate(files)], key=cmp_to_key(cmp_func))]

"""
2018 KAKAO BLIND RECRUITMENT [3차] 파일명 정렬

- head, number, tail 세 부분 잘라서
- 원래 인덱스를 포함하여 새 리스트를 만들고
- 정렬 기준대로 정렬해서
- 원래 인덱스 위치의 값으로 리스트를 만들었다.

cmp_to_key를 사용해서 커스텀 정렬기준으로 정렬했다.


.. SQL아니고 코드에서는 정규식이랑 안친해진다.
.. 왠지 안쓰게됨;

===
막 하다보니 숏코딩이 되어 대강 풀어 쓴 버전

tmp = []
for idx, file in enumerate(files):
    tmp.append([idx]+list(split_file_name))
sorted_ar = sorted(tmp, key=cmp_to_key(cmp_func))
return [files[i[0]] for i in sorted_ar]
"""