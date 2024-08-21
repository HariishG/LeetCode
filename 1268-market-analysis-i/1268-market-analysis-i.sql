# Write your MySQL query statement below
SELECT U.user_id AS buyer_id, U.join_date, COUNT(buyer_id) as orders_in_2019 
    FROM Users U LEFT JOIN (SELECT * FROM Orders WHERE order_date LIKE "2019%") O
    ON (O.buyer_id=U.user_id)
    GROUP BY U.user_id