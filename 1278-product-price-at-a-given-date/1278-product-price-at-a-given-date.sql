# Write your MySQL query statement below
-- SELECT product_id, 
--     IF((SELECT COUNT(change_date) FROM Products WHERE product_id=P.product_id AND change_date="2019-08-16")>0,
--     (SELECT new_price FROM Products WHERE product_id=P.product_id AND change_date="2019-08-16"),
--     IF((SELECT COUNT(change_date) FROM Products WHERE product_id=P.product_id AND change_date<"2019-08-16")>0,
--     (SELECT new_price FROM Products WHERE product_id=P.product_id AND change_date<"2019-08-16" ORDER BY change_date DESC LIMIT 1),
--     10)) AS price FROM Products P GROUP BY product_id

SELECT product_id, 
    IF((SELECT COUNT(change_date) FROM Products WHERE product_id=P.product_id AND change_date<="2019-08-16")>0,
    (SELECT new_price FROM Products WHERE product_id=P.product_id AND change_date<="2019-08-16" ORDER BY change_date DESC LIMIT 1),
    10) AS price FROM Products P GROUP BY product_id   