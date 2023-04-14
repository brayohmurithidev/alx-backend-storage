-- SELECT BANDS WITH Glam rock as their main style
-- Ranked by their longevity

SELECT band_name, (split - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam% %rock%'
ORDER BY lifespan DESC;