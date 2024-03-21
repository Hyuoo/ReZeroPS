"""
Solving Date    : 2024.03.21
Solving Time    : 40m
Title           : HTML 에디터
tags            : https://www.acmicpc.net/problem/4752
url             : 문자열, 파싱
runtime         : 40 ms
memory          : 31120 KB
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def parse_line(line):
    for _ in range(2):
        l, _, line = line.partition(" ")
        yield int(l)
    yield line

def get_all_tags(text):
    tags = []
    tag_set = set()
    i = 0
    while i < len(text):
        if text[i] == "<":
            s, e = i, text.find(">", i)
            tag = text[s:e+1]

            if tag[1] == "/":
                tag_name = tag[2:-1]
            else:
                tag_name = tag[1:-1]

            if tag_name in tag_set:
                tag_set.remove(tag_name)
                tags.pop()
            else:
                tag_set.add(tag_name)
                tags.append(tag)
            
            i = e
        i += 1
    return tags


while True:
    # B E TEXT
    # >> [B, E)
    B, E, TEXT = list(parse_line(input()))
    if B==-1 and E==-1:
        break
    l = "".join(get_all_tags(TEXT[:B]))
    r = "".join(get_all_tags(TEXT[E:]))

    print("{open_tags}{text}{close_tags}".format(
        open_tags = l,
        text = TEXT[B:E],
        close_tags = r,
    ))

"""
왜 플레지
"""