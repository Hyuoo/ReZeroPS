#https://school.programmers.co.kr/learn/courses/30/lessons/169199

from collections import deque

def solution(board):
    
    d = [[0,-1],[0,1],[1,0],[-1,0]]
    def isbound(x,y):
        if x<0 or x>=len(board) or y<0 or y>=l:
            return False
        if board[x][y]=="D":
            return False
        return True
            
    l = len(board[0])
    dp = [[0 for _ in range(l)] for _ in range(len(board))]
    new_board = []
    r, g = [0,0], [0,0]
    for i in range(len(board)):
        tmp = []
        for j in range(l):
            tmp.append(board[i][j])
            if board[i][j]=="R":
                r = [i,j]
            if board[i][j]=="G":
                g = [i,j]
        new_board.append(tmp)
    board = new_board
    
    ans = -1
    q = deque([r+[1]])
    while q:
        x,y,n = q.popleft()
        if dp[x][y]!=0:
            continue
        if x==g[0] and y==g[1]:
            ans = n-1
            break
        dp[x][y] = n
        for dx,dy in d:
            nx = x
            ny = y
            while isbound(nx+dx,ny+dy):
                nx = nx+dx
                ny = ny+dy
            q.append([nx,ny,n+1])
    
    return ans

'''
리코쳇 로봇
풀이시간 : 51m
#KDT_코테스터디

bfs로 R위치에서 모든경우 반복
  -> 골인점 만나면 중지
반복횟수 제한하기 위해서 dp사용
'''
