create database emp_det;
# 1.age maxm 5 fname,lname,age,prof
select fname, lname, age, prof from customer1 order by age desc limit 5;

# 2.age minimum 3 fname,lname,age,prof
select fname, lname, age, prof from customer1 order by age limit 3;

# 3.india work fname,lname,age
select fname, lname, age from customer1 where loc = "india";

# 4.age above 50 fname,lname,age,prof
select fname, lname, age, prof from customer1 where age > 50;

# 5.age range 25 to 40 fname,lname,age
select fname, lname, age from customer1 where age >= 25 and age <= 40;

# 6.india work and prof dancer fname,lname,age
select fname, lname, age from customer1 where loc = "india" and prof = "dancer";

# 7.uk work, age maxm 2 emp fname,lname,age
select fname, lname, age from customer1 where loc = "uk" order by age desc limit 2;

# 8.india work age min 1 emp fname,lname,age,prof
select fname, lname, age, prof from customer1 where loc = "india" order by age limit 1;

# 9.pilot prof work, age maxm 1 emp fname,lname,age
select fname, lname, age from customer1 where prof = "pilot" order by age desc limit 1;

# 10.us work and age above 50 fname,lname,age,prof
select fname, lname, age, prof from customer1 where loc = "us" and age > 50;





