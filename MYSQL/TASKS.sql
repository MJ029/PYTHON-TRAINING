USE sql_learning;

SELECT 
c.ID,
c.Kidhome,
c.Income,
c.Teenhome,
c.Recency,
c.Complain,
p.NumWebPurchases,
p.NumCatalogPurchases,
p.NumStorePurchases,
p.NumWebVisitsMonth,
q.MntWines,
q.MntFruits,
q.MntMeatProducts,
q.MntFishProducts,
q.MntSweetProducts,
q.MntGoldProds,
r.NumDealsPurchases,
r.AcceptedCmp1,
r.AcceptedCmp2,
r.AcceptedCmp3,
r.AcceptedCmp4,
r.AcceptedCmp5,
r.Response,
STR_TO_DATE(c.Dt_customer, '%d-%m-%y') as join_date,
STR_TO_DATE(CONCAT(c.Year_Birth,'-01-01'),'%Y-%m-%d') as YOB,

TRIM(c.Education) as education,
TRIM(c.Marital_Status) as martial_status

FROM customer_details AS c

JOIN places_details AS p
ON c.ID = p.ID

JOIN product_details AS q
ON c.ID = q.ID

JOIN promotions_details AS r
ON c.ID = q.ID;

ALTER TABLE customer_details MODIFY Income DECIMAL(28, 8);

