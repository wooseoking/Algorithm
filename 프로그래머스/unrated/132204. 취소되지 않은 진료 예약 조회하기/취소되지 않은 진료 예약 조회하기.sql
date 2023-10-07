-- 코드를 입력하세요
SELECT a.APNT_NO , p.PT_NAME, p.PT_NO , a.MCDP_CD , d.DR_NAME , a.APNT_YMD
FROM PATIENT as p , DOCTOR as d , APPOINTMENT as a
WHERE a.PT_NO = p.PT_NO and a.MDDR_ID = d.DR_ID
and DATE_FORMAT(a.APNT_YMD,'%Y-%m-%d') = '2022-04-13'
and a.APNT_CNCL_YN = 'N'
and a.MCDP_CD = 'CS'
ORDER BY a.APNT_YMD