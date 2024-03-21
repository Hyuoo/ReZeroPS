"""
Solving Date    : 2024.03.21
Solving Time    : 26m
Title           : HTML
tags            : 문자열, 파싱
url             : https://www.acmicpc.net/problem/6581
runtime         : 40 ms
memory          : 31120 KB
"""

tokens = iter(open(0).read().split())
stdout = ""
line_count = 0

for token in tokens:
    if token == "<br>":
        stdout += "\n"
        line_count = 0
    elif token == "<hr>":
        if line_count:
            stdout += "\n"
            line_count = 0
        stdout += "-"*80 + "\n"
    elif line_count + len(token) + bool(line_count) <= 80:
        stdout += " "*(bool(line_count)) + token
        line_count += len(token) + 1
    else:
        stdout += "\n" + token
        line_count = len(token)

print(stdout)