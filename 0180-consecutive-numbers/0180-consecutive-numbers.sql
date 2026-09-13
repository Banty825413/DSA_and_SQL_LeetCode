select distinct l1.num as consecutiveNums
from Logs l1
     join Logs l2 on l1.id = l2.id-1
     join Logs l3 on l2.id = l3.id -1
where l1.num = l2.num and l3.num = l2.num
