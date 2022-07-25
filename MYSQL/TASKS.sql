USE sql_learning;

SELECT 
str_to_date(c.Dt_customer, '%d-%m-%y') as join_date

CONVERT(Year_Birth, DATE);


FROM customer_details AS c

JOIN places_details AS p
ON c.ID = p.ID

JOIN product_details AS q
ON c.ID = q.ID

JOIN promotions_details AS r
ON c.ID = q.ID

