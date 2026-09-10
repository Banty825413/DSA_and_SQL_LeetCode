# Write your MySQL query statement below
with t1 as 
(   SELECT d.name AS Department , e.name AS Employee , e.salary AS Salary
    FROM Employee e 
    JOIN Department d ON  e.departmentId = d.id
)
,
t2 as (
    select Department , Employee , Salary , Dense_rank() over (partition by  Department order by Salary desc) rnk 
    FROM t1 ) 

select Department , Employee , Salary FROM t2
where rnk = 1
