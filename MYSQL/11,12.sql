USE sql_learning;

-- Customers who are married and Having Only Kids in Home --
    
SELECT 
	ID
    ,martial_status
    ,Kidhome
FROM
	customer_campaign
WHERE
	martial_status ='married' AND Kidhome >=1;
    
-- Customers who are married and Having Only Teenagers in Home --
    
    SELECT 
	ID
    ,martial_status
    ,Teenhome
FROM
	customer_campaign
WHERE
	martial_status ='married' AND Teenhome >=1;