-- Solution using MS SQL Server

SELECT d.NAME as 'DEPT_NAME', AVG(s.AMT_USD) as 'AVG_MONTHLY_SALARY (USD)'
FROM
(SELECT TOP 3 *
FROM Departments) AS d  -- a new table for top 3 departments
JOIN Employees AS e     -- joined Departments table with Employee table using their ids
ON d.ID = e.DEPT_ID
JOIN Salaries AS s      -- joined the resultant table with Salaries table using their ids
ON e.ID = s.EMP_ID
GROUP BY d.NAME         -- grouped the result by the names of the departments


-- I downloaded the csv files for the given tables and imported the data on MS SQL Server to the result.