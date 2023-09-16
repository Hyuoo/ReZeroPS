"""
Solving Date    : 2023.09.14
Solving Time    : 7m
Title           : 베스트셀러
tags            : 자료구조, 문자열, 정렬, 해시를 사용한 집합과 맵
url             : https://www.acmicpc.net/problem/1302
runtime         : 40 ms
memory          : 31256 KB
"""

book = {}
for i in range(int(input())):
    bn = input()
    book[bn] = book.get(bn, 0) + 1
print(sorted(book, key=lambda x:(-book[x], x))[0])