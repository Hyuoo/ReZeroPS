/*
Solving Date    : 2024.04.07
Solving Time    : -
Title           : 문자열 나누기
tags            : String
url             : https://school.programmers.co.kr/learn/courses/30/lessons/140108
runtime         : -
memory          : -
 */

class Solution {
    public int solution(String s) {
        int answer = 0;
        int count = 0;
        char prev = 0;
        
        for (int i=0; i<s.length(); i++) {
            if (prev == 0) {
                prev = s.charAt(i);
            }
            if (prev == s.charAt(i)) {
                count++;
            }
            else {
                count--;
                if (count == 0) {
                    prev = 0;
                    answer++;
                }
            }
        }
        if (prev > 0) {
            answer++;
        }
        
        return answer;
    }
}