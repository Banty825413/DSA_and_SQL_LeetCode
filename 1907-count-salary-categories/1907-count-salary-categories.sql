# Write your MySQL query statement below
with t1 as (
    select account_id , 
    case
        when income < 20000 then "Low Salary"
        when  income between 20000 and 50000 then "Average Salary"
        when income > 50000 then "High Salary" 
        end as category
    from Accounts
    )
select  "Low Salary" as category , count(*) as accounts_count
from t1  where category = "Low Salary"
union
select  "Average Salary" as category , count(*) as accounts_count
from t1  where category = "Average Salary"
union 
select  "High Salary" as category , count(*) as accounts_count
from t1  where category = "High Salary"