-- Most common education level
SELECT nivel_educacion, COUNT(*) AS total
FROM education
GROUP BY nivel_educacion
ORDER BY total DESC;

-- Education level by region
SELECT region, nivel_educacion, COUNT(*) AS total
FROM education
GROUP BY region, nivel_educacion
ORDER BY region, total DESC;

-- Education level grouped age ranges
SELECT
	CASE
		WHEN edad BETWEEN 18 AND 25 THEN '18-25'
		WHEN edad BETWEEN 26 AND 40 THEN '26-40'
		WHEN edad BETWEEN 41 AND 60 THEN '41-60'
		ELSE '60+'
	END AS grupo_de_edades,
	nivel_educacion,
	COUNT(*) AS total
FROM education
GROUP BY grupo_de_edades, nivel_educacion
ORDER BY grupo_de_edades, total DESC;

-- Percentage of high school graduates by region
SELECT 
	region,
	ROUND(
		SUM(CASE
			WHEN nivel_educacion = 'Secundaria completa' THEN 1
			ELSE 0
		END) * 100.0 / COUNT(*), 2)
		AS prc_sec_completa
FROM education
GROUP BY region
ORDER BY prc_sec_completa DESC;