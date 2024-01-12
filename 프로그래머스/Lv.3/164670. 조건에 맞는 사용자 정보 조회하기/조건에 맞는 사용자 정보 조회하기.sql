-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME, concat(u.CITY,' ',u.STREET_ADDRESS1,' ', u.STREET_ADDRESS2) as '전체주소' ,concat(substr(u.TLNO,1,3),'-',substr(u.TLNO,4,4),'-',substr(u.TLNO,8,4)) as '전화번호'
FROM USED_GOODS_BOARD as b , USED_GOODS_USER as u
WHERE b.WRITER_ID = u.USER_ID
GROUP BY u.USER_ID
HAVING count(u.USER_ID) >=3
ORDER BY u.USER_ID DESC