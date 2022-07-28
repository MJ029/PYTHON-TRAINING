USE sql_learning;

-- Number of Customers who purchased product based on AcceptedCmp4 --

SELECT 
	COUNT(ID) as customers,
    AcceptedCmp4,
    MntMeatProducts,
	MntFishProducts,
	MntSweetProducts,
	MntGoldProds
FROM
	customer_campaign
GROUP BY
	AcceptedCmp4 
	


