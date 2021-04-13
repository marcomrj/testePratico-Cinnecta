/* Database used*/
CREATE DATABASE db_exercise2_1;

/* Required table */
CREATE TABLE employees(
    id INT PRIMARY KEY ,
    name VARCHAR(20) NOT NULL,
    age SMALLINT NOT NULL,
    adress VARCHAR(40) NOT NULL,
    salary DECIMAL(18,2) NOT NULL
);




/* Test Inserts */
INSERT INTO employees VALUES (1,'Billy Butcher',40,'Centro',6300.67);
INSERT INTO employees VALUES (2,'Hughie Campbell',28,'Santo Agostinho',3050.10);
INSERT INTO employees VALUES (3, 'Annie January', 26, 'Santo Agostinho', 4450.35);
INSERT INTO employees VALUES (4, 'Susan Raynor', 34, 'Nossa Senhora Aparecida', 2500);
INSERT INTO employees VALUES (5, 'Alastair Adana', 43, 'Serra', 4700.50);
INSERT INTO employees VALUES (6, 'Stan Edigar', 45, 'Belvedere', 4701.50);
INSERT INTO employees VALUES (7, 'Kimiko Miyashiro', 31, 'Buritis', 1100.10);
INSERT INTO employees VALUES (8, 'Grace Mallory', 41, 'Lourdes', 8040);


/* Main Function */
select * from employees where salary < (select salary from employees where id=5);
