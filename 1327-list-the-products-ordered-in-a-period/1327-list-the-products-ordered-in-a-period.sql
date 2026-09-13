# Write your MySQL query statement below
select 
    p.product_name,
    sum(o.unit)as unit
from Products p 
join Orders o using(product_id)
where o.order_date >="2020-02-01" and order_date <="2020-02-29"
group by product_name 

having  unit >= 100