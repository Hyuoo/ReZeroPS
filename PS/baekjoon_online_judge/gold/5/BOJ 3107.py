"""
Solving Date    : 2024.03.05
Solving Time    : 10m
Title           : IPv6
tags            : 구현, 문자열
url             : https://www.acmicpc.net/problem/3107
runtime         : 40 ms
memory          : 31120 KB
"""

answer = ["0000" for _ in range(8)]

parts = input().split(":")
if len(parts) == 8:
    answer = [*map(lambda x:x.zfill(4), parts)]
else:
    if parts[0]:
        for i, p in enumerate(parts):
            if not p:
                break
            answer[i] = p.zfill(4)
    
    if parts[-1]:
        for j, p in enumerate(parts[::-1]):
            if not p:
                break
            answer[7-j] = p.zfill(4)

print(":".join(answer))

"""
코드길이가 무려 444
...

각 콜론으로 자른 뒤 축약이 있을 경우에는(::) -> 길이가 8이 안되니.
- 왼쪽에 붙어있는 부분은 왼쪽부터 채워주고
- 오른쪽에 붙어있는 부분은 오른쪽부터 채워주고
자연스레 가운데는 비어있을거고.

끝

"::"를 포함하는지로 축약 여부를 판단할수도 있지만,
어차피 잘라서 처리하고 붙일거라 자르는방식으로.
"""