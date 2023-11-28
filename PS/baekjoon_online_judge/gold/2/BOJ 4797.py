"""
Solving Date    : 2023.10.09
Solving Time    : 1h 6m
Title           : 화학
tags            : 구현, 자료 구조, 문자열, 파싱, 스택
url             : https://www.acmicpc.net/problem/4797
runtime         : 52 ms
memory          : 31256 KB
"""

def update_exp(elements, element, C):
    if not element:
        return elements
    C = C if C else 1
    if isinstance(element, str):
        elements[element] = elements.get(element, 0) + C
    elif isinstance(element, dict):
        for k, v in element.items():
            elements[k] = elements.get(k, 0) + v*C
    return elements

def foo(exp):
    elements = {}
    element = ""
    C = 0
    i = 0
    while i < len(exp):
        ch = exp[i]
        if ch>="A" and ch<="Z":
            update_exp(elements, element, C)
            C = 0
            element = ch
        elif ch>="a" and ch<="z":
            element += ch
        elif ch>="0" and ch<="9":
            C = C*10 + int(ch)
        elif ch=="(":
            update_exp(elements, element, C)
            # 업뎃 후 항상 0으로 초기화..
            C = 0
            sub_elements, nxt = foo(exp[i+1:])
            i += nxt
            element = sub_elements
        elif ch==")":
            return update_exp(elements, element, C), i+1
        i += 1
    elements = update_exp(elements, element, C)
    # print(elements, end="\t")
    return elements

try:
    while 1:
        exp = input()
        # print(exp, end=": ")
        elements = foo(exp)
        print("+".join([f"{'' if elements[k]==1 else elements[k]}{k}" for k in sorted(elements)]))
except:
    pass

"""
자알 구현하면 되는 문제.
사실 반례 얻으려고 구글에 한번 쳐봤는데
나오는거 없어서 그냥 쌩으로 함..

화학식 파싱 잘 하고, 괄호에 따른 배수처리 잘 해주면 되는 문제.

**딕셔너리에 원소별로 저장하면서**
앞에서부터 읽어나가면서
- 원소는 문자
- 서브그룹은 딕셔너리
로 전체 원소를 계속 업데이트
서브그룹은 재귀식으로 해서 다음 숫자만큼 전체 원소를 곱해줬다. 

H2O: 2H+O
(AlC2)3Na4: 3Al+6C+4Na
(Al2C2)3Na4: 6Al+6C+4Na
H2O2: 2H+2O
HHH: 3H
H(HH): 3H
H(H)H: 3H
(H(H))H: 3H
((H)H)H: 3H
((H)): H
(((((H2)2)2)2)2)2: 64H
CH3COOH: 2C+4H+2O
CH3C(OOH)10: 2C+13H+20O
(Ba2Na3Cl4)10: 20Ba+40Cl+30Na
PM(OH(HONa)2)3P: 9H+M+6Na+9O+2P
A3(BC)2: 3A+2B+2C

.. 무수한 케이스..

- 숫자는 무조건 원소 뒤에 위치
    - 원소는 서브화학식?이 될 수도 있다.
- 원소는 무조건 대문자로 시작 이후 소문자.
- 괄호 안에 있는 수는 모두 이후 숫자만큼 곱함.

풀면서 부딪힌 반례케이스가
- 다중 괄호
- 괄호로 끝날 경우
    - 서브그룹으로 끝날 경우
- 괄호 이후 숫자로 끝날 경우
- 괄호 시작 전 숫자일 경우
    - (line:40에서 C=0안해서 거의 20분동안 외않된데 한듯)
이정도?

그 외 같은원소 다른위치 이런거는 알아서 해결 됐고

- if else문을 괄호로 안묶어줘서 논리에러가 나기도 했다.

오 근데 오늘 기준으로 맞힌사람 26명이네 레어해
"""