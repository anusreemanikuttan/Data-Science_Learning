# create a new database --> college
# create a table --> students -- id, name, age, loc
#add 5 records

create database college;
use college;
create table students(id int, name varchar(20), age int, loc varchar(30));
insert into students(id, name, age, loc) values
(12, "anusree", 22, "Pdlm"),
(2, "abhimanyu", 22, "klnd"),
(15, "abhinav", 13, "mud"),
(34, "smith", 25, "nrd"),
(26, "joe", 24, "fld");
