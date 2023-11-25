"""
Solving Date    : 2023.11.25
Solving Time    : -
Title           : 어려운 스케줄링
tags            : 자료 구조, 정렬, 오프라인 쿼리, 덱
url             : https://www.acmicpc.net/problem/26086
runtime         : 120 ms
memory          : 40900 KB
"""

import sys
input = sys.stdin.readline

N, Q, k = map(int, input().split())
ops = [input().rstrip() for _ in range(Q)]

sorted_ar = []
sort_flag = 0
tmp = [[], []]
cur = 0
for op in ops:
    if op=="1":
        for t in tmp:
            sorted_ar.extend(t)
        sort_flag = cur
        tmp = [[], []]
    elif op=="2":
        cur ^= 1
    else:
        tmp[cur].append(int(op.split()[1]))

res = tmp[0][::-1] + sorted(sorted_ar, reverse=sort_flag) + tmp[1]
print(res[-k if cur else k-1])

"""
2022 Sogang Programming Contest > Master (Open) E번

- 무조건 앞에서부터 스케줄을 삽입한다.
- 정렬은 맨 마지막 한번만 실행하면 결과는 똑같다.
- 뒤집기는 매번 뒤집을 필요 없이 deque를 사용해서 앞, 뒤에 붙여 오버헤드를 줄임.

풀이:
정렬이전 리스트와 정렬된 리스트 기준으로 좌, 우에 오는 리스트를 구분해서 입력받았다.
정렬이 나올때마다 임시배열에 일단 넣고 마지막에 정렬했다. 


문제를 푸는 과정에서 정렬 한 리스트를 뒤집는걸 생각을 안해서 매우 오래걸렸다.
"""