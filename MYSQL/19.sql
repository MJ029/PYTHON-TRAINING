USE sql_learning;

-- Customer with Maximum number of Web Purchase and Recently logged-in --

SELECT
  *
FROM 
  (
    SELECT 
      RANK() OVER(
        ORDER BY 
          NumWebPurchases DESC, Recency DESC
      ) AS TOP_3_customers, 
      ID, 
      Recency,
      NumWebPurchases
    FROM 
      customer_campaign
  ) AS tmp 
WHERE 
  tmp.TOP_3_customers <= 3;