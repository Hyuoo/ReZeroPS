#https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    s = []
    for n in number:
        while k and s and s[-1]<n:
            s.pop()
            k -= 1
        s.append(n)
    if k:
        s = s[:-k]
    return "".join(s)
'''
큰 수 만들기

1. 앞에부터 읽으면서 숫자를 선택하며
  1.1 지금 읽는게 선택된 숫자보다 크면
    삭제. (k가 남아있을 경우/선택된숫자가 있을경우)

다 읽었는데 k가 남아있으면 k개를 지워야되는데,
숫자가 내림차순으로 되어있는 경우이기때문에 뒤에서 k개만큼 지움

끝.
'''
