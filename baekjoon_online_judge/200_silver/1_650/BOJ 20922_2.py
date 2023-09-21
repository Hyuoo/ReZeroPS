"""
Solving Date    : 2023.09.21
Solving Time    : -
Title           : 겹치는 건 싫어
tags            : 투 포인터
url             : https://www.acmicpc.net/problem/20922
runtime         : 216 ms
memory          : 53144 KB
"""

n, k = map(int, input().split())
ar = [*map(int, input().split())]

num_count = [0 for _ in range(100001)]
max_len = 0
j = 0

for i, num in enumerate(ar):
    while num_count[num] == k:
        num_count[ar[j]] -= 1
        j += 1
    num_count[num] += 1
    max_len = max(max_len, i-j+1)

print(max_len)

"""
224ms -> (216,220)ms

enumerate를 안쓰고 그냥 num, now_len 해서 하니까 216ms 였긴한데
이게 코드가 너무 깔끔..

- 숫자 개수 +1 하는건 공통이고,
- 개수가 넘칠경우 빌때까지 뒤따라가면 끝.

끝.
"""