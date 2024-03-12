/*
Solving Date    : 2024.02.19
Title           : 업그레이드 할 수 없는 아이템 구하기
tags            : IS NULL
url             : https://school.programmers.co.kr/learn/courses/30/lessons/273712
*/

with p_list as (
    select distinct parent_item_id as item_id
    from item_tree
    where parent_item_id is not NULL
    )

select item_id, item_name, rarity
from item_info
where item_id not in (select item_id from p_list)
order by item_id desc
;