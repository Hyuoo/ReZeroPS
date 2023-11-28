"""
Solving Date    : 2023.11.14
Title           : Serca
tags            : 구현
url             : https://www.acmicpc.net/problem/26766
rank            : 4
byte            : 114 B
"""

s=""
n=0x5565545599545656545955946555649555589565589599586a56a4
while n:n>>=2;s+="\n @"[n&3]
print(s*int(input()))

"""
for n in [0x5565545599545656545955946555649555589565589599586a56a4]*int(input()):
    while n:n>>=2;print(end="\n @"[n&3])
122B -> 114B 위 코드로 변경
"""