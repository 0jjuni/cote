-- 코드를 입력하세요
SELECT warehouse_id, warehouse_name, address, 
case when freezer_yn is null then 'N'
else freezer_yn end FREEZER_YN
from food_warehouse
where warehouse_name like '%경기_'
order by warehouse_id asc