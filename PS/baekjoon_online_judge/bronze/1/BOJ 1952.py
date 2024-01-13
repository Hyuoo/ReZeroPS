"""
Solving Date    : 2024.01.08
Solving Time    : 13m
Title           : 달팽이2
tags            : 수학, 구현, 시뮬레이션
url             : https://www.acmicpc.net/problem/1952
runtime         : 44 ms
memory          : 31120 KB
"""

m, n = map(int, input().split())
print((min(m, n)-1)*2 + (m>n))

"""
뭔가 규칙이 보이는데 싶어서 규칙 찾아서 풀이.

한 줄씩 진행 할 때마다 남은 과정에서는 한 줄씩 없어진다는
부분 문제로 나눠서 푼 느낌?

5 3을 예로 들면 한줄을 진행한 이후에는
- 꺾어지는 횟수가 +1되고
- 남은 과정은 4 3이 된다
4 3에서는 또 한줄 진행하면
- 꺾어지는 횟수 +1
- 남은 과정은 4 2
...
이렇게 접근했다. 
"""