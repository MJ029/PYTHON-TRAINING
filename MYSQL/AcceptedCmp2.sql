USE sql_learning;

-- Number of Customers who purchased product based on AcceptedCmp2 --

SELECT 
	COUNT(ID) as customers,
    AcceptedCmp2,
    MntMeatProducts,
	MntFishProducts,
	MntSweetProducts,
	MntGoldProds
FROM
	customer_campaign
GROUP BY
	AcceptedCmp2 
	


