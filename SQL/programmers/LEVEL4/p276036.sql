/*
Solving Date    : 2024.02.23
Title           : 언어별 개발자 분류하기
tags            : GROUP BY, BIT MASK
url             : https://school.programmers.co.kr/learn/courses/30/lessons/276036
*/

-- ret(GRADE, ID, EMAIL)
-- A: Front End + Python
-- B: C#
-- C: Front End with out (A, B)

WITH A as (
    SELECT SUM(CODE) as 'A'
    FROM SKILLCODES
    WHERE
        NAME like 'Python'
   ),
    B as (
    SELECT SUM(CODE) as 'B'
    FROM SKILLCODES
    WHERE
        NAME like 'C#'
    ),
    C as (
    SELECT SUM(CODE) as 'C'
    FROM SKILLCODES
    WHERE
        CATEGORY like 'Front End'
    ),
    GRADES as (
    SELECT *
    FROM A, B, C
    )

SELECT GRADE, ID, EMAIL
FROM
    (SELECT
        d.ID,
        d.EMAIL,
        -- d.SKILL_CODE,
        -- g.A, g.B, g.C,
        CASE
            WHEN d.SKILL_CODE & A AND d.SKILL_CODE & C THEN 'A'
            WHEN d.SKILL_CODE & B THEN 'B'
            WHEN d.SKILL_CODE & C THEN 'C'
        END as GRADE
    FROM DEVELOPERS as d
    JOIN GRADES as g
    ) as t
WHERE GRADE is not NULL
ORDER BY GRADE, ID
;

/*

*/