#https://school.programmers.co.kr/learn/courses/30/lessons/12952

def dfs(ar,i,n):
    if not n:
        return 1
    ans = 0
    for j in range(len(n)):
        f = 1
        for k,v in enumerate(ar):
            if n[j]+(i-k)==ar[k] or n[j]-(i-k)==ar[k]:
                f=0
                break
        if f:
            ans+=dfs(ar+[n[j]],i+1,n[:j]+n[j+1:])
    return ans
    
def solution(n):
    answer = 0
    tok = [i for i in range(n)]
    for i in range(n):
        answer += dfs([i],1,tok[:i]+tok[i+1:])
    return answer

'''
N-Queen
#KDT_코테스터디

길이 n의 체스판에 n개의 퀸 이동이 안겹치게 놓는 경우의수 구하는 문제

1차 접근:
어차피 같은줄에선 하나밖에 못두니까
한둘마다 두면서, 겹치지 않는 자리면 두기
  -> 두는 과정을 dfs로 해서 모두 순회
  -> "둘 수 있는 경우" 만 두기 때문에 길이가 n까지 도달하면 1개의 경우가 된다.

결과: 마지막 케이스 하나만 시간초과

꿀잠이후 2차 접근:
시간초과를 줄일라면,,
가로세로 모두 하나씩만 둘 수 있으니까
1. 처음 1~n까지 경우 모두 넣어놓고,
2. "둘 수 있는 경우" 둠
  -> 어쨋든 둘 수 있는 경우만 두기 때문에 종료조건은 동일

다음줄 다음줄 진행하고, 모든 숫자가 1개씩만 들어있어서
"둘 수 있는 경우" 검사를 대각선만 하면 됨.
  => 매 검사횟수 감소
  + 크기가 커질수록 남은 가능케이스가 작아지니 속도 증가
'''
