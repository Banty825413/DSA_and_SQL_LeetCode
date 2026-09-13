# Write your MySQL query statement below
-- first less than 30k , second no manager
select employee_id 
from Employees
where salary < 30000 and manager_id not in (select employee_id from Employees)
order by employee_id