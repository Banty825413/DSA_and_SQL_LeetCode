# Write your MySQL query statement below
with t as (Select distinct teacher_id , subject_id from Teacher)
select distinct teacher_id , count(subject_id)over (partition by teacher_id  ) as cnt 
from t