use may_batch;
create table emp(id int primary key auto_increment, name varchar(15) not null, age int unique, 
dept varchar(10) not null, salary int not null, join_yr int not null);
desc emp;

insert into emp(name, age, dept, salary, join_yr) values("Alice", 25, "HR", 35000, 2019),
("Bob", 28, "Finance" , 40000, 2018), ("Charlie", 30, "IT", 50000, 2020), 
("David", 26, "Finance", 42000, 2021), ("Eva", 32, "HR", 37000, 2017),
("Frank", 27, "IT", 48000, 2022), ("Grace", 29, "Marketing", 39000, 2019),
("Helen", 31, "Finance", 41000, 2016), ("Ian", 24, "Marketing", 36000, 2023),
("Jane", 33, "IT", 52000, 2015);
select * from emp;

-- 1.Count the total number of employees.
select count(*) from emp;

-- 2.Find the minimum age of employees.
select min(age) as min_age from emp group by age limit 1;

-- 3.Find the maximum salary.
select max(salary) as max_salary from emp limit 1;

-- 4.Find the average salary.
select avg(salary) as avg_salary from emp limit 1;

-- 5.Display all records sorted by age in ascending order.
select * from emp order by age;

-- 6.Display the top 3 highest-paid employees.
select * from emp order by salary desc limit 3;

-- 7.Show details of employees who joined after 2020.
select * from emp where join_yr > 2020;

-- 8.Count the number of employees in each department.
select dept, count(*) from emp group by dept;

-- 9.Which department has the highest average salary?
select dept, avg(salary) as high_avg_salary from emp group by dept 
order by high_avg_salary desc limit 1;

-- 10.What is the total salary paid to the Finance department?
select dept, sum(salary) as tot_salary from emp where dept = "finance" group by dept;

-- 11.List employees who earn more than the average salary.
select * from emp where salary > (select avg(salary) from emp);

-- 12.How many employees are above 30 years of age?
select count(*) from emp where age > 30;

-- 13.Find the department with the maximum number of employees.
select dept, count(*) as emp_count from emp group by dept order by emp_count desc limit 1;

-- 14.Show the name and department of the youngest employee.
select name, dept from emp where age = (select min(age) from emp);

-- 15.Calculate the difference between the highest and lowest salary.
select max(salary) - min(salary) as salary_diff from emp;
