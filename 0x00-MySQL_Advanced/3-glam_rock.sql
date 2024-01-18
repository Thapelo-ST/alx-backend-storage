-- Listing bands with Glam rock as their main style, ranked by longevity
-- This script is intended for any database on MySQL

SELECT band_name,
       IFNULL(DATEDIFF(IFNULL(split, '2022-01-01'), IFNULL(formed, '2022-01-01')), 0) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;

