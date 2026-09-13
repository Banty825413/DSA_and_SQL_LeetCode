# Write your MySQL query statement below
with t1 as 
(   select user_id , count(user_id) as maxx
    from MovieRating
    group by user_id
    order by maxx desc
)
(select name as results
from Users 
join t1 using(user_id)
order by maxx desc ,name asc
limit 1 
)
UNION ALL

(select title as results
    from(
        select avg(rating) as avgg,movie_id,title
        from MovieRating
        join Movies using(movie_id)
        where created_at >="2020-02-01" and created_at <="2020-02-29"
        group by movie_id,title
        order by avgg desc , title asc
        limit 1
        ) as avr
)
    
