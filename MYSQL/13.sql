USE sql_learning;

-- Top 3 Customers, Who was single and recent login is very large --

SELECT 
  ID
  ,Recency
  ,martial_status,
  
  DENSE_RANK() OVER (
    ORDER BY 
      Recency DESC
  ) AS TOP_3_customers 
FROM 
  customer_campaign
WHERE
	martial_status = 'Single'
LIMIT 
  3;