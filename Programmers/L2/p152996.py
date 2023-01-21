#https://school.programmers.co.kr/learn/courses/30/lessons/152996
#코딩테스트 연습 > 연습문제 > 시소 짝꿍
'''
풀이시간 : 거의 한두시간?
분류 : 구현...?, 시간복잡도 개선

>> 1차 시도 -> 테케 4번부터 올 시간초과
def solution(weights):
    bal = [[w*2,w*3,w*4] for w in sorted(weights)]
    a = 0
    for i in range(len(bal)-1):
        for j in range(i+1,len(bal)):
            if bal[i][2]<bal[j][0]:
                break
            if len(set(bal[i]).union(bal[j])) != 6:
                a += 1
    return a

>> 2차 시도 -> 테케 4는 통과되는데 5부터 다시 시간초과
def able(a):
    ar = [6*a//12,8*a//12,9*a//12,a,16*a//12,18*a//12,a*2]
    return ar
def solution(weights):
    weights.sort()
    a = 0
    for i in range(len(weights)-1):
        for j in able(weights[i]):
            a += weights[i+1:].count(j)
    return a

>> 이후 생각을 완전히 바꿔서 n^n 시간복잡도로는 클리어가 안되겠구나 해서 n^n이 아닌 방법을 몰색.
a,b가 짝꿍인가? 에서
임의의 수 a가 있을 때 얘랑 짝꿍이 되는 수에 대해서 접근
a는 2a, 3a, 4a가 되고, 각 수를 /2, /3, /4 한 숫자가 짝꿍이 될 수 있는 경우.
그럼 그 가능한 짝꿍이 몇개가 있는지를 체크하면 되겠구나 생각.

기존 짝꿍의 수를 dictionary로 변환해 저장해서 되는 케이스에 접근해서 다 더하는 방식을 사용.
collections.Counter를 사용.
저장하고, 각 결과를 계산해, 맞는 녀석들을 셈.
그리고 겹치는경우 구분안하고 다 더했기 때문에 2로 나누어줌.

-> 딕셔너리에 없는 요소에 접근할 때 에러가 나올 줄 알았는데 Count 객체는 없는 값을 조회하면 0을 준다.
-> a*2//2, a*2//3... 9개의 경우가 나오는데 중복이 나올 경우가 없기 때문에 그냥 더하기만 하면 된다.
'''
from collections import Counter
def solution(weights):
    wd = Counter(weights)
    a = 0
    for w in weights:
        a += wd[w] - 1
        for i in range(2,5):
            for j in range(2,5):
                if i==j:
                    continue
                t = w*i/j
                if t == int(t):
                    a += wd[int(t)]
    return a//2
