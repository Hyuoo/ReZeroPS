/*
Solving Date    : 2024.01.29
Title           : 주문량이 많은 아이스크림들 조회하기
tags            : JOIN
url             : https://school.programmers.co.kr/learn/courses/30/lessons/133027
*/

WITH tot AS
	(
        (SELECT FLAVOR, FIRST_HALF.TOTAL_ORDER as TOTAL_ORDER FROM FIRST_HALF)
		UNION ALL
		(SELECT FLAVOR, JULY.TOTAL_ORDER FROM JULY)
    )

SELECT FLAVOR FROM tot
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC
LIMIT 3
;