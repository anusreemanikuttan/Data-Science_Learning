use may_batch;
create table table1(id int, fname varchar(15), lname varchar(15), age int, loc varchar(20));
insert into table1(id, fname, lname, age, loc) values(1, "ann", "jose", 22, "ekm"),
(2, "anju", "k", 23, "ekm"),(3, "arun", "m", 24, "clt"), (4, "kiran", "j", 23, "ekm");
select * from table1;

create table table2(prof varchar(20),id int, salary int);
insert into table2(prof, id, salary) values("testing", 3, 1000),
("python", 4, 3000),
("java", 5, 2000);
select * from table2;

select a.id, a.fname, a.lname, a.age, a.loc, b.prof, b.salary from table1 a join table2 b on(a.id = b.id);

-- from custom table and order table
-- 1. name, age, loc, sal, dat, amt

select c.name, c.age, c.location, c.salary, o.dat, o.amount from custom c join order_w o on(c.id = o.id);

select c.*, o.dat, o.amount from custom c join order_w o on(c.id = o.id);

select c.name, c.age, c.location, o.dat, o.amount from custom c join order_w o on(c.id = o.id) where c.salary > 2000;

select c.name, c.age, o.dat, o.amount from custom c join order_w o on(c.id = o.id) order by c.age desc limit 1;


select m.name, m.roll, n.res from student m join result n on(m.roll = n.roll) where n.res = "pass";

