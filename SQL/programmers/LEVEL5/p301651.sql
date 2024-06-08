/*
Solving Date    : 2024.06.09
Title           : 멸종위기의 대장균 찾기
tags            : SELECT, RECURSIVE, JOIN
url             : https://school.programmers.co.kr/learn/courses/30/lessons/301651
*/

WITH RECURSIVE t AS (
    SELECT 1 as GENERATION, PARENT_ID, ID FROM ECOLI_DATA WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT GENERATION+1, t.ID, r.ID FROM t LEFT JOIN ECOLI_DATA r ON t.ID=r.PARENT_ID
    WHERE r.ID
)

SELECT COUNT(*) as COUNT, t.GENERATION
FROM t
LEFT JOIN ECOLI_DATA c ON t.ID=c.PARENT_ID
WHERE c.ID is NULL
GROUP BY t.GENERATION
ORDER BY t.GENERATION;

/*
재귀쿼리 첨써본당
*/