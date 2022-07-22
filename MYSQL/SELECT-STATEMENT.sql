USE sql_learning;

-- creating a table for SQL-select tasks --                                  

CREATE TABLE IF NOT EXISTS select_stmt(
car_num  INT,
car_name  VARCHAR(250),
car_colour  VARCHAR(250),
car_price  INT
);

TRUNCATE TABLE select_stmt;
 
INSERT INTO select_stmt (car_num,car_name,car_colour,car_price)
VALUES(01,'suzuki','red',200000);
INSERT INTO select_stmt (car_num,car_name,car_colour,car_price)
VALUES(02,'city','green',400000);
INSERT INTO select_stmt (car_num,car_name,car_colour,car_price)
VALUES(03,'creta','blue',500000);
INSERT INTO select_stmt (car_num,car_name,car_colour,car_price)
VALUES(04,'venue','red',200000);
INSERT INTO select_stmt (car_num,car_name,car_colour,car_price)
VALUES(05,'polo','green',400000);
INSERT INTO select_stmt (car_num,car_name,car_colour,car_price)
VALUES(06,'verna','blue',500000);
INSERT INTO select_stmt (car_num,car_name,car_colour,car_price)
VALUES(07,'breeza','red',200000);

-- selecting (*) for selecting all rows --

SELECT * FROM select_stmt;

-- for selecting certain rows --

SELECT car_name,car_price FROM select_stmt;

-- selecting using WHERE clause -- 

SELECT car_name,car_price FROM select_stmt WHERE car_price = 200000;

-- using GROUP BY clause --

SELECT count(car_name),car_colour FROM select_stmt GROUP BY car_colour;

-- using HAVING clause --

SELECT count(car_name),car_price FROM select_stmt GROUP BY car_price HAVING car_price > 300000;

-- using ORDER BY -- 

SELECT * FROM select_stmt ORDER BY car_num desc;

-- select DISTINCT command -- 

SELECT DISTINCT car_colour FROM select_stmt;

-- using count() --

SELECT count(car_colour) AS total_colours FROM select_stmt;

-- using count(DISTINCT) --

SELECT count(DISTINCT car_colour) AS unique_colour FROM select_stmt;

-- using RANDOM -- 

SELECT car_price FROM select_stmt ORDER BY rand() LIMIT 1;

-- using SUM functions --

SELECT SUM(car_price) FROM select_stmt WHERE car_price > 300000;

