/*
Solving Date    : 2024.06.09
Title           : 특정 세대의 대장균 찾기
tags            : SELECT, JOIN, SELF JOIN
url             : https://school.programmers.co.kr/learn/courses/30/lessons/301650
*/

WITH root AS (
    SELECT ID as rt FROM ECOLI_DATA WHERE PARENT_ID IS NULL
),
    lineage AS (
    SELECT a.rt, b.ID as g2, c.ID as g3
    FROM root a
    JOIN ECOLI_DATA b ON a.rt=b.PARENT_ID
    JOIN ECOLI_DATA c ON b.ID=c.PARENT_ID
)

SELECT g3 as ID FROM lineage;

/*
이거 왜 레벨 4임
*/