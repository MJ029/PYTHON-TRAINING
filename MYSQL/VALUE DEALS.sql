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
      ID, 
      Income,
      NumDealsPurchases
    FROM 
      customer_campaign
  ) AS tmp 
WHERE 
  tmp.TOP_3_customers <= 3;