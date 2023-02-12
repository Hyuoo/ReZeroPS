#https://school.programmers.co.kr/learn/courses/30/lessons/155651
def mtime(t):
    h, m = map(int,t.split(":"))
    return h*60+m

def solution(book_time):
    reserv = [0]
    times = []
    for i in book_time:
        times.append([mtime(i[0]), mtime(i[1])+9])
    times.sort()
    
    for t in times:
        f = 0
        for i in range(len(reserv)):
            if reserv[i]<t[0]:
                reserv[i] = t[1]
                f = 1
                break
        if f == 0:
            reserv.append(t[1])
    
    return len(reserv)

'''
연습문제 호텔 대실
풀이시간 : 16m

모두 분단위로 합산하여
객실 배열 reserv 칸마다 1객실로 두고
정렬된 시간순서로 넣기


+ 시작시간 끝시간당 객실 수 +- 해서 누적합 방식으로도 구할 수 있음.
'''
