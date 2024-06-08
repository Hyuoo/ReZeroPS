/*
Solving Date    : 2024.06.09
Title           : 연도별 대장균 크기의 편차 구하기
tags            : SELECT, DATE, SUM, MAX, MIN
url             : https://school.programmers.co.kr/learn/courses/30/lessons/299310
*/

WITH t AS (
    SELECT
        YEAR(DIFFERENTIATION_DATE) AS YEAR,
        MAX(SIZE_OF_COLONY)
            OVER(PARTITION BY YEAR(DIFFERENTIATION_DATE)) AS MAXS,
        SIZE_OF_COLONY,
        ID
    FROM ECOLI_DATA
)
    
SELECT YEAR, MAXS-SIZE_OF_COLONY AS YEAR_DEV, ID
FROM t
ORDER BY 1, 2;