# Write your MySQL query statement below
with t as 
(select turn , weight from Queue 
    order by turn )

,t2 as (
        select turn , sum(weight) over(order by turn) as total_weight
    from t
)
,t3 as 
    (select turn ,total_weight
    from t2
    where total_weight <=1000
    order by total_weight desc
    limit 1
    )

select person_name from Queue 
where turn  in (select turn from t3)