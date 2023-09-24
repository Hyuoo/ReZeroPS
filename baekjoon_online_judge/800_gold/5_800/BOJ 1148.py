"""
Solving Date    : 2023.09.24
Solving Time    : 30m
Title           : 단어 만들기
tags            : 구현, 문자열
url             : https://www.acmicpc.net/problem/1148
runtime         : 2744 ms
memory          : 45128 KB
"""

import sys
input = sys.stdin.readline

word_set = []
while 1:
    line = input().rstrip()
    if line == "-":
        break
    word_set.append(line)
# print(word_set, len(word_set))

while 1:
    line = input().rstrip()
    if line == "#":
        break
    puzzle = line
    # puzzle_spell = Counter(puzzle)
    puzzle_spell = {}
    for p in puzzle:
        puzzle_spell[p] = puzzle_spell.get(p, 0) + 1
    puzzle_able = {k: 0 for k in puzzle}

    for word in word_set:
        # word_spell = Counter(word)
        word_spell = {}
        for w in word:
            word_spell[w] = word_spell.get(w, 0) + 1
        # print(word, end =": ")
        for ch in word_spell:
            if puzzle_spell.get(ch, 0) - word_spell[ch] < 0:
                # print("불가능")
                break
        else:
            # print("가능")
            for ch in word_spell:
                puzzle_able[ch] += 1
    # print(puzzle_able)

    spell_min = [200001, ""]
    spell_max = [-1, ""]
    for k, v in puzzle_able.items():
        if spell_min[0] > v:
            spell_min[0] = v
            spell_min[1] = [k]
        elif spell_min[0] == v:
            spell_min[1].append(k)
        if spell_max[0] < v:
            spell_max[0] = v
            spell_max[1] = [k]
        elif spell_max[0] == v:
            spell_max[1].append(k)

    print("".join(sorted(spell_min[1])), spell_min[0], "".join(sorted(spell_max[1])), spell_max[0])

"""
- 아예 max(),min() 함수써서 하는건 성능에 큰 영향이 없다.
- Counter를 쓰던걸 안쓰게 바꾼거하나로 시간이 확 줄었다.
    - 3688 ms -> 2744 ms

모든 주어진 단어를
9개 스펠링을 사용해서
- 가장 많이 만들 수 있는 스펠링과
- 가장 적게 만들 수 있는 스펠링 찾기

퀴즈판별로
    각 단어 별로 만들 수 있는지
        만들수 있는단어에 있는 스펠링 카운트
이후 종합하여 출력
"""