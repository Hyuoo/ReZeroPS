#https://school.programmers.co.kr/learn/courses/30/lessons/150365
'''
코딩테스트 연습 2023 KAKAO BLIND RECRUITMENT 미로 탈출 명령어
렙3문제 미로탈출 명령어
풀이시간 : 1h

dfs로 탈출구까지 전부 탐색.
- 애초에 사전순으로 탐색하기때문에 가장먼저 찾은 값이 사전순으로 제일 빠른 값.
- 벽이 따로 없으므로 맵을 안그리고 isbound함수로 범위만 정해줌
- 최단거리가 k보다 멀어지면 아무리 가도 불가능하므로 absdist를 이용해 사전에 종료

- 다 풀고나서 재귀깊이때문에 에러나서 추가하고,
- 마지막케이스가 if absdist(x,y,r,c)%2!=k%2:return "impossible";로 해결되는 저격케이스여서 넣으니 성공.
'''
import sys
sys.setrecursionlimit(10**9)
def isbound(n,m,x,y):
    if x<1 or y<1 or x>n or y>m:
        return False
    return True
def absdist(x,y,r,c):
    return abs(x-r)+abs(y-c)
def dfs(n,m,x,y,r,c,k,route): # k--
    if not isbound(n,m,x,y) or absdist(x,y,r,c)>k:
        return -1
    if x==r and y==c and k==0:
        return route
    for next_route, i, j in zip("dlru",[1,0,0,-1],[0,-1,1,0]):
        t = dfs(n,m,x+i,y+j,r,c,k-1,route+next_route)
        if t!=-1 and t:
            return t
    return -1

def solution(n, m, x, y, r, c, k):
    if absdist(x,y,r,c)%2!=k%2:
        return "impossible"
    a = dfs(n,m,x,y,r,c,k,"")
    return a if a!=-1 else "impossible"
