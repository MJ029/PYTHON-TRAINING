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
	AcceptedCmp1; 
    
    
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
	AcceptedCmp2;
    
    
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
	AcceptedCmp3;
	
    
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
	AcceptedCmp4;
    
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
	AcceptedCmp5;
	

	


