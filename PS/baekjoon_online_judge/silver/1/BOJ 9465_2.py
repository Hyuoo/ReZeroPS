"""
Solving Date    : 2024.03.21
Solving Time    : 8m
Title           : 스티커
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/9465
runtime         : 696 ms
memory          : 40880 KB
"""

for tc in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    
    acc = [0, 0]
    for i in range(n):
        acc = [
            max(acc[0], a[i]+acc[1]),
            max(acc[1], b[i]+acc[0])
            ]
    
    print(max(acc))


"""
재풀이.

"선택하지 않는" 불필요한 경우를 계산함을 제외
"""