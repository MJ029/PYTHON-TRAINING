USE sql_learning;

-- Customer With Top 3 Income --

SELECT
  *
FROM 
  (
    SELECT 
      RANK() OVER(
        ORDER BY 
          Income DESC
      ) AS TOP_3_customers, 
      ID, 
      Income 
    FROM 
      customer_campaign
  ) AS tmp 
WHERE 
  tmp.TOP_3_customers <= 3;
  
  -- Customer With LAST 3 Income --

SELECT
  *
FROM 
  (
    SELECT 
      RANK() OVER(
        ORDER BY 
          Income ASC
      ) AS LAST_3_customers, 
      ID, 
      Income 
    FROM 
      customer_campaign
  ) AS tmp 
  LIMIT 3;

