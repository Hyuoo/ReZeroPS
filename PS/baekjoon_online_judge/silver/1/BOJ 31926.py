"""
Solving Date    : 2024.05.28
Solving Time    : 36m
Title           : 밤양갱
tags            : 그리디 알고리즘, 애드 혹
url             : https://www.acmicpc.net/problem/31926
runtime         : 44 ms
memory          : 33240 KB
"""

import math
print(int(math.log2(int(input())))+10)

"""
"달디다"ㄴ를 얼마나 복사하느냐

수학적 풀이로 접근했다.
- 상대적으로 수학적이지 않은 풀이는 2배씩늘려가며 목표치를 넘기는지 반복하는 방법이 있다.


틀린풀이:
- 먼저 맨 처음 d a l d i dal g o 를 8회로 잡고
- 마지막 daldida n 은 2회로 잡고
- 중간 daldidalgo는 log2로 복사하면 된다고 생각해서

다음과 같이 생각했다.
앞 + 중간 + 마지막
8 + ceil(log2(n)) + 2


맞는풀이:
- daldidalgo 까진 똑같음
- 마지막 daldidan이 독립적이지 않고 
  daldidalgodaldida + n 으로 계산되어 1회 적게 계산할 수 있다.
    -> 마지막부분의 daldida까지 반복구간으로 계산.

- 결과적으로 n이 주어질 때, 시작-중간-끝은 다음과 같이 된다.
    - daldidalgo
    - (daldidalgo n-1번 daldida(n) 1번) = n번
    - n

- 그리고 계산해야 하는건 시작-중간 인 n+1번
- 1부터 시작해서 *2씩 (1+n)로 만들기 위한 횟수를 계산하면 된다.
    - n==1일 때, 2를 만드는데 1
    - n==2일 때, 3을 만드는데 2
    - n==3일 때, 4를 만드는데 2
    - n==4일 때, 5를 만드는데 3 ...

- 그래서 이 패턴이 나오는게 다음 두개
    - floor( log2( n ) ) + 10
    - ceil( log2( n+1 ) ) + 9
계산하면 끝난다.



===
패턴에 맞춰서 생각하는건 되는데
수학적으로 뭔지 명확하게 설명하는게 안된다.

막 갈겨적긴 했는데 패턴으로는 이해가 되는데
수학적으로 왜 저런지 이해가 딱 안된다. 심각쓰
"""