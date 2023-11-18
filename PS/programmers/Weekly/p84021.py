#LEVEL3
#코딩테스트 연습 > 위클리 챌린지 > 3주차 > 퍼즐 조각 채우기
#https://programmers.co.kr/learn/courses/30/lessons/84021


''' 속도에 대한 메모
1. 배열복사
> def valcpy(dest, src, size):
    for i in range(size):
        for j in range(size):
            dest[i][j] = src[i][j]
슬라이싱이 비교도 안되게 빠름
> tmp_board = copy.deepcopy(board) 핵느림
> valcpy(tmp_board, board, size) 짱느림
> tmp_board = [i[:] for i in board] 채용

2. 반복문
> for i in range(n):
> for i,n in enumerate(table):
둘다 별차이없음

3. 범위검사
> def ifrange(size, i, j):
    return (i in range(0,size) and j in range(0,size))
아래가 더 빠르고, 아예 인라인으로 쓰는게 더빠르고
> def ifrange(size, i, j):
    return (i>=0 and i<size) and (j>=0 and j<size)
    
4. 이차원배열속 요소 개수 세기
> def count_num1(ar):
    count = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            count += 1 if ar[i][j]==4 else 0
    return count
> def count_num2(ar):
    count = 0
        for i in ar:
            count += i.count(4)
    return count
> count_num1(ar)    핵느림
> sum(ar,[]).count(4)   느림
> count_num2(ar)    젤빠름

5. 다 했는데 안돼서 블럭 개수 메모해주는 방식으로
한번더 검사해서 반복이 가장 많이 일어나는, 불필요한 foo, startIdx 호출을 줄임
>> 성공
'''

def foo(board, table, size, bi, bj, ti, tj, i, j, r):
    if(ti+i<0 or ti+i>=size or tj+j<0 or tj+j>=size):
        return 0
    
    count = 0
    
    if(table[ti+i][tj+j] == 1):
        table[ti+i][tj+j] = 0
        count = 1
        
        if(r==0):
            if(add2board(board, size, bi+i, bj+j)==-1):
                return -1
        elif(r==1):
            if(add2board(board, size, bi-i, bj-j)==-1):
                return -1
        elif(r==2):
            if(add2board(board, size, bi-j, bj+i)==-1):
                return -1
        elif(r==3):
            if(add2board(board, size, bi+j, bj-i)==-1):
                return -1
            
        tmp = foo(board, table, size, bi, bj, ti, tj, i+1, j, r)
        if(tmp==-1): return -1
        else: count+=tmp
        tmp = foo(board, table, size, bi, bj, ti, tj, i-1, j, r)
        if(tmp==-1): return -1
        else: count+=tmp
        tmp = foo(board, table, size, bi, bj, ti, tj, i, j+1, r)
        if(tmp==-1): return -1
        else: count+=tmp
        tmp = foo(board, table, size, bi, bj, ti, tj, i, j-1, r)
        if(tmp==-1): return -1
        else: count+=tmp
    
    return count

def add2board(board, size, i, j):
    if(i<0 or i>=size or j<0 or j>=size):
        return -1
    board[i][j] += 2
    return 0

def startIdx(board, size, i, j):
    if(i<0 or i>=size or j<0 or j>=size):
        return 0
    
    if(board[i][j]==0 or board[i][j]==3):
        return -1
    if(board[i][j]==2):
        board[i][j]=4
        if(startIdx(board,size,i+1,j) == -1): return -1
        if(startIdx(board,size,i-1,j) == -1): return -1
        if(startIdx(board,size,i,j+1) == -1): return -1
        if(startIdx(board,size,i,j-1) == -1): return -1
    return 0

def rmIdx(table, size, i, j):
    if(i<0 or i>=size or j<0 or j>=size):
        return
    if(table[i][j]==1):
        table[i][j]=0
        rmIdx(table, size, i+1,j)
        rmIdx(table, size, i-1,j)
        rmIdx(table, size, i,j+1)
        rmIdx(table, size, i,j-1)

def memmo(memo, board, size):
    for i in range(size):
        for j in range(size):
            if(board[i][j]==0):
                tmp_board = [i[:] for i in board]
                memo[i][j] = cc(tmp_board,size,i,j)
                
def cc(board, size, i, j):
    if(i<0 or i>=size or j<0 or j>=size):
        return 0
    count = 0
    if(board[i][j] == 0):
        board[i][j] = 1
        count = 1
        tmp = cc(board, size, i+1, j)
        if(tmp==-1): return -1
        else: count+=tmp
        tmp = cc(board, size, i-1, j)
        if(tmp==-1): return -1
        else: count+=tmp
        tmp = cc(board, size, i, j+1)
        if(tmp==-1): return -1
        else: count+=tmp
        tmp = cc(board, size, i, j-1)
        if(tmp==-1): return -1
        else: count+=tmp
    
    return count

def solution(board, table):
    answer = 0
    size = len(board)
    
    #table 순회
    for i in range(size):
        for j in range(size):
            if(table[i][j]==1):
                flag=1
                table_block = 0
                
                #board 순회
                if(flag==0):continue
                for x in range(size):
                    for y in range(size):
                        if(flag==0): break
                        if(board[x][y]==0):

                            #try
                            if(table_block==0 or table_block==memo[x][y]):
                                for r in range(4):
                                    tmp_board = [i[:] for i in board]
                                    tmp_table = [i[:] for i in table]
                                    t_block = foo(tmp_board, tmp_table, size, x, y, i, j, 0, 0, r)
                                    
                                    if(table_block == 0 and t_block != -1): table_block = t_block
                                        
                                    if(t_block==memo[x][y]):
                                    
                                        if(startIdx(tmp_board, size, x, y)!=-1):
                                            flag=0
                                            rmIdx(table, size, i, j)
                                            board = [i[:] for i in tmp_board]
                                            break
                
                if(flag):rmIdx(table, size, i, j)
    
    for i in board:
        answer+=i.count(4)
    #인덱스 조회하면서 도는건 짱느리고
    #sum(ar,[]).count(4) 이렇게 할 수도 있는데 저게 더 빠름
    return answer
