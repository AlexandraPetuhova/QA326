-- 1.	На основе таблиц ниже, составьте запрос, где стоимость заказов больше 1000 и меньше 3000
SELECT 
    *
FROM
    orders
WHERE
    customer_id > 1000
        AND customer_id < 3000;
-- 2.	На основе таблиц ниже, составьте запрос за весенние месяцы 2016 года
SELECT 
    first_name, last_name, order_date
FROM
    orders,
    customers
WHERE
    orders.customer_id = customers.customer_id
        AND YEAR(order_date) = 2016
        AND MONTH(order_date) IN (3, 4, 5);
        
-- 3.	Покажите Пользователей у кого нет заказов
SELECT 
    first_name, last_name
FROM
    orders,
    customers
WHERE
	customers.customer_id NOT IN (SELECT customer_id FROM orders);


-- 1.	На основе таблиц ниже, составьте запрос, где будет показываться звонки за 2020/1/11 покупателям с фамилией на B
SELECT 
    customer_name, start_time, end_time
FROM
    calls,
    customer
WHERE
    customer.id = customer_id 
        AND DATE(start_time) = '2020-1-11'
        AND customer_name LIKE 'B%';

-- 2.	На основе таблиц ниже, составьте запрос кому звонил Thomas 
SELECT 
    customer_name
FROM
    calls,
    customer,
    employee
WHERE
    customer.id = customer_id
        AND employee.id = employee_id
        AND first_name LIKE 'Thomas%';

-- 3.	показы у кого были завершены звонки успешно 
SELECT 
    customer_name, first_name, last_name, start_time, end_time
FROM
    calls,
    customer,
    employee
WHERE
    customer.id = customer_id
        AND employee.id = employee_id
        AND call_outcome_id = 2;
        
-- Спроектировать  бд “семья”

CREATE TABLE IF NOT EXISTS family_members (
    member_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    statuss VARCHAR(30),
    member_name VARCHAR(50),
    birthday DATE
);

CREATE TABLE IF NOT EXISTS goods_type (
    t_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    t_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS goods (
    g_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    g_name VARCHAR(50),
    g_type INT,
    FOREIGN KEY (g_type)
        REFERENCES goods_type (t_id)
);

CREATE TABLE IF NOT EXISTS payments (
    p_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    amount INT,
    unit_price INT,
    p_date DATETIME,
    family_member INT,
    FOREIGN KEY (family_member)
        REFERENCES family_members (member_id),
    good INT,
    FOREIGN KEY (good)
        REFERENCES goods (g_id)
);

INSERT INTO family_members (statuss, member_name, birthday) VALUES
    ('mother', 'Mary', '1990-11-23'),
    ('father', 'John', '1988-05-15'),
    ('son', 'Michael', '2010-03-08'),
    ('daughter', 'Emily', '2013-09-21'),
    ('grandmother', 'Alice', '1955-12-10'),
    ('grandfather', 'Robert', '1950-08-02'),
    ('daughter', 'Sophia', '2018-06-14'),
    ('son', 'William', '2005-12-30'),
    ('father', 'David', '1975-04-18'),
    ('mother', 'Emma', '1985-09-07');
    
INSERT INTO goods_type (t_name) VALUES
    ('vegetables'),
    ('fruits'),
    ('electronics'),
    ('clothing'),
    ('books');
    
INSERT INTO goods (g_name, g_type) VALUES
    ('potato', 1),
    ('apple', 2),
    ('laptop', 3),
    ('jeans', 4),
    ('notebook', 5),
    ('carrot', 1),
    ('orange', 2),
    ('smartphone', 3),
    ('t-shirt', 4),
    ('fiction book', 5),
    ('cucumber', 1),
    ('banana', 2),
    ('headphones', 3),
    ('dress', 4),
    ('non-fiction book', 5);
    
INSERT INTO payments (amount, unit_price, p_date, family_member, good) VALUES
    (3, 50, '2023-12-09 09:14:50', 1, 3),
    (8, 20, '2023-12-10 12:30:15', 5, 8),
    (2, 35, '2023-12-11 14:45:30', 2, 5),
    (5, 15, '2023-12-12 17:00:45', 7, 1),
    (7, 40, '2023-12-13 19:15:00', 4, 7),
    (1, 25, '2023-12-14 21:30:15', 9, 2),
    (6, 30, '2023-12-15 23:45:30', 6, 14),
    (4, 18, '2023-12-16 10:00:45', 3, 12),
    (9, 22, '2023-12-17 12:15:00', 8, 6),
    (10, 28, '2023-12-18 14:30:15', 10, 9),
    (3, 33, '2023-12-19 16:45:30', 1, 11),
    (8, 19, '2023-12-20 19:00:45', 5, 13),
    (2, 45, '2023-12-21 21:15:00', 2, 4),
    (5, 12, '2023-12-22 23:30:15', 7, 15),
    (7, 38, '2023-12-23 10:45:30', 4, 1),
    (1, 26, '2023-12-24 13:00:45', 9, 8),
    (6, 32, '2023-12-25 15:15:00', 6, 3),
    (4, 17, '2023-12-26 17:30:15', 3, 5),
    (9, 23, '2023-12-27 19:45:30', 8, 7),
    (10, 29, '2023-12-28 22:00:45', 10, 1);

-- 1.1. Найти имена всех матерей (mother)
SELECT 
    member_name
FROM
    family_members
WHERE
    statuss = 'mother';
    
-- 1.2. Определить, кто из членов семьи покупал картошку (potato)
SELECT 
    member_name
FROM
    family_members,
    goods,
    payments
WHERE
    payments.good = g_id
        AND payments.family_member = member_id
        AND g_name = 'potato';
        
-- 1.3. Определить какие товары не были куплены 
SELECT DISTINCT
    g_name
FROM
    goods,
    payments
WHERE
    goods.g_id NOT IN (SELECT good FROM payments)