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
      ) AS customer, 
      cust.ID, 
      Recency,
      NumWebPurchases
    FROM 
      customer_details AS cust
      JOIN places_details AS p ON cust.ID = p.ID
  ) AS tmp 
LIMIT 1;