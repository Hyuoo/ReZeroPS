"""
Solving Date    : 2024.09.05
Solving Time    : 32m
Title           : 로마 숫자
tags            : 수학, 구현, 문자열
url             : https://www.acmicpc.net/problem/2608
runtime         : 40 ms
memory          : 31120 KB
"""

rom_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def rom_to_arab(txt):
    ret = 0
    prev = 1001
    for ch in txt:
        num = rom_dict[ch]
        ret += num
        if prev < num:
            ret -= prev*2
        prev = num
    return ret

def arab_to_rom(num):
    """
    자릿수 별 0~9 케이스
    (A: 해당자리1, B: 해당자리5, C: 다음자리1)
    0 = None = None
    1 = 1 = A
    2 = 11 = AA
    3 = 111 = AAA
    4 = 15 = AB
    5 = 5 = B
    6 = 51 = BA
    7 = 511 = BAA
    8 = 5111 = BAAA
    9 = 110 = AC
    n % 5
    """
    
    nx = iter("IVXLCDM"[i:i+3] for i in [0, 2, 4])
    ret = ""
    while num:
        n = num%10
        A, B, C = next(nx, "M  ")
        if n%5 != 4:
            ret += (A*(n%5) + B*(n//5))
        else:
            if n//5:
                ret += (C+A)
            else:
                ret += (B+A)
        num //= 10
    return ret[::-1]


a = rom_to_arab(input()) + rom_to_arab(input())
print(a)
print(arab_to_rom(a))