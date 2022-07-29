USE sql_learning;

DROP TABLE IF EXISTS customer_campaign;

CREATE TABLE If NOT EXISTS customer_campaign AS 

SELECT 
  c.ID, 
  STR_TO_DATE(c.Dt_customer, '%d-%m-%Y') AS join_date, 
  STR_TO_DATE(
    CONCAT(c.Year_Birth, '-01-01'), 
    '%Y-%m-%d'
  ) AS YOB, 
  TRIM(c.Education) AS education,
  TRIM(c.Marital_Status) AS martial_status,
  CAST(
    c.Income AS DECIMAL(28, 2)
  ) AS Income 
  ,c.Kidhome 
,c.Teenhome 
,c.Recency 
,c.Complain 
,p.NumWebPurchases
,p.NumCatalogPurchases
,p.NumStorePurchases
,p.NumWebVisitsMonth 
,q.MntWines
,q.MntFruits 
,q.MntMeatProducts
,q.MntFishProducts 
,q.MntSweetProducts
,q.MntGoldProds
,r.NumDealsPurchases
,r.AcceptedCmp1
,r.AcceptedCmp2 
,r.AcceptedCmp3 
,r.AcceptedCmp4 
,r.AcceptedCmp5 
,r.Response 
FROM 
  customer_details AS c 
  JOIN places_details AS p ON c.ID = p.ID 
  JOIN product_details AS q ON c.ID = q.ID 
  JOIN promotions_details AS r ON c.ID = r.ID;
