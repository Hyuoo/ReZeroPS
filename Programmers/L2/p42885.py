#https://school.programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    i = 0
    j = len(people)-1
    people.sort()
    count = 0
    while i<=j:
        if people[i]+people[j]>limit:
            j-=1
        else:
            i+=1
            j-=1
        count+=1
    return count
'''
구명보트
@KDT_코테스터디
풀이시간 : 10m

무조건 무거운 사람부터 태워야 한다는 마인드.

근데 가벼운사람 짝지은건 좋은데
만약 (70,10) 이렇게 짝지었는데 (70,30)처럼 더 최적이 있다면?
>> 다이조부:
  가벼운 10보다 30이 최적이려면
  무거운 70보다 큰 값이 존재해야되는데,
    이미 더 무거운사람들은 태워 보냈다.
    고로 고려안해도 최적 해
'''
