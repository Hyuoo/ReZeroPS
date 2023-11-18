/*
Solving Date    : -
Title           : 저자 별 카테고리 별 매출액 집계하기
tags            : GROUP BY
url             : https://school.programmers.co.kr/learn/courses/30/lessons/144856
*/

select
author.AUTHOR_ID
, author.AUTHOR_NAME
, sales_cat.CATEGORY
, sales_cat.TOTAL_SALES 
from author, (
    select 
    t.author_id
    , t.category
    , sum(total_sales) as TOTAL_SALES
    from (
    select
        book.book_id
        ,book.author_id
        ,book.category
        ,(book.price*sales.sell) as total_sales
        from book, (
            SELECT
            book_id
            , sum(sales) as sell
            from book_sales
            where date_format(sales_date,"%Y%m")="202201"
            group by book_id
        ) as sales
        where book.book_id=sales.book_id
    )as t
    group by t.author_id,t.category
) as sales_cat
where author.author_id=sales_cat.author_id
order by AUTHOR_ID, CATEGORY desc;
