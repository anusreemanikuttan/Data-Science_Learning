use may_batch;
-- 1. Find Row count 
select count(*) from txn;

-- 2. jan month oid,cusno,category,product,state
--     A. Row count
create view jan as select oid, cuid, category, product, state from txn where dat between "01-01-2011" and "01-31-2011";
show tables;
select count(*) from jan;

-- 3. July Month oid,cusno,category,product,state
--     B. Row count 
create view jul as select oid, cuid, category, product, state from txn where dat between "07-01-2011" and "07-31-2011";
show tables;
select count(*) from jul;

-- 4. Each category [count desc sort] 
select category, count(*) as cat_count from txn group by category order by cat_count desc;
select * from txn where category = "Outdoor Recreation";

-- 6. Each paymethod count 
select method, count(*) from txn group by method;

-- 7. jan-july month purchase count [include] 
select count(*) as purchase from txn where dat between "01-01-2011" and "07-31-2011";

-- 8. Each category total amount 
select category, sum(pay_amount) from txn group by category;

-- 9. Each category maximum amount 
select category, max(pay_amount) from txn group by category;

-- 10. Each category avg amount 
select category, avg(pay_amount) from txn group by category;

-- 11.total amount by cash and credit card
select method, sum(pay_amount) from txn group by method;

-- 12. Indoor games ,total amount 
select category, sum(pay_amount) as tot_amount from txn where category = "indoor games" group by category;

-- 13. Each state count 
select state, count(*) from txn group by state;