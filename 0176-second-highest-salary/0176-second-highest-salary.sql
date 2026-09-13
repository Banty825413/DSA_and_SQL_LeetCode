SELECT 

(
    SELECT salary  
        FROM( 
            SELECT salary , 
                            DENSE_RANK()  OVER (ORDER BY salary DESC) rnk
            FROM Employee
            ) AS ranked
        WHERE rnk = 2
LIMIT  1) AS  SecondHighestSalary