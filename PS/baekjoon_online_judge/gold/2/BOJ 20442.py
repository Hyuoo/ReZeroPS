"""
Solving Date    : 2023.09.24
Solving Time    : 1h 10m
Title           : ㅋㅋ루ㅋㅋ
tags            : 투 포인터
url             : https://www.acmicpc.net/problem/20442
runtime         : 2344 ms
memory          : 37560 KB
"""

kkr = input()
R = kkr.count("R")
# print(kkr)

l = 0
r = len(kkr) - 1
lk = rk = m = 0

while l <= r:
    # print(f"{'*' * l}{kkr[l:r + 1]}{'*' * (len(kkr) - r - 1)}", min(lk, rk) * 2 + R, "/", l, r, lk, rk)
    if R:
        m = max(m, min(lk, rk) * 2 + R)

    if lk < rk:
        if kkr[l] == "K":
            lk += 1
        else:
            R -= 1
        l += 1
    else:
        if kkr[r] == "K":
            rk += 1
        else:
            R -= 1
        r -= 1

print(m)

"""
무조건 양쪽에 K쌍이 맞거나,
+ 순수 R인 문자열 구하기.

1. 처음 재귀로 접근해서
    바깥쪽에서부터 K쌍 찾으면서 사이에 있는 R을
    매 함수호출마다 카운팅.
- 뭐가 잘못된지 기록을 안했네,


2. 그냥 문자열 양쪽에서 포인터로 줄여가면서
    K 쌍 맞으면, 사이에 있는 R 개수랑 더해서
    (K그냥 싹다 지나쳐오면서 min값으로 함.)
    그 중 최대값 출력

- 여기서 R을 세는 방법도
    처음엔 그냥 누적합으로 해서 구간합으로 했는데,
    굳이 그럴 필요 없이
    전체 R 개수 세어서, 포인터가 지나치는 개수만큼 빼주면 됨.


(3.) 내 풀이는 아닌데, 무조건 K쌍 맞을때까지 포인터 진행하고
    K+=2 하면서, 이후에 R 개수랑 합치는것도 가능. 
"""