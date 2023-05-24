#https://school.programmers.co.kr/learn/courses/30/lessons/62048

from math import floor, ceil

def gcd(a,b):
    return gcd(b,a%b) if b else a

def solution(w,h):
    ans = w*h
    n = gcd(w,h)
    w = int(w//n)
    h = int(h//n)
    M = max(w,h)
    m = min(w,h)
    for i in range(m):
        # ans -= (ceil(M/m*(i+1))-floor(M/m*i))*n
        ans -= (ceil((M*(i+1))/m)-floor((M*i)/m))*n
    return ans
'''
멀쩡한 사각형
#KDT_코테스터디

격자칸 종이에서 대각선 스윽 그을때 이용가능한 격자 수 구하는 문제

접근 :
1. 이게 약분이 되는 크기면 반복구조이므로
  일단 약분해서 반복횟수 줄이고, 약분한 값을 곱해주기
2. 한칸마다 경계선 위치를 기준으로 잘리니까
  칸의 경계마다 위치를 구해서 올림, 내림으로 소거되는 칸 수 세기

풀이 :
1. 전체 칸 크기 ans
2. 일단 공약수만큼 나눔
3. 큰값 작은값 분리
4. 작은값만큼 반복하면서,
  4.1 칸 앞뒤 경계위치 구해서 ((올림-내림)*공약수)를 ans에서 빼준다.

문제점 :
1. 실행시간 너무 김
  => 반복횟수 줄이기 -> 더 작은값을 range로
2. 4,17번만 틀려서 한참 고민하다 질문하기 보니까
  => 소수점 오차때문이란 말이 있어서 연산순서 변경하니까 됨 (주석부분)
    나누기곱하기 -> 곱하기나누기
----------------------------------------------
아니근데
w*h- ( w+h-gcd(w,h) )
이게 그냥 정답이 되네?
'''
