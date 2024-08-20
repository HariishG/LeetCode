# Write your MySQL query statement below
WITH temp as(
    SELECT user_id, 
            (SELECT COUNT(action) FROM Confirmations WHERE user_id = Signups.user_id AND action = "confirmed")/
            (SELECT COUNT(action) FROM Confirmations WHERE user_id = Signups.user_id) AS confirmation_rate
    FROM Signups
)
SELECT user_id, IF(confirmation_rate IS NULL, 0, ROUND(confirmation_rate,2)) AS confirmation_rate FROM temp