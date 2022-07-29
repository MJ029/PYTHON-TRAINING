USE sql_learning;

SELECT category, COUNT(ID) AS customers FROM 
(SELECT CASE WHEN Income < (SELECT AVG(Income) FROM customer_campaign) THEN "BELOW AVERAGE"
			WHEN Income >= (SELECT AVG(Income) FROM customer_campaign) THEN "ABOVE AVERAGE"
            ELSE "NOT FOUND" END AS category,
            ID
FROM customer_campaign
) AS tmp
GROUP BY category
ORDER BY category;