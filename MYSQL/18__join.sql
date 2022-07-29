USE sql_learning;

-- Top 10 Customers who Utilized Most Value Deals where with larger income slab --

SELECT
  *
FROM 
  (
    SELECT 
      RANK() OVER(
        ORDER BY 
          NumDealsPurchases DESC, Income DESC
      ) AS TOP_3_customers, 
      cust.ID, 
      Income,
      NumDealsPurchases
    FROM 
      customer_details AS cust
      JOIN promotions_details AS prom ON cust.ID = prom.ID
  ) AS tmp 
LIMIT 10;