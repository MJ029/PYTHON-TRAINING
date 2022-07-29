USE sql_learning;

-- Customers who joined before '01-01-2013' --

SELECT 
  ID, 
  join_date 
FROM 
  customer_campaign 
WHERE 
  join_date <= '2013-01-01';
  
-- Customers who joined After '01-01-2014' --
  
SELECT 
  ID, 
  join_date 
FROM 
  customer_campaign 
WHERE 
  join_date >='2014-01-01';
  
  -- Customers who joined Between '01-01-2013' AND '31-12-2013' --
  
SELECT 
  ID, 
  join_date 
FROM 
  customer_campaign 
WHERE 
  join_date BETWEEN '2013-01-01' AND '2013-12-31';

