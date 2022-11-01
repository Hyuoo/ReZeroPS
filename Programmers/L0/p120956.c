//https://school.programmers.co.kr/learn/courses/30/lessons/120956
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// babbling_len은 배열 babbling의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
/*
각 문자열이 읽을 수 있는지 검사하는 함수 readingTest.
읽을수있는 문자열 4개를 앞에서부터 반복하여 읽고,
읽을수없으면 인덱스 그대로, 읽을수있으면 그 뒤 인덱스로
-> 포인터가 \0(종료)까지 도달했으면 읽을 수 있음.
*/
int readingTest(const char* babb){
    char* readable[] = {"ye","ma","aya","woo"};
    char* ba;
    char* idx;
    ba = babb;
    for(int i=0;i<4;i++){
        idx = strstr(ba, readable[i]);
        if(!(idx-ba)){
            ba+=(i>>1&1)+2;
            i=-1;
            continue;
        }
    }
    return *ba=='\0';
}
int solution(const char* babbling[], size_t babbling_len) {
    int answer = 0;
    for(int i=0;i<babbling_len;i++)
        answer += readingTest(babbling[i]);
    return answer;
}
