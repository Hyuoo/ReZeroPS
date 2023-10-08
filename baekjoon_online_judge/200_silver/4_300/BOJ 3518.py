"""
Solving Date    : 2023.10.05
Solving Time    : 18m
Title           : 공백왕 빈-칸
tags            : 구현, 문자열, 파싱
url             : https://www.acmicpc.net/problem/3518
runtime         : 144 ms
memory          : 40100 KB
"""

blank = []
buf = []
try:
    while 1:
        line = input()
        tmp = line.split()
        buf.append(tmp)
        for i, l in enumerate(tmp):
            if i < len(blank):
                blank[i] = max(blank[i], len(l))
            else:
                blank.append(len(l))
except:
    pass

print("\n".join("".join([f"{line[i]:{blank[i]+1}}" for i in range(len(line))]).rstrip() for line in buf))

"""
그냥.. 한줄로 쓰고싶었다...

근데 중간에도 rstrip 해줘야되는거 귀찮네

어쨋든 단어 당 최대 길이를 알려면 다 읽어야만 하기 때문에
한번 읽고, 최대 길이로 다시 문자 출력
끝.
"""