//LEVEL3
//코딩테스트 연습 > 위클리 챌린지 > 3주차 > 퍼즐 조각 채우기
//https://programmers.co.kr/learn/courses/30/lessons/84021

#include <string>
#include <vector>

using namespace std;

int add2board(vector<vector<int>> &board, size_t size, int i, int j){
    if(i>=size || i<0 || j>=size || j<0)
        return -1;
    
    board[i][j]+=2;
    return 0;
}

int foo(vector<vector<int>> &board, vector<vector<int>> &table, int size,int bi, int bj, int ti, int tj, int i, int j, int rotate){
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


int startIdx(vector<vector<int>> &board, int size, int i, int j){
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

void rmIdx(vector<vector<int>> &table, int size, int i, int j){
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

int change4to1(vector<vector<int>> &board,int size){
    int count=0;
    for(int i=0;i<size;i++)
        for(int j=0;j<size;j++)
            if(board[i][j]==4)
                count++;
    return count;
}

void printt(vector<vector<int>> a){
    for(int i=0;i<a.size();i++){
        for(int j=0;j<a.size();j++){
            printf("[%d]",a[i][j]);
        }
        printf("\n");
    }
}

int solution(vector<vector<int>> board, vector<vector<int>> table) {
    int flag;
    int size = board.size();
    vector<vector<int>> tmp_board;
    vector<vector<int>> tmp_table;
    
    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            if(table[i][j]==1){
                flag=1;
                
                for(int x=0;flag&&x<size;x++){
                    for(int y=0;flag&&y<size;y++){
                        if(board[x][y]==0){
                            
                            for(int r=0;r<4;r++){
                                //tmp_board.assign(board.begin(), board.end());
                                //tmp_table.assign(table.begin(), table.end());
                                tmp_board = board;
                                tmp_table = table;
                                
                                if(foo(tmp_board, tmp_table, size, x, y, i, j, 0, 0, r)==0){
                                    if(startIdx(tmp_board,size,x,y)==0){
                                        flag=0;
                                        rmIdx(table,size,i,j);
                                        //board.assign(tmp_board.begin(), tmp_board.end());
                                        board = tmp_board;
                                    }
                                }
                                
                            }
                        }
                    }
                }
                rmIdx(table,size,i,j);
            }
        }
    }
    return change4to1(board,size);
}
