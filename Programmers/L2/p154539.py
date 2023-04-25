#https://school.programmers.co.kr/learn/courses/30/lessons/154539

# 코드 줄이기 못참지
def solution(nums):
    ans = []
    s = []
    for i in reversed(nums):
        while s and i>=s[-1]:s.pop()
        ans.append(s[-1] if s and i<s[-1] else -1)
        s.append(i)
    return list(reversed(ans))
  
# 첫번째 풀이 : 뒤에서 순차적으로
# def solution(nums):
#     ans = [-1 for _ in range(len(nums))]
#     s = []
#     for i in reversed(range(len(nums))):
#         while s and nums[i] >= s[-1]:
#             s.pop()
#         if s and nums[i] < s[-1]:
#             ans[i] = s[-1]
#         s.append(nums[i])
#     return ans
  
# 두번째 풀이 : 앞에서 처리안된 인덱스부터
# def solution(nums):
#     ans = [-1 for _ in range(len(nums))]
#     s = []
#     for i in range(len(nums)):
#         while s and nums[s[-1]] < nums[i]:
#             ans[s.pop()] = nums[i]
#         s.append(i)
#     return ans


'''
뒤에 있는 큰 수 찾기
#KDT_코테스터디
풀이시간 : 1h 10m

유사문제 : https://www.acmicpc.net/problem/17298

순서가 뒤에있는 수 중에 가장 앞에있는 큰 숫자 리스트로 만드는 문제.
당연히 그냥 접근하면 시간문제로 막힌다.

<첫번째 풀이>
한참 생각하다가 풀이방법이 생각안나서 질문게시판 제목보고 스택에서 힌트를 얻어서
2번째 방법으로 풀었다.
- 뒤에서부터 읽으며 값을 스택의 값과 비교한다.
- 스택에는 항상 큰수에서 낮은 수 순으로 쌓인다. peek()은 제일 낮은 수
- 읽고있는 값을 스택에 있는 값과 비교해서 작은값을 빼다보면(pop())
  1. 더 큰 수가 나오거나
    - 해당 수가 지금읽는자리의 답
  2. 빈 스택이 되거나
    - 해당 수보다 큰 수는 뒤에 없음
  각각 처리하면 된다.
코드에서는 디폴트로 -1로 설정하여 1.의 케이스만 처리했다.
-1을 안만들면 ans = []로 초기화하고
if s and nums[i] < s[-1]:
    ans.append(s[-1])
else:
    ans.append(-1)
로 바꾸고, 제출때 뒤집어서 내면 정답이 된다.

=======================================
근데 이렇게 만드니까
if else 어케참음
ans.append(s[-1] if s and nums[i]<s[-1] else -1)
로 바꿔버리기

어 근데 이러니까 for문도 인덱스가 아니라 다 nums[i]만 쓰네?
바로 for i in reversed(nums)로 바꿔버리기

해서 나온 코드가 주석없는 코드
========================================

<두번째 풀이>
스터디하는 다른분의 코드를 보고
앞에서 부터 접근해서
처리안된 인덱스를 저장하는 식으로 해도 되는구나 해서
푼 방법.

첫번째 방법보다 직관적인 것 같다.
앞 뒤의 차이가 은근 헷갈린다.

다만 뒤에서 접근하면 무조건 지나간 자리는 처리완료
앞에서 접근은 이해가 쉽다.
'''
