-- List bands with Glam rock as their main style, ranked by longevity
SELECT band_name, 
       CASE 
            WHEN formed = 0 THEN 0  -- If formed is 0, set lifespan to 0
            ELSE GREATEST(2022 - formed, 0)  -- Calculate lifespan until 2022
       END AS lifespan
FROM bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC, band_name;
