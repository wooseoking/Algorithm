-- 코드를 입력하세요
SELECT i.REST_ID,i.REST_NAME,i.FOOD_TYPE,i.FAVORITES,i.ADDRESS,ROUND(AVG(r.REVIEW_SCORE),2) as SCORE
FROM REST_INFO as i , REST_REVIEW as r
WHERE i.REST_ID = r.REST_ID and i.ADDRESS like '서울%'
GROUP BY i.REST_ID
ORDER BY ROUND(AVG(r.REVIEW_SCORE),2) DESC , i.FAVORITES DESC