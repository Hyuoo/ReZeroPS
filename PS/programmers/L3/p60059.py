"""
Solving Date    : 2023.12.05
Solving Time    : 1h 31m
Title           : 자물쇠와 열쇠
tags            : 구현
url             : https://school.programmers.co.kr/learn/courses/30/lessons/60059
runtime         : -
memory          : -
"""

def key_match(key, lock, iter_x, iter_y, v=False):
    """(Key기준위치, Lock크기)를 갖는 iteration 받아서 Key-Lock 매칭 시도"""
    for i, x in enumerate(iter_x):
        for j, y in enumerate(iter_y):
            # key[x][y]값을 가져와서 비교
            tmp_key = 0
            # key범위 밖이면 0으로 간주
            if x >= 0 and x < len(key) and y >= 0 and y < len(key):
                if v:
                    # 방향에 따라 안과 밖의 for문 순서를 바꿔줘야 함
                    tmp_key = key[y][x]
                else:
                    tmp_key = key[x][y]

            # key[x][y]와 lock[i][j]가 달라야 되므로 같으면 0(False)
            if tmp_key == lock[i][j]:
                return 0
    # 성공적으로 Lock 매칭이 끝나면 1(True)
    return 1


def solution(key, lock):
    answer = False
    # print(*[i for i in key], "=====", *[i for i in lock], sep="\n")
    n = len(key)
    m = len(lock)
    # Key의 모서리 한쪽만 걸칠수도 있으므로 범위바깥부터 탐색
    # 반복횟수는 n + (m-1) *2
    for i in range(1 - m, n):
        for j in range(1 - m, n):
            # [i:i+m][j:j+m] 범위의 key를 방향 회전해가며 매칭
            iter_x = [*range(i, i + m)]
            iter_y = [*range(j, j + m)]
            # 슬라이싱[::-1]을 통해서 리스트 뒤집기
            for rev_x, rev_y, v in zip([1, 1, -1, -1], [1, -1, -1, 1], [0, 1, 0, 1]):
                if key_match(key, lock, iter_x[::rev_x], iter_y[::rev_y], v=v):
                    answer = True
        # 반복 최소화
        if answer:
            break

    return answer

"""
2020 KAKAO BLIND RECRUITMENT
자물쇠와 열쇠

구현은 너무 어렵다.
레벨3으로 넘 어렵다니 갈길이 멀다.

일단.
- 자물쇠는 무조건 모든 범위를 스캔해야한다.
- 열쇠는 꼭 모든 범위를 스캔 할 필요는 없다.
- 열쇠범위 바깥의 자물쇠가 0이어도 다 채워져야 한다.

접근방식:
- 자물쇠 끝부분에 한칸이라도 열쇠가 걸치는 모든 범위
- 4방향
을 싹다 스캔한다. 끝.

iter_x, iter_y를 통해서 자물쇠를 비교 할 범위를 정하고
(v)ertical 플래그와 뒤집기를 통해서 열쇠의 회전을 구현했다.
"""