use may_batch;
create table student_2(id int primary key auto_increment, name varchar(15) unique, dept varchar(10) not null,
marks int not null);
insert into student_2(name, dept, marks) values('Anu','CSE',85), ('Rahul','ECE',72),
('Meera','CSE',91), ('Akhil','EEE',65), ('Nisha','ECE',88), ('Arjun','CSE',78),
('Diya','EEE',95), ('Vinay','ECE',70);
select * from student_2;


-- 1. Find students who scored more than the average mark.
select * from student_2 where marks > (select avg(marks) from student_2);

-- 2. Find the students with the highest mark.
select * from student_2 where marks = (select max(marks) from student_2);

-- 3. Find the students with the lowest mark.
select * from student_2 where marks = (select min(marks) from student_2);

-- 4. Find students whose marks are less than the average mark.
select * from student_2 where marks < (select avg(marks) from student_2);

-- 5. Find students who scored more than Rahul.
select * from student_2 where marks > (select marks from student_2 where name = "rahul");

-- 6. Find students who scored more than Nisha.
select * from student_2 where marks > (select marks from student_2 where name = "nisha");

-- 7. Find students from the same department as Meera.
select * from student_2 where dept = (select dept from student_2 where name = "meera");

-- 8. Find students whose marks are equal to the maximum mark.
select * from student_2 where marks = (select max(marks) from student_2);

-- 9. Find students whose marks are less than the average mark of the CSE department.
select * from student_2 where marks < (select avg(marks) from student_2 where dept = "cse");

