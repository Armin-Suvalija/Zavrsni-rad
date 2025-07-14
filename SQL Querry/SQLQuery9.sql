SELECT 
  (yr_built / 10) * 10 AS decade_built,
  COUNT(*) AS properties_built
FROM housing_price_data
GROUP BY (yr_built / 10) * 10
ORDER BY decade_built;