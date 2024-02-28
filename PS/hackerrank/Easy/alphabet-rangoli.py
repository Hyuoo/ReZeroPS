"""
Solving Date    : 2024.02.28
Solving Time    : 10m
Title           : Alphabet Rangoli
tags            : String
url             : https://www.hackerrank.com/challenges/alphabet-rangoli/problem
runtime         : -
memory          : -
"""

def print_rangoli(size):
    n = size*2-1
    ar = [["-" for _ in range(n)] for _ in range(n)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (dis:=abs(size-i)+abs(size-j)) < size:
                ar[i-1][j-1] = chr(97+dis)
    print(*map(lambda a:"-".join(a), ar), sep="\n")

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)