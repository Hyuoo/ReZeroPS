"""
Solving Date    : 2024.02.21
Solving Time    : 25m
Title           : 201. Bitwise AND of Numbers Range
tags            : bitmask
url             : https://leetcode.com/problems/bitwise-and-of-numbers-range/?envType=daily-question&envId=2024-02-21
runtime         : 53 ms
memory          : 16.54 MB
"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = left
        bit = 1
        while bit <= left:
            if ans&bit and ans+bit <= right:
                ans -= bit
            bit <<= 1
        return ans

"""
left, right범위 내에 해당 자릿수가 0인게 하나라도 있으면 0.
전체 숫자를 보기엔 불필요하게 오래걸려서
자릿수를 0으로 만드는 숫자가 범위에 포함되는지 체크를 하는 방식으로 풀이했다.

풀이:
- left를 기준으로 잡고 최하위비트부터 차례로 스캔 (bit <<= 1)
    - 현재 비트가 1일 경우 (ans&bit)
    - 해당 비트를 0으로 만드는 가장 작은 수(and+bit)가 범위 내에 포함(<=right)되면
    - 해당 비트를 0으로 만든다. (ans -= bit)

===
leetcode는 런타임이랑 메모리가 너무 편차가 크다.
위 코드로 똑같이 3번 제출 했는데,
[53ms, 16.54MB], [61ms, 16.48MB], [38ms, 16.66MB]
나왔다.
"""