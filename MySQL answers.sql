175. 
SELECT FirstName, LastName, City, State 
  FROM Person LEFT JOIN Address ON Person.PersonID = Address.PersonID;


176. --- This was annoying. The simple solution won't return NULL, so you have to use IFNULL(). DISTINCT so
     --- equal salaries don't count as multiples.
SELECT 
  IFNULL(
      (SELECT Salary 
         FROM Employee 
       ORDER BY Salary DESC 
        LIMIT 1 OFFSET 1), 
      NULL) AS SecondHighestSalary;


177. 
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT; -- You have to declare variables in SQL, and you must assign variables before return.
  SET M = N - 1;
  RETURN (
    SELECT 
      IFNULL((SELECT DISTINCT Salary 
                FROM Employee
               ORDER BY Salary DESC LIMIT 1 OFFSET M), 
             NULL) 
  );
END


178. 
-- With windowing
SELECT 
  Score, 
  DENSE_RANK() OVER w AS 'Rank'
FROM Scores 
WINDOW w AS (ORDER BY Score DESC);

-- Without windowing
SELECT 
  Scores.Score, 
  ranking.Rank
FROM (SELECT 
        Score,
        (@rank := @rank + 1) AS 'Rank'
      FROM (SELECT 
              DISTINCT Score, 
              (@rank := 0)
            FROM Scores
            ORDER BY SCORE DESC) AS zero_scores
      ) AS ranking
JOIN Scores ON Scores.Score = Ranking.Score
ORDER BY ranking.Rank ASC;


180.
SELECT k.Num AS ConsecutiveNums 
FROM Logs i
JOIN Logs j
JOIN Logs k
WHERE i.Id = j.Id - 1 
  AND j.Id = k.Id - 1 
  AND i.Num = j.Num 
  AND i.Num = k.Num 
GROUP BY k.Num  -- Need GROUP BY to ensure that the same number isn't included twice.


181.
SELECT Employee.Name AS Employee FROM Employee
LEFT JOIN (SELECT * FROM Employee) AS manager
  ON manager.Id = Employee.ManagerId
WHERE manager.Salary < Employee.Salary


182.
SELECT Email 
FROM Person 
GROUP BY Email HAVING COUNT(Email) > 1


183. 
-- mySQL doesn't support EXCEPT.
SELECT Name AS Customers 
FROM Customers 
WHERE Id NOT IN (SELECT CustomerId FROM Orders)


184. --------------------- NOT WORKING ---------------------
SELECT 
    DISTINCT d.Name AS Department, 
    e.Name AS Employee, 
    e.Salary
FROM Employee e
JOIN Department d
  ON d.Id = e.DepartmentId
WHERE 
ORDER BY d.Id, e.Salary


196.
DELETE 
FROM Person 
WHERE Id NOT IN 
    (SELECT Id FROM 
        (SELECT  MIN(Id) AS Id -- Have to do sub-sub select here to 
                               -- create a new table;
                               -- can't delete from table I'm querying directly.
                               -- min() will get minimum before group by
           FROM Person
         GROUP BY Email) AS i)


197.
SELECT j.Id FROM
Weather i
JOIN Weather j -- Remember you can join without ON.
WHERE DateDiff(j.RecordDate, i.RecordDate) = 1 -- Have to use DateDiff here, simple subtraction doesn't work.
      AND j.Temperature > i.Temperature


595.
SELECT name, population, area 
FROM World
WHERE area > 3000000 
   OR population > 25000000


596.
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5


620.
SELECT id, movie, description, rating 
FROM cinema
WHERE id % 2 = 1
  AND description != "boring"
ORDER BY rating DESC


626.
SELECT 
    CASE WHEN id % 2 = 1 AND id = (SELECT COUNT(id) FROM seat)
         THEN id
         ELSE
            CASE WHEN id % 2 = 1
                 THEN id + 1
                 ELSE id - 1
            END
         END AS id,
    student
FROM seat 
ORDER BY id

-- Better:
SELECT 
    CASE WHEN id % 2 = 1 AND id = (SELECT COUNT(id) FROM seat) THEN id
         WHEN id % 2 = 1 THEN id + 1
         ELSE id - 1
    END AS id,
    student
FROM seat 
ORDER BY id


627.
UPDATE salary 
SET sex = CASE WHEN sex = "m" 
               THEN "f" 
               ELSE "m" 
          END

-- Probably better/faster:
UPDATE salary 
SET sex = IF(sex = "m", "f", "m")


1179.
-- My solution, using joins; kinda ugly
select jan.id, Jan_Revenue, Feb_Revenue
from
(select id, revenue as Jan_Revenue from department where month = 'Jan') as jan
join 
(select id, revenue as Feb_Revenue from department where month = 'Feb') as feb
on jan.id = feb.id
join
(select id, revenue as Mar_Revenue from department where month = 'Mar') as mar
on mar.id = jan.id
join
-- etc.

-- From discussion:

-- Using multiple selects
select a.id,
(select revenue from Department where month = 'Jan' and id = a.id) as Jan_Revenue,
(select revenue from Department where month = 'Feb' and id = a.id) as Feb_Revenue,
(select revenue from Department where month = 'Mar' and id = a.id) as Mar_Revenue,
-- etc.
from
(select distinct id as id from Department) a

-- Similar, but using case. Could also use max()
select id,
min(case when month = 'Jan' then Revenue end) as Jan_Revenue,
min(case when month = 'Feb' then Revenue end) as Feb_Revenue,
min(case when month = 'Mar' then Revenue end) as Mar_Revenue,
min(case when month = 'Apr' then Revenue end) as Apr_Revenue,
min(case when month = 'May' then Revenue end) as May_Revenue,
min(case when month = 'Jun' then Revenue end) as Jun_Revenue,
min(case when month = 'Jul' then Revenue end) as Jul_Revenue,
min(case when month = 'Aug' then Revenue end) as Aug_Revenue,
min(case when month = 'Sep' then Revenue end) as Sep_Revenue,
min(case when month = 'Oct' then Revenue end) as Oct_Revenue,
min(case when month = 'Nov' then Revenue end) as Nov_Revenue,
min(case when month = 'Dec' then Revenue end) as Dec_Revenue
from Department
group by id

-- Pivot table
select id
  , [Jan] as Jan_revenue
  , [Feb] as Feb_revenue
  , [Mar] as Mar_revenue
  , [Apr] as Apr_revenue
  , [May] as May_revenue
  , [Jun] as Jun_revenue
  , [Jul] as Jul_revenue
  , [Aug] as Aug_revenue
  , [Sep] as Sep_revenue
  , [Oct] as Oct_revenue
  , [Nov] as Nov_revenue
  , [Dec] as Dec_revenue
  from(
select * from department
pivot
(
sum(revenue)
for month in ([Jan],[Feb],[Mar],[Apr],[May],[Jun],[Jul],[Aug],[Sep],[Oct],[Nov],[Dec])) as pivot_tble) p

