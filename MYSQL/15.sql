USE sql_learning;

-- top 3 Customers, Who Bought most Wine between '01-03-2013' AND '31-09-2013' --

SELECT 
  ID 
  ,MntWines
  join_date,
  
  DENSE_RANK() OVER (
    ORDER BY 
      MntWines DESC
  ) TOP_3_customers 
FROM 
  customer_campaign
WHERE
	join_date BETWEEN '2013-03-01' AND '2013-09-31'
LIMIT 
  3;