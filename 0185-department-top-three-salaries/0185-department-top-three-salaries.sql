with t as 
    (select d.name as Department, e.name as Employee , e.salary as Salary , 
    dense_rank() over (partition by d.name order by Salary desc ) rnk
    FROM Employee e left join Department d on e.departmentId = d.id
    )
select Department , Employee , Salary
from t 
where rnk <=3
