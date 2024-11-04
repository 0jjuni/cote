-- 코드를 작성해주세요
select round(avg(case when length is null then 10
else length end),2) AVERAGE_LENGTH
from fish_info

