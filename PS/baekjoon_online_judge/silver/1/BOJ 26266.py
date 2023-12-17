"""
Solving Date    : 2023.12.17
Solving Time    : 30m
Title           : 비즈네르 암호 해독
tags            : 수학, 문자열, 브루트포스 알고리즘, 정수론
url             : https://www.acmicpc.net/problem/26266
runtime         : 224 ms
memory          : 32900 KB
"""

p = input()
c = input()
l = len(p)

k = "".join(chr((ord(c[i])-ord(p[i])-1)%26+65) for i in range(l))

for i in range(1, l+1):
    if l%i: continue
    o = k[:i]
    for j in range(i, len(p), i):
        if k[j:j+i] != o: break
    else:
        print(o)
        break

"""
문제가 5%인가 6%에서 틀린다면
- 평문의 길이와 키의 길이가 동일 할 경우

그리고 시간이 너무 오래걸려서 뭐지 하고 보니,
- 키를 단순 반복해 평문과 동일한 길이를 만들 수 있는 경우만 고려한다.
라고 써 있는걸 보고 불필요한 반복을 없애줬다.

길이가 배수가 아닐경우 반복해서 남은부분을 잘라낼거라고 생각했다.

풀이:
(평문 + 키 = 암호문) 이기 때문에
(암호문 - 평문 = 키) 가 된다.
- A는 1이기 때문에 이에 맞춰서 역계산을 하면 바로 키값이 나온다.
다만 이 때 키 값은
문자열 길이만큼 반복이 되어있을 수 있기 때문에
- 반복되는 문자열을 찾으면 원래의 키 값이 된다.
"""