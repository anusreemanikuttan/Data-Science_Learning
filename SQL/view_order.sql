use may_batch;
select * from customer;

select fname, lname from customer;

select fname, age, prof from customer;

select fname, lname, age, prof from customer limit 5;

# collect the fname, lname, age of the first 5 persons from person table

select `First Name`, `Last Name`, age from person limit 5;

select * from person where age > 21;

select `First Name`, `Last Name`, age from person where age = 22;

select `First Name`, `Last Name`, age, city from person where city = "chennai";

select * from person where age > 20 and city = "chennai";

# View Table

create view chennai_data as select * from person where age > 20 and city = "chennai";
show tables;
drop view chennai_data;

# Order by

select * from person order by age;

select * from person order by age desc;

select * from person order by city;

select * from person order by city desc;

select fname, lname, age, prof from customer order by age desc limit 2;
select fname, lname, age from customer order by age limit 1;
create view uk_loc as select fname, lname, age, prof from customer where loc = "uk" order by age desc limit 3;
show tables;