# Write your MySQL query statement below
SELECT "Low Salary" AS category, (SELECT COUNT(*) FROM Accounts WHERE income<20000) AS accounts_count
UNION ALL
SELECT "Average Salary" AS category, (SELECT COUNT(*) FROM Accounts WHERE income>=20000 and income<=50000) AS accounts_count
UNION ALL
SELECT "High Salary" AS category, (SELECT COUNT(*) FROM Accounts WHERE income>50000) AS accounts_count