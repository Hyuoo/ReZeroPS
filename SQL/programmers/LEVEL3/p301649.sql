/*
Solving Date    : 2024.06.09
Title           : 대장균의 크기에 따라 분류하기 2
tags            : SELECT, RANK, CASE
url             : https://school.programmers.co.kr/learn/courses/30/lessons/301649
*/

WITH t AS (
    SELECT ID,
        RANK() OVER(ORDER BY SIZE_OF_COLONY) as r,
        count(1) OVER() as a
    FROM ECOLI_DATA
)

SELECT ID,
    CASE ceil(r/a*4)
        WHEN 1 THEN 'LOW'
        WHEN 2 THEN 'MEDIUM'
        WHEN 3 THEN 'HIGH'
        WHEN 4 THEN 'CRITICAL'
    END AS COLONY_NAME
FROM t
ORDER BY 1;

/*
처음부터 퍼센테이지로 계산해주는 PERCENTRANK() 함수가 있다.

퍼센트 1~4 범위로 표준화시켜서 약식 CASE문으로 가독성좋게 작성
*/