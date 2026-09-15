# Write your MySQL query statement below
with t1 as (
   select stock_name,  sum(price) as total
from Stocks
where operation = "Buy"
group by stock_name
)
,t2 as 
(
    select stock_name, sum(price) as total2
    from Stocks 
    where operation = "Sell"
    group by stock_name
)
select stock_name , total2-total as capital_gain_loss
from t1 join t2 using(stock_name)