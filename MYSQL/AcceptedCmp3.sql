USE sql_learning;

-- Number of Customers who purchased product based on AcceptedCmp3 --

SELECT 
	COUNT(ID) as customers,
    AcceptedCmp3,
    MntMeatProducts,
	MntFishProducts,
	MntSweetProducts,
	MntGoldProds
FROM
	customer_campaign
GROUP BY
	AcceptedCmp3 
	


