"""
Solving Date    : 2024.05.17
Solving Time    : 9m
Title           : 대충 만든 자판
tags            : string, implement
url             : https://school.programmers.co.kr/learn/courses/30/lessons/160586
runtime         : - ms
memory          : - KB
"""

def solution(keymap, targets):
    answer = []
    keymap = {
        ch: (min([t for keys in keymap if ((t:=keys.find(ch))!=-1)] or [-1]))
        for ch in [chr(65+i) for i in range(26)]
    }
    
    for target in targets:
        tmp = len(target)
        for ch in target:
            if keymap[ch] == -1:
                tmp = -1
                break
            tmp += keymap[ch]
        answer.append(tmp)
    
    return answer