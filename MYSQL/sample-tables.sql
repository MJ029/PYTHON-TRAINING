USE sql_learning;

CREATE TABLE IF NOT EXISTS table_j(
id INT,
staff_name VARCHAR(250),
staff_age INT,
staff_city VARCHAR(250)
);

TRUNCATE TABLE table_j;

INSERT INTO table_j(id,staff_name,staff_age,staff_city)
VALUES(1,'gayu',23,'mumbai');
INSERT INTO table_j(id,staff_name,staff_age,staff_city)
VALUES(2,'nisha',24,'pune');
INSERT INTO table_j(id,staff_name,staff_age,staff_city)
VALUES(3,'harini',25,'noida');
INSERT INTO table_j(id,staff_name,staff_age,staff_city)
VALUES(4,'selvam',35,'mumbai');


CREATE TABLE IF NOT EXISTS table_j2(
payment_id INT,
dates DATE,
staff_id INT,
amount FLOAT
);


TRUNCATE TABLE table_j2;

INSERT INTO table_j2(payment_id,dates,staff_id,amount)
VALUES(101,'2009-12-30',1,3000.00);
INSERT INTO table_j2(payment_id,dates,staff_id,amount)
VALUES(102,'2010-02-22',3,2500.00);
INSERT INTO table_j2(payment_id,dates,staff_id,amount)
VALUES(103,'2010-02-03',4,3500.00);


SELECT staff_id, staff_name, staff_age, amount   
   FROM table_j as f, table_j2 as j  
   WHERE f.id =j.staff_id;
   
