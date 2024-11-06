-- 코드를 작성해주세요
-- 상위 0% ~ 25% 를 'CRITICAL', 26% ~ 50% 를 'HIGH', 51% ~ 75% 를 'MEDIUM', 76% ~ 100% 를 'LOW' 라고 분류합니다

WITH Ranked_Ecoil AS(
    SELECT
        ID,
        SIZE_OF_COLONY,
        PERCENT_RANK() over(ORDER BY SIZE_OF_COLONY DESC) AS rank_percentage
    FROM ECOLI_DATA
)
SELECT 
    ID,
    CASE
        WHEN rank_percentage  <= 0.25 THEN 'CRITICAL'
        WHEN rank_percentage  <= 0.50 THEN 'HIGH'
        WHEN rank_percentage  <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM Ranked_Ecoil
ORDER BY ID ASC