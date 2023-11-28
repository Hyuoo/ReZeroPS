"""
Solving Date    : 2023.11.02
Title           : 좋은 자동차 번호판
tags            : 구현, 문자열
url             : https://www.acmicpc.net/problem/1871
rank            : 6
byte            : 116 B
"""
for i in[*open(0)][1:]:a,b=i.split("-");t=0;print("not "*(abs([t:=t*26+ord(c)-65for c in a][-1]-int(b))>100)+"nice")