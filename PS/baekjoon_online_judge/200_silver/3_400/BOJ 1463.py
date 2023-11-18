"""
Solving Date    : 2023.11.08
Solving Time    : 23m
Title           : 1로 만들기
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/1463
runtime         : 56 ms
memory          : 31120 KB
"""

def div(x, t):
    if x<4: return 1+t
    return min(div(x//3, x%3), div(x//2, x%2))+t+1

x = int(input())
print(div(x, 0) if x-1 else 0)

"""
'왜.. DP지..!?'

- 일단, 전체 경우를 따질 필요가 없다고 생각함.
    > '1을 뺀다' 에 해당하는 연산.
- DP를 하면 [-1, //2, //3] 이렇게 3개 경우를 따지는데
  1을 뺀다를 없애면 [//2, //3]만 하면 되고,
  백만에서 //2 //3만 하면
  값 줄어드는걸 보면, 속도는 오히려 더 빠를 거라 예상함.

근데 1이 답이 0이라는걸 생각안해서 시간 엄청씀
"""