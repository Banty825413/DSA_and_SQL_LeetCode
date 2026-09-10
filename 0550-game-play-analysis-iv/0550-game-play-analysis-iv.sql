with t1 as (select player_id , datediff(event_date, min(event_date) over (partition by player_id )) = 1 as diff
from Activity)

select round(sum(diff) / count(distinct player_id),2)
as fraction
from t1