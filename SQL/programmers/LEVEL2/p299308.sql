/*
Solving Date    : 2024.06.09
Title           : 분기별 분화된 대장균의 개체 수 구하기
tags            : STRING, DATE
url             : https://school.programmers.co.kr/learn/courses/30/lessons/299308
*/

SELECT q AS QUARTER, count(1) AS ECOLI_COUNT
FROM (
    SELECT concat(floor((MONTH(DIFFERENTIATION_DATE)-1)/3+1), 'Q') AS q FROM ECOLI_DATA
) t
GROUP BY q
ORDER BY q
;