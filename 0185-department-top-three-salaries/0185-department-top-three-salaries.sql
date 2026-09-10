# Write your MySQL query statement below
with t1 as (
    select d.name as Department , e.name as Employee , e.salary as Salary
    FROM Employee e JOIN Department d ON e.departmentId = d.id
)
,t2 as (
select Department , Employee, Salary , dense_rank() over (partition by Department order by Salary desc) rnk
from t1 
)

select Department ,Employee , Salary 
from t2 
where rnk <= 3

