-- 코드를 입력하세요
SELECT f.flavor
FROM FIRST_HALF F, ICECREAM_INFO I
WHERE F.FLAVOR = I.FLAVOR AND TOTAL_ORDER > 3000 AND INGREDIENT_TYPE = 'fruit_based'
order by total_order desc

