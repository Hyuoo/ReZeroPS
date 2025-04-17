"""
최대공약수(GCD;Greatest Common Divisor)
최소공배수(LCM;Least Common Multiple)

유클리드 호제법을 통해서 두 수 사이의 최대 공약수를 구하는 알고리즘


math.gcd 함수는 3.5버전부터 추가되었다.
+(3.9 이후부터는 세 개 이상의 인자도 지원)

math.lcm 함수는 3.9버전부터 추가
(여러 인자 가능)
"""

from math import gcd, lcm

def _gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return _gcd(b, a%b)

def _lcm(a: int, b: int) -> int:
    return (a*b) // _gcd(a, b)


if __name__ == "__main__":
    print(gcd(3, 5), _gcd(3, 5))  # 1
    print(gcd(15, 5), _gcd(15, 5))  # 5
    print(gcd(60, 14), _gcd(60, 14))  # 2
    print(gcd(123, 3), _gcd(123, 3))  # 3
    print(gcd(123, 13), _gcd(123, 13))  # 1
    
    print("="*20)

    print(lcm(10, 3), _lcm(10, 3))  # 30
    print(lcm(7, 5), _lcm(7, 5))  # 35
    print(lcm(7, 8), _lcm(7, 8))  # 56
    print(lcm(123, 13), _lcm(123, 13))  # 1599

    print("-"*20)


    ## 시간 측정?
    if 0:
        import timeit
        import random
        t = zip([random.randint(1, 1000) for _ in range(100)],
         [random.randint(1, 1000) for _ in range(100)])
        fa = """
for a, b in t:
    foo(a, b)
"""
        
        tmp = lambda x:print(f"{x.__name__}:", timeit.timeit(fa,setup=f"foo={x.__name__}", number=10000000, globals=globals()))

        tmp(_gcd)
        tmp(gcd)
        tmp(_lcm)
        tmp(lcm)
        """number=10000000
        _gcd: 0.3025370879995535
        gcd: 0.31298251499993057
        _lcm: 0.28175971299970115
        lcm: 0.3093033289997038
        """
        """number=300000000
        _gcd: 8.960910357000103
        gcd: 8.85278799400021
        _lcm: 9.042148268999881
        lcm: 8.853052089999437
        """