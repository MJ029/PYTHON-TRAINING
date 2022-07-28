USE sql_learning;

-- Number of Customers who purchased product based on AcceptedCmp5 --

SELECT 
	COUNT(ID) as customers,
    AcceptedCmp5,
    MntMeatProducts,
	MntFishProducts,
	MntSweetProducts,
	MntGoldProds
FROM
	customer_campaign
GROUP BY
	AcceptedCmp5 
	


