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
