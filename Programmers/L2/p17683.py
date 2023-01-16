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
'''
def conv_time(time):
    h,m = time.split(":")
    return int(m)+int(h)*60
def conv_melody(m):
    for a,b in (["A#","a"],["C#","c"],["D#","d"],["F#","f"],["G#","g"]):
            m = m.replace(a,b)
    return m
def solution(m, musicinfos):
    answer = ''
    m = conv_melody(m)
    #print(m, musicinfos)
    musics = []
    for seq, music in enumerate(musicinfos):
        start, end, name, melody = music.split(",")
       # end = conv_time(end)
       # start = conv_time(start)
       # if end<start:
       #     end+=24*60
        play = conv_time(end)-conv_time(start)
        melody = conv_melody(melody)
        if play>len(melody):
            melody = melody*(play//len(melody)+1)
        melody = melody[:play]
        musics.append([-play,seq,melody,name])
    musics.sort()
    for music in musics:
        if m in music[2]:
            return music[3]
    return "(None)"
