"""
Solving Date    : 2023.09.16
Solving Time    : 22m
Title           : 후위 표기식
tags            : 자료 구조, 스택
url             : https://www.acmicpc.net/problem/1918
runtime         : 40 ms
memory          : 31256 KB
"""

precedence = {
    "*": 1,
    "/": 1,
    "+": 3,
    "-": 3,
    "(": 5,
    ")": 0,
}

st = []
infix = input()
postfix = ""

for c in infix:
    # print(c, end =": ")
    if c not in precedence:
        postfix += c
    else:
        if c == "(":
            st.append(c)
        elif c == ")":
            while st and st[-1] != "(":
                postfix += st.pop()
            st.pop()
        else:
            while st and precedence[c] >= precedence[st[-1]]:
                postfix += st.pop()
            st.append(c)
    # print(postfix, st)

while st:
    postfix += st.pop()

print(postfix)

"""
중위표기식을 후위표기식으로 전환하는 문제

스택 이용해서 연산자만 우선순위대로 재배치 하면 되는 문제.

..

예전에 자료구조 배우면서
스택 배우고 계산기 한다고 두어번 만들었는데
다시 하려니 은근 바로바로 생각 안난다.

우선순위를 어떻게 설정하고 어떻게 쌓아야되더라~

그리고 이게 골드 2나 된다니 싶다.
하긴 안배우고 풀려면 생각하는데 상당히 걸릴 듯
"""