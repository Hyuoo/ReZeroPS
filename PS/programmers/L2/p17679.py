#https://school.programmers.co.kr/learn/courses/30/lessons/17679

r = [[0,0],[1,0],[0,1],[1,1]]
def solution(m, n, board):
    board = list(map(list,board))
    answer = 0
    
    while 1:
        del_cell = []
        for i in range(m-1):
            for j in range(n-1):
                four = ""
                for x,y in r:
                    four+=board[i+x][j+y]
                if "0" not in four and len(set(four))==1:
                    del_cell.append([i,j])
        
        if not del_cell:
            break
        
        for di, dj in del_cell:
            for x,y in r:
                if board[di+x][dj+y]!="0":
                    board[di+x][dj+y] = "0"
                    answer+=1
    
        for i in reversed(range(1,m)):
            for j in range(n):
                if board[i][j]=="0":
                    for k in reversed(range(i)):
                        if board[k][j]!="0":
                            board[i][j] = board[k][j]
                            board[k][j] = "0"
                            break
    
    return answer
'''
2018 KAKAO BLIND RECRUITMENT [1차] 프렌즈4블록
#KDT_코테스터디

똑바로 구현하는 문제

1. 4개 맞춰진곳 찾아서
1.1 지울곳없으면 끝
2. 지울곳 지우고
3. 떨구고
반복
'''
