"""
Solving Date    : 2023.10.27
Solving Time    : 12m
Title           : AC
tags            : 구현, 자료 구조, 문자열, 파싱, 덱
url             : https://www.acmicpc.net/problem/5430
runtime         : 156 ms
memory          : 45832 KB
"""

import sys
input = sys.stdin.readline

buf = ""
for _ in range(int(input())):
    func = input().rstrip()
    n = int(input())
    ar = input().rstrip().strip("[]").split(",")

    s = 0
    e = n
    p = 0  # 0: front, 1: back
    for op in func:
        if op == "R":
            p ^= 1
        elif op == "D":
            if p:
                e -= 1
            else:
                s += 1

    if s>e:
        buf += "error\n"
    else:
        tmp = ar[s:e]
        if p:
            tmp = reversed(tmp)
        buf += f"[{','.join(tmp)}]\n"

print(buf)

"""
굳이 배열을 막 조작 할 필요가 없다.

접근:
- 뒤집고, 버리는 연산 2개 뿐이기 때문에
  양쪽에서 하나씩밖에 줄어들지 못함.
- 처음 인덱스를 전체 배열로 두고,
  정방향이면 왼쪽에서 줄이고
  역방향이면 오른쪽이고 줄인다.
    - 인덱스가 결국 교차되면 에러 발생.
"""