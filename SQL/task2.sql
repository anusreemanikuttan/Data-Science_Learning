use may_batch;
select count(*) from person;

each prof count from customer table
select prof, count(*) from customer group by prof;
select age, count(*) from customer group by age;

select prof, count(*) as prof_count from customer group by prof order by prof_count desc;

select prof, count(*) as prof_count from customer where loc = "india" group by prof order by prof_count;

select prof, max(age) as prof_max_age from customer group by prof;

select prof, min(age) as prof_min_age from customer group by prof;

