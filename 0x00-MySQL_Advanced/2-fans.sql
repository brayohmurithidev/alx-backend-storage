-- SELECT countyry origins and order by (non unique) fans
-- Rank country origin of brands based on number of fans they have

SELECT origin, SUM(fans) AS nb_fans FROM metal_bands
GROUP BY origin 
ORDER BY nb_fans DESC;