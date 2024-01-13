"""
Solving Date    : 2024.01.08
Solving Time    : 20m
Title           : 가장 긴 바이토닉 부분 수열
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/11054
runtime         : 312 ms
memory          : 31120 KB
"""

n = int(input())
ar = [*map(int, input().split())]

left = [1 for _ in range(n)]
right = [1 for _ in range(n)]

for m in range(n):
    for l in range(m):
        if ar[l] < ar[m]:
            left[m] = max(left[l]+1, left[m])
    for r in range(n-1, n-m-1, -1):
        if ar[n-m-1] > ar[r]:
            right[n-m-1] = max(right[n-m-1], right[r]+1)

print(max([left[i]+right[i]-1 for i in range(n)]))

"""
LIS를 양방향으로 구한 뒤, 합쳤다.
중간 값은 좌, 우 겹쳤기 때문에 -1

*굳이 바깥 for문을 하나로 합쳐서 가독성과 해결시간을 손해봤다.
*춘배컵 나비와전봇대 문제에서 이런식의 수열이 나왔어서
 어 그때 이걸로 풀었어야 했나 했는데, 아니었다. 다행이
 이걸로 풀었으면 시간초과가 났을 것...
    (- 애초에 최장길이 vs 최근꺼 로 목표가 다름.) 
 이 수열에 대해 이름이 있다는것에 반가워서 쓰는 소리.
"""