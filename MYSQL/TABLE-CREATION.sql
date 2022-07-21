CREATE DATABASE IF NOT EXISTS sql_learning;

USE sql_learning;

-- creating table --

CREATE TABLE IF NOT EXISTS table_creation(
id INT NOT NULL,
student_name VARCHAR(250)NOT NULL,
age INT NOT NULL,
city VARCHAR(250),
PRIMARY KEY(id)
);

-- creating a #table using last table --  

CREATE TABLE IF NOT EXISTS table2 AS
SELECT id,student_name,city
FROM table_creation;

-- dropping a table --

DROP TABLE table2;

-- renaming a table --

ALTER TABLE table_creation RENAME TO table1; 

-- adding new columns to table --

ALTER TABLE table1 ADD phone_number INT; 
