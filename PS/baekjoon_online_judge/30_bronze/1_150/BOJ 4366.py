"""
Solving Date    : 2023.10.09
Solving Time    : 20m
Title           : Average Speed
tags            : 수학, 구현, 문자열, 사칙연산, 파싱
url             : https://www.acmicpc.net/problem/4366
runtime         : 40 ms
memory          : 31256 KB
"""

try:
    dis = 0
    prev_t = 0
    prev_sp = 0
    while 1:
        q = input()
        t, sp = q[:8], q[9:]
        h, m, s = map(int, t.split(":"))
        now_t = h*60*60 + m*60 + s
        dis += (now_t-prev_t)*prev_sp
        prev_t = now_t
        if sp:
            prev_sp = int(sp)
        else:
            print(f"{t} {dis/3600:.2f} km")
except:
    pass

"""
거리 계속 누적시키면서
속도 변경하고
출력
"""