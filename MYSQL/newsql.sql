CREATE DATABASE IF NOT EXISTS surya_dev;

USE surya_dev;

CREATE TABLE IF NOT EXISTS employee_details (
emp_id INT,
emp_name VARCHAR(250),
emp_salary FLOAT,
emp_monthlybonus FLOAT
);

SELECT * FROM  employee_details;
INSERT INTO employee_details (emp_id,emp_name,emp_salary,emp_monthlybonus)
VALUES(101,'Tushar',25000,4000);
INSERT INTO employee_details (emp_id,emp_name,emp_salary,emp_monthlybonus) 
VALUES(102,'Anuj',30000,200);
SELECT emp_salary + 20000 as emp_new_salary FROM employee_details;  
SELECT * FROM  employee_details;