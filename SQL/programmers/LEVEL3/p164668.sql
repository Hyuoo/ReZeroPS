/*
Solving Date    : -
Title           : 조건에 맞는 사용자와 총 거래금액 조회하기
tags            : GROUP BY
url             : https://school.programmers.co.kr/learn/courses/30/lessons/164668
*/

select a.USER_ID, a.NICKNAME, b.P as TOTAL_SALES
from USED_GOODS_USER as a,
(
    SELECT
    WRITER_ID, sum(PRICE) as P
    from USED_GOODS_BOARD
    where status="DONE"
    group by WRITER_ID
    having P>=700000
) as b
where a.USER_ID=b.WRITER_ID
order by 3
;
