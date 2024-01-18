-- ranking country origions of bands by the number of non unique fans
-- intended for any db on mysql

SELECT origin, COUNT(DISTINCT fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

