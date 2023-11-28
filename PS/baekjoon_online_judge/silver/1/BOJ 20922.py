"""
Solving Date    : 2023.09.21
Solving Time    : 1h 11m
Title           : 겹치는 건 싫어
tags            : 투 포인터
url             : https://www.acmicpc.net/problem/20922
runtime         : 224 ms
memory          : 53144 KB
"""

n, k = map(int, input().split())
ar = [0]+[*map(int, input().split())]

num_count = [0 for _ in range(100001)]
max_len = -1
now_len = -1
i = 0

for num in ar:
    now_len += 1
    if num_count[num] == k:
        num_count[num] += 1
        f = 1
        while f:
            i += 1
            now_len -= 1
            num_count[ar[i]] -= 1
            if ar[i] == num:
                f = 0
    else:
        num_count[num] += 1
    max_len = max(max_len, now_len)

print(max_len)

"""
처음 접근을
숫자마다 개수를 세고, 숫자마다 큐를 사용해서
개수 초과한 숫자는 popleft 해서 가장 앞에있던 위치만큼 빼주는 식.
-> 전혀 틀린 풀이.
    1 2 3 4 2 1 이런식으로 중간에 낀 숫자가 있으면
    2 - 2, 1 - 1 이런식으로 매칭되어 안된다.


이후 한참 고민하다가
투포인터라는 힌트를 본 뒤에
다시 접근.

- 포인터 하나는 계속 1칸씩 진행하며 (길이+1, 숫자 카운트)
진행하다가 길이 초과 한 숫자가 나올 경우
- 다른 포인터가 맨 앞에서부터,
해당 숫자를 만날때까지 (개수-1, 길이-1)


* 224ms로 다른 엥간한 풀이보다 빠르다 굿
"""