-- We can use this SQL script to extract and clean customer data for churn prediction. But you can change it according to your database configurations.

SELECT
    c.customer_id,
    c.gender,
    c.age,
    c.tenure,
    c.balance,
    c.num_of_products,
    c.has_cr_card,
    c.is_active_member,
    c.estimated_salary,
    CASE 
        WHEN c.churn = 'Yes' THEN 1
        ELSE 0
    END AS churn
FROM
    customers c
