"""
Solving Date    : 2023.11.08
Title           : 1로 만들기
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/1463
rank            : 11
byte            : 77 B
"""

f=lambda x:0 if x<2else min(f(x//3)+x%3,f(x//2)+x%2)+1
print(f(int(input())))

"""
- 숫자하나만 입력이면
  *open(0) 보다 input() 이 1바이트가 짧다.
- 상수도 키워드랑 붙여써도 되는구나.
"""