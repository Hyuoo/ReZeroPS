"""
Solving Date    : 2024.08.08
Solving Time    : 10m
Title           : 페그
tags            : 구현, 브루트포스 알고리즘
url             : https://www.acmicpc.net/problem/3010
runtime         : 32 ms
memory          : 31120 KB
"""

board = [input() for _ in range(7)]
rotate_b = ["" for _ in range(7)]

for i in range(7):
    for j in range(7):
        rotate_b[i] += board[j][i]

board.extend(rotate_b)
print(sum(map(lambda x:x.count(".oo") + x.count("oo."), board)))


"""
칩을 움직일 수 있는 "모든" 경우의 수를 구하는 문제

칩이 움직일 수 있는 조건은
- 칩이 있는 위치를 기준으로
- 다음칸에 칩이 있어야 하고
- 다다음칸은 빈칸이어야 한다.
즉, "oo." 또는 ".oo"패턴을 찾으면 된다.

굳이 인덱스를 통해서 찾지 않고 각 열끼리는 영향을 주지 않기 때문에
수평 수직 라인을 모두 문자열로 두고 count를 통해서 패턴을 찾아주었다.
"""