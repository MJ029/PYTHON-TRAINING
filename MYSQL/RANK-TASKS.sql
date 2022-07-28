SELECT 
  ID, 
  Income, 
  DENSE_RANK() OVER (
    ORDER BY 
      Income
  ) LAST_3_RANK 
FROM 
  customer_campaign 
LIMIT 
  3;
  
  
SELECT 
  ID, 
  Income, 
  DENSE_RANK() OVER (
    ORDER BY 
      Income DESC
  ) TOP_3_RANK 
FROM 
  customer_campaign 
LIMIT 
  3;
