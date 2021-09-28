#LEVEL3
#코딩테스트 연습 > 위클리 챌린지 > 3주차 > 퍼즐 조각 채우기
#https://programmers.co.kr/learn/courses/30/lessons/84021

#include <stdio.h>
#include <stdlib.h>

//foo : table -> board 위에 겹치는 함수. 범위밖으로 넘어가면 -1, 정상 0
int foo(int** board, int** table, size_t size,int bi, int bj, int ti, int tj, int i, int j, int rotate){
    if(ti+i>=size || ti+i<0 || tj+j>=size || tj+j<0)
        return 0;
    
    int tmp;
    if(table[ti+i][tj+j]==1){
        table[ti+i][tj+j]=0;
        switch(rotate){
            case 0:
                tmp=add2board(board,size,bi+i,bj+j);
                break;
            case 1:
                tmp=add2board(board,size,bi-i,bj-j);
                break;
            case 2:
                tmp=add2board(board,size,bi+j,bj-i);
                break;
            case 3:
                tmp=add2board(board,size,bi-j,bj+i);
                break;
        }
        if(tmp<0) return -1;
        
        tmp=foo(board,table,size,bi,bj,ti,tj,i+1,j,rotate)+\
        foo(board,table,size,bi,bj,ti,tj,i-1,j,rotate)+\
        foo(board,table,size,bi,bj,ti,tj,i,j+1,rotate)+\
        foo(board,table,size,bi,bj,ti,tj,i,j-1,rotate);
        if(tmp<0) return -1;
    }
    return 0;
}

// foo에서 호출, board위치에 블럭겹쳐놓기(+=2)
int add2board(int** board, size_t size, int i, int j){
    if(i>=size || i<0 || j>=size || j<0)
        return -1;
    
    board[i][j]+=2;
    return 0;
}

//특정위치에서 블럭 겹쳐진 유효성 검사
//맞는 블럭은 4로 치환. 이후 change4to1 함수에서 처리
int startIdx(int** board, size_t size, int i, int j){
    if(i<0 || j<0 || i>=size || j>=size)
        return 0;
    
    int tmp;
    switch(board[i][j]){//case 0,4는 return 0;
        case 0: case 3:
            return -1;
        case 2:
            board[i][j]=4;
            tmp=startIdx(board,size,i+1,j)+\
            startIdx(board,size,i-1,j)+\
            startIdx(board,size,i,j+1)+\
            startIdx(board,size,i,j-1);
            if(tmp<0) return -1;
    }
    return 0;
}

//table에서 조회한블럭 제거
void rmIdx(int** table, size_t size, int i, int j){
    if(i<0 || j<0 || i>=size || j>=size)
        return;
    
    if(table[i][j]==1){
        table[i][j]=0;
        rmIdx(table,size,i+1,j);
        rmIdx(table,size,i-1,j);
        rmIdx(table,size,i,j+1);
        rmIdx(table,size,i,j-1);
    }
}

// startIdx(유효성검사) 후 add2board 후 호출; 4블럭 1로 전환하고 그 개수반환
int change4to1(int **board,size_t size){
    int count=0;
    for(int i=0;i<size;i++)
        for(int j=0;j<size;j++)
            if(board[i][j]==4)
                count++;
    return count;
}

//배열 복사용
void valcpy(int** dest, int** source, int size){
    for(int i=0;i<size;i++)
        for(int j=0;j<size;j++)
            dest[i][j] = source[i][j];
}

int solution(int** origin_board, size_t size, size_t z, int** origin_table) {
    int flag;
    /*
    블럭상태구분->(0:빈칸, 1:블럭, 2:빈칸위에 포갠블럭, 3:블럭위에 포갠블럭)
    func foo : table -> board 로 블럭 겹치는 함수 (정상0, 비-1)
    func add2board : foo에서 호출 / board에 블럭 겹치기 (+=2)
    func startIdx : 블럭 겹친 후 유효성검사 (빈칸에 딱 겹쳐졌는지), 옳은블럭은 4로 치환.
    func rmIdx : table에서 블럭 제거 (1덩어리 -> 0)
    func change4to1 : startIdx에서 4로 치환된거 1로바꾸며 그 개수 반환
    func valcpy : origin배열 -> tmp배열 카피용
    */
    int** tmp_board= (int**)malloc(sizeof(int*)*size);
    int** tmp_table= (int**)malloc(sizeof(int*)*size);
    for(int i=0;i<size;i++){
        tmp_board[i]= (int*)malloc(sizeof(int)*size);
        tmp_table[i]= (int*)malloc(sizeof(int)*size);
    }
    
    //table 순회 (값==1 탐색) / 블럭찾기
    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            if(origin_table[i][j]==1){
                flag=1;
                
                //board 순회 (값==0 탐색) / 빈칸찾기
                for(int x=0;flag&&x<size;x++){
                    for(int y=0;flag&&y<size;y++){
                        if(origin_board[x][y]==0){
                            
                            //4방향으로 다 조회
                            for(int r=0;r<4;r++){
                                //임시테이블 만들어서
                                valcpy(tmp_board,origin_board,size);
                                valcpy(tmp_table,origin_table,size);
                                //빈칸기준으로 다 포개보고,
                                if(foo(tmp_board, tmp_table, size, x, y, i, j, 0, 0, r)==0){
                                    //유효하면
                                    if(startIdx(tmp_board, size, x, y)==0){
                                        flag=0;
                                        //원본table에서 해당 블럭 지우고
                                        rmIdx(origin_table,size,i,j);
                                        //임시board -> 원본board 적용 (아직 맞은블럭은 4)
                                        valcpy(origin_board,tmp_board,size);
                                    }
                                }
                            }
                        }
                    }
                }
                //어차피 한번 다 대본블럭은 다시맞을일 없음
                rmIdx(origin_table, size, i,j);
            }
        }
    }
    //모든 4 세서 반환
    return change4to1(origin_board,size);
}
