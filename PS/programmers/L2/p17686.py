"""
Solving Date    : 2024.02.24
Solving Time    : 33m
Title           : 파일명 정렬
tags            : string, implement
url             : https://school.programmers.co.kr/learn/courses/30/lessons/17686
runtime         : -
memory          : -
"""

def split_file_name(file_name):
    tmp = ""
    flag = 0
    for ch in file_name:
        if flag == 0 and "0"<=ch<="9":
            yield tmp.lower()
            tmp = ""
            flag += 1
        elif flag == 1 and not "0"<=ch<="9":
            yield int(tmp)
            flag += 1
        tmp += ch
    if flag == 1:
        yield int(tmp)


def solution(files):
    # name<= A-Z, a-z, 0-9, " .-"
    # " .-"는 문자열
    # startwsith A-Z, a-z, 숫자 무조건 포함
    # HEAD / NUMBER / TAIL => str / int / None|Any
    # for file in files:
    #     print(file, ":", list(split_file_name(file)))

    return [i[0] for i in sorted([[file]+list(split_file_name(file)) for file in files], key=lambda x:(x[1], x[2]))]

"""
2018 KAKAO BLIND RECRUITMENT [3차] 파일명 정렬

- head, number, tail 세 부분 잘라서
- 원래 인덱스를 포함하여 새 리스트를 만들고
- 정렬 기준대로 정렬


.. SQL아니고 코드에서는 정규식이랑 안친해진다.
.. 왠지 안쓰게됨;

===
막 하다보니 숏코딩이 되어 대강 풀어 쓴 버전

tmp = []
for file in files:
    tmp.append([file]+list(split_file_name(file)))
sorted_ar = sorted(tmp, key=lambda x:(x[1], x[2]))
return [i[0] for i in sorted_ar]
"""