'''
https://school.programmers.co.kr/learn/courses/30/lessons/17683
"망할 문제/.."
문자열다루는 문제.
재생시간 분단위로 음이 반복되는 사이에 "방금 들었던 멜로디 m" 이 있으면 해당 제목.
중복이면 재생시간긴거, 이것도 중복이면 기존 입력에서 순서 빠른 순

단순히 쪼개서, 멜로디 길이만큼 커버 되게 늘리고, in으로 비교했다.

근데 어이없는게
[ 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다. ]
라고 해놓고 (None)이 코드영역으로 되어있고, 파이썬을 쓰니 자연스레 "(None)"이 None을 말하는 건줄 알았는데
문자열 "(None)"을 반환해야 하는게 답이었다.

킹받네
---
23.06.08 KDT코테스터디 재풀이 코드변경
'''
def get_t(time):
    h,m=map(int,time.split(":"))
    return h*60+m

def solution(m, musicinfos):
    repl = [["C#","c"],["D#","d"],["F#","f"],["G#","g"],["A#","a"]]
    for old, new in repl:
        m = m.replace(old, new)
    find = []
    for i, musicinfo in enumerate(musicinfos):
        s,e,title,melody = musicinfo.split(",")
        play=get_t(e)-get_t(s)
        for old, new in repl:
            melody = melody.replace(old, new)
        melody = melody*(play//len(melody)+1)
        if m in melody[:play]: # [:play] >> TC30
            find.append([-play,i,title])
    if find:
        return sorted(find)[0][2]
    else:
        return "(None)"
