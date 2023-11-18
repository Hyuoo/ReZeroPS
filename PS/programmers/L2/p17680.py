#https://school.programmers.co.kr/learn/courses/30/lessons/17680

def cscan(c, csize, d):
    last = 0
    for i in range(csize):
        if c[i][0]==d:
            return True, i
        if c[last][1]>c[i][1]:
            last = i
    return False, last

def solution(csize, cities):
    answer = 0
    c = [["",-1] for _ in range(csize)]
    
    if not c:
        return len(cities)*5
    
    for i in range(len(cities)):
        city = cities[i].lower()
        f, idx = cscan(c, csize, city)
        if f:
            answer += 1
            c[idx][1] = i
        else:
            answer += 5
            c[idx] = [city,i]
    
    return answer

'''
캐시
#KDT_코테스터디
어 시간을 체크안했네 대충 한 20분?

캐시를 그냥 리스트로 쓰고, -> 어차피 큐로 해도 캐시 풀스캔 할텐데 오버헤드 만들필요가 있나?
(캐시 hit/miss여부, 찾은/오래된인덱스) 를 리턴해주는 함수 cscan작성해서
1. 히트 시
    페이지시간 교체
2. 미스 시
    페이지 교체
끝
'''
