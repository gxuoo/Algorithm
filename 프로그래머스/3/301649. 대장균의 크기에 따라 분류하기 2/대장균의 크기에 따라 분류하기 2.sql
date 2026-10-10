-- 코드를 작성해주세요
SELECT
    ID,
    CASE
        WHEN ratio <= 0.25 THEN 'CRITICAL'
        WHEN ratio <= 0.50 THEN 'HIGH'
        WHEN ratio <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM (
    SELECT
        ID,
        PERCENT_RANK() OVER (
            ORDER BY SIZE_OF_COLONY DESC
        ) AS ratio
    FROM ECOLI_DATA
) AS ranked
ORDER BY ID;