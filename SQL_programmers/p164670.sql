select
USER_ID
, NICKNAME
, concat_ws(" ",city,street_address1,street_address2) as 전체주소
, insert(insert(tlno,8,0,"-"),4,0,"-") as 전화번호
from used_goods_user
where user_id in (
    select uboard.writer_id
    from used_goods_board as uboard,used_goods_user as uuser
    where uboard.writer_id=uuser.user_id
    group by uboard.writer_id
    having count(*)>=3
)
order by user_id desc
;
