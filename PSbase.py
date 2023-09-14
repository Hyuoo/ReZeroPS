import math
from math import sqrt
import heapq
from collections import defaultdict
from collections import Counter
from collections import deque
from functools import cmp_to_key
from functools import reduce
from itertools import permutations
from itertools import combinations
import random
from typing import *
import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt", 'r')
#MAX_LENGTH_79@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''CODE'''

"""
Solving Date    : 
Solving Time    : 
Title           : 
tags            : 
url             : 
runtime         : 
memory          : 
"""


# def getpi(p):
#     m = len(p)
#     j = 0
#     pi = [0 for _ in range(m)]
#
#     for i in range(1,m):
#         while j>0 and p[i]!=p[j]:
#             j = pi[j-1]
#         if p[i] == p[j]:
#             j += 1
#             pi[i] = j
#     return pi
#
# def kmp(s, p):
#     ans:int = []
#     pi = getpi(p)
#     n = len(s)
#     m = len(p)
#     j = 0
#     for i in range(0,n):
#         while j>0 and s[i]!=p[j]:
#             j = pi[j-1]
#         if s[i]==p[j]:
#             if j==m-1:
#                 ans.append(i-m+1)
#                 j = pi[j]
#             else:
#                 j+=1
#     return ans
#
# def pipi(string):
#     ar = getpi(string)
#     print(*string)
#     print(*ar)
#     print(kmp(string,"ABC"))
#     print()
# s = ["ABCDABCDABEED","ABCABCACC","ABCDCBA","ABCDABCD","ABABABABA","ABABABABAB","ABABCABCABD","ABCAABCABCABC"]
# for i in s:
#     pipi(i)


#
# def check():
#     pass
#
# for all_case in range(int(input())):
#     n = int(input())
#     arr = [*map(int,input().split())]
#     print(arr)

# def check1(s):
#     return len(set(s))>1
# def check2(s, k):
#     for i in range(len(s)-1):
#         for j in range(i+1,len(s)):
#             if (s[i]+s[j])%k==0:
#                 return False
#     return True
#
# n,k = map(int,input().split())
# ar = [*map(int,input().split())]
# count = 0
# for i in range(2, n):
#     for s in combinations(ar, i):
#         # print(s, "=", check1(s), check2(s, k))
#         if check1(s) and check2(s, k):
#             count+=1
#             # print(s)
# print(count%1000000007)

# for tc in range(int(input())):
#     input()

book = defaultdict(int)
for i in range(int(input())):
    book[input()] += 1
print(sorted(book, key=lambda x:(-book[x], x))[0])