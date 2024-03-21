"""
Solving Date    : 2024.03.21
Solving Time    : 47m
Title           : 아스키 아트 표
tags            : 구현
url             : https://www.acmicpc.net/problem/9336
runtime         : 44 ms
memory          : 31120 KB
"""

import sys
input = sys.stdin.readline

def input_line():
    _, *ar = map(int, input().split())
    ar = list(zip(ar[::2], ar[1::2]))
    return ar

def set_ascii(m, ascii):
    # [ver, hor]
    cells = [[[1, 1] for _ in range(9)] for _ in range(m)]
    i = j = 0
    n = 0
    for asci in ascii:
        j = 0
        for asc in asci:
            while cells[i][j] != [1, 1]:
                # 병합된 셀 스킵
                j += 1
            ver, hor = asc
            for x in range(i, i+ver):
                for y in range(j, j+hor):
                    if i!=x:
                        cells[x][y][0] = 0
                    if j!=y:
                        cells[x][y][1] = 0
            j += hor
        n = max(n, j)
        i += 1
    return ([row[:n] for row in cells], n)

def draw_ascii(m, n, cells):
    # print(cells)
    ret = ""
    
    for i in range(m):
        hr = ""
        for j in range(n):
            hr += " --" if cells[i][j][0] else "   "
        ret += hr.rstrip()+"\n"
        for j in range(n):
            if cells[i][j][0] and cells[i][j][1]:
                ret += f"|{i+1}{j+1}"
            elif cells[i][j][1]:
                ret += "|  "
            else:
                ret += "   "
        ret += "|\n"
    ret += " --"*n
    return ret


if __name__ == "__main__":
    tmp = []
    while 1:
        m = int(input())
        if m == 0:
            break
        ascii = [input_line() for _ in range(m)]
        cells, n = set_ascii(m, ascii)
        fig = draw_ascii(m, n, cells)
        tmp.append(fig)

    print("\n\n".join(tmp))


"""
접근:
각 셀 마다 왼쪽, 위쪽이 벽이 있는지 없는지 여부를 체크하고
이를 기반으로 그림을 그린다.

풀이방법:
1. 각 세트를 입력받아 라인별로 처리한다. (set_ascii함수)
    - 각 셀의 default값은 [1, 1]로 벽이 모두 존재함을 뜻함.
        - [1, 1]은 병합되지 않은 셀임을 나타냄.
    - 병합되지 않은 경우, 병합되는 셀 전체를 돌며 벽을 없앰 (=0)
        - 합치는 정보가 겹치는 경우가 없기 때문에
          어딘가 병합 된 셀(!=[1, 1])이면 건너 뜀
          (예외처리 X)
    - 수평 병합의 경우에는 병합된 수만큼 column번호를 증가시킴
    - column이 몇갠지 주어지지 않기 때문에
        - max()를 통해서 구함(=n)
        - 열 길이를 최대인 9로 선언하고 n으로 잘라서 반환
2. 모든 셀에 대한 벽 정보에 따라 ascii문자를 구성하여 반환한다. (draw_ascii함수)
    - 수직 벽을 먼저 처리하고, 수평 벽을 따로 처리
    - 수직 벽 " -- -- --"
        - 공백으로 끝 날 경우 rstrip을 해주기 위해 별도 버퍼 변수를 사용함.
    - 수평 벽 + 셀번호
        - 벽이 둘 다 있을 경우, 셀 번호까지 출력
        - 수평 벽만 있을 경우 벽만 출력
        - 아니면 공백 출력
    - 마지막 수직 벽은 무조건 column 수 만큼 (n)
3. 모두 반복하여 "\n\n".join()하여 출력한다.
"""