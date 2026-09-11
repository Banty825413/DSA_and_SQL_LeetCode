with t1 as (
    SELECT d.name as Department,e.name AS Employee  , e.salary as Salary
    FROM Employee e JOIN Department d on e.departmentId = d.id
)
,t2 AS(
    select Department , Employee , Salary , Dense_rank() over (partition by Department ORDER BY Salary desc) rnk
    FROM t1
)
SELECT Department , Employee, Salary 
FROM  t2 
WHERE rnk = 1