with t1 as (
    select users_id from Users where banned ='NO'
)
,t2 as (
select  request_at,status ,
case when status in ('cancelled_by_driver','cancelled_by_client') then 1 else 0 end as no_req
from Trips 
where client_id in (select users_id from t1) and 
driver_id in (select users_id from t1)
AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
)
select request_at as Day , round(sum(no_req) / count(*), 2) as 'Cancellation Rate'
from t2 
group by request_at