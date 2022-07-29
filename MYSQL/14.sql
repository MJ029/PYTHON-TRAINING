USE sql_learning;

-- Customer Who bought most of Gold Products -- 

SELECT 
  ID 
  ,MntGoldProds,
  
  DENSE_RANK() OVER (
    ORDER BY 
      MntGoldProds DESC
  ) AS TOP_customers
FROM 
  customer_campaign
  LIMIT 10;