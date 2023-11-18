https://school.programmers.co.kr/learn/courses/30/lessons/92341
from collections import defaultdict
from math import ceil

def m_time(hour_clock):
    h,m = map(int,hour_clock.split(":"))
    return (h*60 + m)

def solution(fees, records):
    acc_time = defaultdict(int)
    
    parking = {}
    for record in records:
        hour_clock, number, ino = record.split()
        minute = m_time(hour_clock)
        if ino=="IN":
            parking[number] = minute
        else:
            acc_time[number] += minute - parking[number]
            del parking[number]
    
    last_time = m_time("23:59")
    for k in parking.keys():
        acc_time[k] += last_time - parking[k]
    
    base_time, base_fee, unit_time, unit_fee = fees
    #for k,v in {k:base_fee + ceil(max(0,(v-base_time)/unit_time))*unit_fee for k,v in acc_time.items()}.items():
    
    complete_fees = {}
    for k,v in acc_time.items():
        complete_fees[k] = base_fee + ceil(max(0,(v-base_time)/unit_time))*unit_fee
    
    return [complete_fees[k] for k in sorted(complete_fees.keys())]
'''
주차 요금 계산
풀이시간 : 26m

주어진 조건대로 처리하는 문제

- 같은차가 여러번 입차,출차 가능하고,
출차때 정산이 아니라
- 하루 누적시간 정산이라는 점
- 출차가 없을 시 23:59 출차로 계산한다는 점
이정도 고려하고 시키는대로 하면 끝
'''
