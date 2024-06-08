/*
Solving Date    : 2024.06.09
Title           : 대장균들의 자식의 수 구하기
tags            : SELECT, SELF JOIN
url             : https://school.programmers.co.kr/learn/courses/30/lessons/299305
*/

SELECT a.ID, COUNT(b.ID) AS CHILD_COUNT
FROM ECOLI_DATA a
LEFT JOIN ECOLI_DATA b ON a.ID=b.PARENT_ID
GROUP BY a.ID
ORDER BY ID;

/*
아무리봐도 프로그래머스는 레벨링 기준을 모르겠다.
*/