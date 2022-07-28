USE sql_learning;

-- Number of Customers who purchased product based on AcceptedCmp1 --

SELECT 
	COUNT(ID) as customers,
    AcceptedCmp1,
    MntMeatProducts,
	MntFishProducts,
	MntSweetProducts,
	MntGoldProds
FROM
	customer_campaign
GROUP BY
	AcceptedCmp1 
	


