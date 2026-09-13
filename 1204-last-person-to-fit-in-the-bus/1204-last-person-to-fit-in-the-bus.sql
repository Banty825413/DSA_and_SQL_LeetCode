

with t2 as (
        select person_name, turn , sum(weight) over(order by turn) as total_weight
        from Queue
)


select person_name from  
t2 
where total_weight <= 1000
order by total_weight desc 
limit 1 