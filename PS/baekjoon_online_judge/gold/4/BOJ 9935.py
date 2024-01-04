"""
Solving Date    : 2023.12.26
Solving Time    : 15m
Title           : 문자열 폭발
tags            : 자료 구조, 문자열, 스택
url             : https://www.acmicpc.net/problem/9935
runtime         : 364 ms
memory          : 42300 KB
"""

origin, expl = map(str.strip, open(0))
st = []
expl = list(expl)
l = len(expl)

for ch in origin:
    st.append(ch)
    if ch == expl[-1] and st[-l:] == expl:
        for _ in range(l):
            st.pop()

print(ans if (ans:="".join(st)) else "FRULA")

"""
폭발 문자열과 비교를 하는 과정에서
for문을 써서 차례로 비교하다가 멈추는게 빠를 것이라고 판단했는데
그냥 통째로 슬라이싱해서 비교하는게 더 빠르다.
"""