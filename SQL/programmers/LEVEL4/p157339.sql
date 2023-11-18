/*
Solving Date    : 2023.11.16
Title           : 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기
tags            : JOIN
url             : https://school.programmers.co.kr/learn/courses/30/lessons/157339
*/

with
car as (
    select car_id, car_type, daily_fee
    from CAR_RENTAL_COMPANY_CAR
    where car_type in ('세단', 'SUV')
    ),
dc as (
    select car_type, discount_rate
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where duration_type LIKE '30%'
    )

select *
from (
    select car_id, car_type, floor(daily_fee*((100-discount_rate)/100)*30) as fee
    where car_id not in (
        select distinct car_id
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where
            start_date <= '2022-11-30'
            and end_date >= '2022-11-01'
    )
) as t
where fee>=500000 and fee<2000000
order by 3 desc, 2, 1 desc
;

/*
문제를 제대로 안읽고
CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블이
대여 가능한 기간 테이블 인 줄 알고 한참 헛고생 함.

그리고 JOIN보다
start_date, end_date 조건을 생각하는 게 주된 어려움
- 해당 기간에 기록이 없는 car_id를 찾아야됨.
*/