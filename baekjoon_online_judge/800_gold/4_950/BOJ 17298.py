input()
nums = list(map(int,input().split()))
ans = []
s = []
for i in reversed(nums):
    while s and i>=s[-1]:
        s.pop()
    ans.append(s[-1] if s and i<s[-1] else -1)
    s.append(i)
print(*reversed(ans))
'''
오큰수
풀이시간 : 1h 30m???

#KDT_코테스터디
에서 푼 [프로그래머스 - 뒤에 있는 큰 수 찾기]
#https://school.programmers.co.kr/learn/courses/30/lessons/154539
문제와 동일해서 동일코드로 품.

응용 문제 [백준 - 오등큰수]
#https://www.acmicpc.net/problem/17299

뒤에서부터 읽으면서
스택에는 내림차순으로 저장되어있고
스택을 까다보면
1. 큰수가 나오던가
  - 큰 수가 뒤에서 젤먼처 큰 수 (peek)
2. 스택이 비던가
  - 뒤에 큰수가없음 (-1)
'''
