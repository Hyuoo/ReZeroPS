#https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    answer = 0
    discount = [""]*10+discount
    l = len(want)
    for i in range(10,len(discount)):
        f = 1
        for j in range(l):
            if discount[i]==want[j]:
                number[j] -= 1
            if discount[i-10]==want[j]:
                number[j] += 1
            if number[j]:
                f = 0
        if f:
            answer += 1
    return answer

'''
할인 행사
풀이시간 : 14m
#KDT_코테스터디

슬라이딩 윈도우 식으로 풀스캔
'''
