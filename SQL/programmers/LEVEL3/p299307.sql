/*
Solving Date    : 2024.06.09
Title           : 대장균의 크기에 따라 분류하기 1
tags            : SELECT, CASE
url             : https://school.programmers.co.kr/learn/courses/30/lessons/299307
*/

SELECT ID,
    CASE FLOOR(LOG(10, SIZE_OF_COLONY))
        WHEN 0 THEN 'LOW'
        WHEN 1 THEN 'LOW'
        WHEN 2 THEN 'MEDIUM'
        ELSE 'HIGH'
    END AS SIZE
FROM ECOLI_DATA
ORDER BY ID;