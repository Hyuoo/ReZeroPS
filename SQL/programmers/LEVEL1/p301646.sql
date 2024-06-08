/*
Solving Date    : 2024.06.09
Title           : 특정 형질을 가지는 대장균 찾기
tags            : GROUP BY, BIT MASK
url             : https://school.programmers.co.kr/learn/courses/30/lessons/301646
*/

SELECT COUNT(CASE WHEN GENOTYPE & 5 THEN 1 END) AS COUNT
FROM ECOLI_DATA
WHERE NOT GENOTYPE & 2;

/*
프로그래머스 비트마스킹 왤케 좋아함;
*/