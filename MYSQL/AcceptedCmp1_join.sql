USE sql_learning;

 -- Number of Customers who purchased product based on number of attempts --
 
 SELECT
	 COUNT(prod.ID) as customers,
		AcceptedCmp1,
		MntMeatProducts,
		MntFishProducts,
		MntSweetProducts,
		MntGoldProds
FROM
		product_details AS prod
	JOIN promotions_details AS prom ON prod.ID = prom.ID
GROUP BY
	AcceptedCmp1