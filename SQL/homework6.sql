-- задание 1 
-- Выбрать пассажиров и их места в рейсе:

SELECT 
    trips.id, name_passenger, place
FROM
    passengers
        JOIN
    Pass_in_trip ON passengers.id = Pass_in_trip.passenger
        JOIN
    trips ON trips.id = Pass_in_trip.trip;

-- Подсчитать общее количество пассажиров на конкретном рейсе:

SELECT 
    plane, town_from, town_to, COUNT(Pass_in_trip.passenger)
FROM
    trips
        JOIN
    Pass_in_trip ON trips.id = Pass_in_trip.trip
GROUP BY Pass_in_trip.trip;

-- посчитать рейсы, отправляющиеся после 2023-01-05:

SELECT 
    plane, town_from, town_to, time_out
FROM
    trips
WHERE
    time_out > '2023-01-05';

-- Посчитать количество рейсов, отправленных из каждого города:

SELECT 
    town_from, COUNT(id)
FROM
    trips
GROUP BY town_from;

-- Выбрать среднюю продолжительность рейсов для каждой компании:

SELECT 
    company_name, AVG(HOUR(TIMEDIFF(time_in, time_out)))
FROM
    trips
        JOIN
    companies ON trips.company = companies.id
GROUP BY trips.company;

-- Выбрать компании и количество рейсов, осуществленных каждой из них:

SELECT 
    company_name, COUNT(trips.id)
FROM
    trips
        JOIN
    companies ON trips.company = companies.id
GROUP BY trips.company;

-- Выбрать пассажиров, у которых имя начинается на 'J' и место в рейсе начинается на 'B':

SELECT 
    name_passenger, place
FROM
    Pass_in_trip
        JOIN
    passengers ON passengers.id = Pass_in_trip.passenger
WHERE
    place LIKE 'B%'
        AND name_passenger LIKE 'J%';
        
        
        
-- задание 2
-- 1. Запрос, который выводит все блюда из определенной категории (например, "Пиццы" или "Напитки").

SELECT 
    item_name
FROM
    menu
        JOIN
    category ON menu.category_id = category.category_id
WHERE
    category_name = 'Пиццы';

-- 2. Запрос, который выводит все заказы клиента по его идентификатору, включая дату заказа, статус и общую сумму.

SELECT 
    order_date, total_amount, status
FROM
    orders
WHERE
    customer_id = 1;

-- 3. Запрос, который считает общую сумму оплат за определенный период времени.

SELECT 
    SUM(amount_paid)
FROM
    Payment
WHERE
    payment_date < '2023-12-2'
        AND payment_date > '2023-11-2';


-- 4. Запрос, который подсчитывает количество заказов в разрезе статусов (например, "в обработке", "выполнен").

SELECT 
    COUNT(order_id)
FROM
    orders
GROUP BY status;


-- 5. Запрос, который вычисляет средний чек по всем заказам.


SELECT 
    AVG(total_amount)
FROM
    orders;

-- 6. Запрос, который выводит все заказы с определенным адресом доставки.

SELECT 
    *
FROM
    orders
        JOIN
    Delivery ON orders.order_id = Delivery.order_id
WHERE
    delivery_address = 'ул. Чайковского, 32';


-- 7. Запрос, который находит самые популярные блюда по количеству заказов.

SELECT 
    item_name, COUNT(Order_Item.menu_id)
FROM
    menu
        JOIN
    Order_Item ON Order_Item.menu_id = menu.menu_id
GROUP BY menu.menu_id
ORDER BY COUNT(Order_Item.menu_id) DESC;

-- ДОПОЛНИТЕЛЬНОЕ (можно сделать если сделали или задание 1 или задание 2 (или все вместе))
-- 1. найти всех пользователей и их адреса

SELECT 
    name, addr
FROM
    users
        JOIN
    user_addrs ON user_addrs.user = users.last_id;

-- 2. найти все заказы и заказанные предметы

SELECT 
    orders.last_id as "Номер заказа", items.title
FROM
    orders
        JOIN
    order_items ON orders.last_id = order_items.order_id
        JOIN
    items ON items.last_id = order_items.item_id;

-- 3. найти всех пользователей и их номера телефона

SELECT 
    name, phone
FROM
    users
        LEFT JOIN
    user_phones ON user_phones.user = users.last_id;

-- 4. посчитать кол-во пользователей сделавших заказ

SELECT 
    COUNT(DISTINCT user_id)
FROM
    orders;

-- 5. подсчитать общую сумму заказов для каждого пользователя

SELECT 
    name, SUM(price)
FROM
    orders
        LEFT JOIN
    users ON user_id = users.last_id
GROUP BY user_id;