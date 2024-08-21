# Write your MySQL query statement below
WITH temp AS(
    SELECT customer_id, 
    (SELECT MIN(order_date) FROM Delivery WHERE customer_id=D.customer_id) AS m_o, 
    customer_pref_delivery_date AS m_d 
    FROM Delivery D)
SELECT ROUND((SELECT COUNT(customer_id) FROM temp WHERE m_o=m_d)/(SELECT COUNT(DISTINCT customer_id) FROM Delivery), 4)*100 AS immediate_percentage