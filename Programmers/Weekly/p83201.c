//LEVEL1
//코딩테스트 연습 > 위클리 챌린지 > 2주차 > 상호 평가
//https://programmers.co.kr/learn/courses/30/lessons/83201

#include <stdio.h>

char* solution(int** sc, size_t size, size_t dummy) {
    char* answer = (char*)malloc(size+1);answer[size]='\0';
    int min, max, sum, flag, tmp_num, tmp_count;
    
    for(int i=0;i<size;i++){
        min=100; max=sum=flag=tmp_num=0;
        
        for(int j=0;j<size;j++){
            min = sc[j][i]>min?min:sc[j][i];
            max = sc[j][i]>max?sc[j][i]:max;
            sum += sc[j][i];
        }
        
        if(sc[i][i]==min)tmp_num=min;
        else if(sc[i][i]==max)tmp_num=max;
        
        if(tmp_num!=0){
            tmp_count=0;
            for(int j=0;j<size;j++)
                tmp_count+=sc[j][i]==tmp_num?1:0;
            if(tmp_count==1)
                sum-=tmp_num,flag=1;
        }
        answer[i]="FFFFFDDCBAA"[(sum/(size-flag))/10];
    }
    return answer;
}
