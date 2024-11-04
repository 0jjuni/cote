-- 코드를 작성해주세요
select count(*) FISH_COUNT
from fish_info
where DATE_FORMAT(time, '%Y') = '2021'