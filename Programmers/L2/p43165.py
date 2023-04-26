#코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 타겟 넘버
#https://programmers.co.kr/learn/courses/30/lessons/43165

def get_sum(n, nums):
    tot = 0
    for i in nums:
        tot+=(i if n&1 else -i)
        n//=2
    return tot

def solution(nums, target):
    ans = 0
    for i in range(2**(len(nums))):
        if get_sum(i,nums)==target:
            ans+=1
    return ans

# 숏...?
# def solution_2(n, t):
#     return list(map(eval,["".join(["+-"[ord(d)-48]+str(n) for n,d in zip(n,"{:0{l}}".format(int(bin(b)[2:]),l=len(n)))]) for b in range(2**(len(n)))])).count(t)

# 옛날코드
# def solution(numbers, target):
#     n=len(numbers)
#     ar=[0]*(2**(n+1))
#     idx=2
#     for i in range(n):
#         for j in range(2**(i+1)):
#             ar[idx]=ar[idx//2]+numbers[i]*(1 if idx%2 else -1)
#             idx+=1
#     return ar[2**n:].count(target)

'''
타겟 넘버
풀이시간 : 약 30분?
#KDT_코테스터디

얘도 이전에 풀었던 이력이 있다. 근데 기억하나도 안나

방법은 +- 분기가 나뉘는 모든 경우의수를
2인법으로 생각.

숫자가 3개라면
+++ >> 000
++- >> 001
+-+ >> 010
+-- >> 011
..

이 방법을 이용해서 쉽게 모든 경우의 수 계산 가능
(0~2**(len(nums))):
    get_sum()함수로 +-위치대로 nums 계산해서 계산결과 리턴
같으면 ans+=1

=============
옛날 풀이도 비슷한 원리
속도는 얘가 훨빠르네
얘는 포화 완전 이진트리를 이용한 방법이라고도 볼 수 있을 듯
'''
