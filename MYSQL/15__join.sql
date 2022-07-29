USE sql_learning;

-- top 3 Customers, Who Bought most Wine between '01-03-2013' AND '31-09-2013' --

SELECT 
  cust.ID 
  ,MntWines
  Dt_Customer,
  
  DENSE_RANK() OVER (
    ORDER BY 
      MntWines DESC
  ) TOP_3_customers 
FROM 
  customer_details AS cust
  JOIN product_details AS prod ON cust.ID = prod.ID
WHERE
	Dt_customer BETWEEN '2013-03-01' AND '2013-09-31'
LIMIT 
  3;