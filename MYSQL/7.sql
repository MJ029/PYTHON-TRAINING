USE sql_learning;
-- MRF - MOST REGISTERED FIELD -- 
SELECT 
  education AS MRF, 
  COUNT(education) AS `customers` 
FROM 
  customer_campaign 
GROUP BY 
  education 
ORDER BY 
  `customers` DESC 
LIMIT 
  1;




