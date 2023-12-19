-- 1. Напишите запрос, который бы вывел список номеров Заказов, сопровождающихся именем заказчика, который создавал эти Заказы.
SELECT 
    orders.id, customers.cname
FROM
    customers,
    orders
WHERE
    customers.id = id_customer;
    
-- 2. Напишите запрос, который бы выдавал имена продавца и заказчика для каждого Заказа после номера Заказов.
SELECT 
    orders.id, amt, odate, sname as "продавец", cname as "покупатель"
FROM
    orders,
    salespeople,
    customers
WHERE
    orders.id_customer = customers.id
        AND orders.id_salesPeople = salespeople.id;

-- 3. Напишите запрос, который бы выводил всех заказчиков, обслуживаемых продавцом с комиссионными выше 12%. 
-- Выведите имя заказчика, имя продавца и ставку комиссионных продавца.
SELECT 
    cname, sname, comm
FROM
    salespeople,
    customers
WHERE
    id_salesPeople = salespeople.id
        AND comm >= 12;

-- 4. Напишите запрос, который вычислил бы сумму комиссионных продавца для каждого Заказа заказчика с оценкой выше 90.
SELECT 
    sname, orders.id, amt as "сумма заказа", (amt / 100 * comm) as "комиссионные за заказ"
FROM
    salespeople,
    customers,
    orders
WHERE    
    orders.id_customer = customers.id
        AND orders.id_salesPeople = salespeople.id
        AND rating > 90;

-- 5. Напишите запрос, который бы выдавал имена продавцов и заказчиков, проживающих в одном и том же городе.
SELECT 
    sname, cname
FROM
    salespeople,
    customers
WHERE
    id_salesPeople = salespeople.id    -- если имелись в виду заказчики, привязанные к продавцам
        AND salespeople.city = customers.city; -- если нет, то только эта строка

-- 6. Напишите запрос, который бы выдавал имена продавцов и заказчиков, проживающих в одном и том же городе и суммы их приобретений.
SELECT 
    sname, cname, amt
FROM
    salespeople,
    customers,
    orders
WHERE
    orders.id_customer = customers.id
        AND orders.id_salesPeople = salespeople.id
        AND salespeople.city = customers.city;

-- 7. Вывести попарно продавцов и покупателей из одного города.
SELECT 
    sname, cname
FROM
    salespeople,
    customers
WHERE
    salespeople.city = customers.city;

-- 8. Вывести пары продавец — покупатель, при условии, что у продавца комиссия ниже 20%, а у покупателя рейтинг ниже 90.
SELECT 
    sname, cname
FROM
    salespeople,
    customers,
    orders
WHERE
    orders.id_customer = customers.id
        AND orders.id_salesPeople = salespeople.id
        AND comm < 20
        AND rating < 90;

-- 1. Напишите запрос, который сосчитал бы все суммы заказов, выполненных в январе 2016 года.
SELECT 
    SUM(amt)
FROM
    orders
WHERE
    YEAR(odate) = 2016 AND MONTH(odate) = 1;

-- 2. Напишите запрос, кол-во покупателей, которых обслуживает продавец “Малкин” 
SELECT 
    COUNT(customers.id)
FROM
    salespeople,
    customers
WHERE
    id_salesPeople = salespeople.id
        AND sname = 'Малкин';

-- 3. Напишите запрос, который выбрал бы наименьшую скидку в городе среди продавцов. 
SELECT 
    city, MIN(comm)
FROM
    salespeople
GROUP BY salespeople.city;

-- 4. Напишите запрос, который бы считал сумму (заказ + заказ) продавцов чьи имена начинаются с буквы “П”. 
SELECT 
    sname, SUM(amt)
FROM
    salespeople,
    orders
WHERE
    id_salesPeople = salespeople.id
        AND sname LIKE 'П%'
GROUP BY sname;

-- 5. Напишите запрос, который выбрал бы среднюю скидку(comm) в каждом городе. 
SELECT 
    city, AVG(comm)
FROM
    salespeople
GROUP BY salespeople.city;