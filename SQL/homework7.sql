--  составьте БД (минимум из 3 таблиц) на произвольную тему 

create database if not exists petshop;
use petshop;

CREATE TABLE if not exists Item_groups
(
  group_id INT PRIMARY KEY AUTO_INCREMENT,
  gname VARCHAR(30)
);

INSERT INTO Item_groups(gname) VALUES
("Pets"),
("Pet food"),
("Pet toys"),
("Accessories");

CREATE TABLE if not exists Customers
(
  customer_id INT PRIMARY KEY AUTO_INCREMENT,
  cname VARCHAR(30)
);

INSERT INTO Customers(cname) VALUES
("George Clooney"), ("Kevin Costner"), ("Donald Sutherland"), 
("Jennifer Lopez"), ("Ray Liotta"), ("Samuel L. Jackson"), 
("Nikole Kidman"), ("Alan Rickman"), ("Kurt Russell"), ("Harrison Ford"), 
("Russell Crowe"), ("Steve Martin"), ("Michael Caine"), ("Angelina Jolie"), 
("Mel Gibson"), ("Michael Douglas"), ("John Travolta"), ("Sylvester Stallone"), 
("Tommy Lee Jones"), ("Catherine Zeta-Jones"), ("Antonio Banderas"), ("Kim Basinger"), 
("Sam Neill"), ("Gary Oldman"), ("Clint Eastwood"), ("Brad Pitt"), ("Johnny Depp"), 
("Pierce Brosnan"), ("Sean Connery"), ("Bruce Willis"), ("Mullah Omar"), ("Leonardo Grant-Baker");

CREATE TABLE if not exists Items
(
  item_id INT PRIMARY KEY AUTO_INCREMENT,
  iname VARCHAR(30),
  price INT,
  group_id INT,
  FOREIGN KEY (group_id) REFERENCES Item_groups(group_id)
);

INSERT INTO Items (iname, price, group_id) VALUES
("Cat", 1500, 1),
("Dog", 1800, 1),
("Parrot", 2300, 1),
("Mouse", 500, 1),
("Hamster", 700, 1),
("Fish", 200, 1),
("Kittycat", 200, 2),
("Chappy", 300, 2),
("Purina", 400, 2),
("GO", 1500, 2),
("Sirius", 700, 2),
("Poyal Canin", 400, 2),
("Mouse", 230, 3),
("Ball", 130, 3),
("Bone", 50, 3),
("Scratching post", 3400, 4),
("Collar", 1400, 4),
("Leash", 1400, 4),
("Drinker", 1800, 4),
("Carrier", 2400, 4),
("Bowl", 300, 4);

CREATE TABLE if not exists Purchase
(
  purchase_id INT PRIMARY KEY AUTO_INCREMENT,
  count INT,
  pdate DATE,
  customer_id INT,
  item_id INT,
  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
  FOREIGN KEY (item_id) REFERENCES Items(item_id)
);

INSERT INTO Purchase (count, pdate, customer_id, item_id) VALUES
(1, '2023-11-01', 31, 2),
(2, '2023-11-02', 12, 7),
(3, '2023-11-03', 2, 15),
(4, '2023-11-04', 25, 10),
(1, '2023-11-05', 12, 5),
(2, '2023-11-06', 13, 18),
(3, '2023-11-07', 23, 12),
(4, '2023-11-08', 16, 21),
(1, '2023-11-09', 14, 6),
(2, '2023-11-10', 16, 17),
(3, '2023-11-11', 29, 9),
(4, '2023-11-12', 27, 3),
(1, '2023-11-13', 18, 20),
(2, '2023-11-14', 1, 14),
(3, '2023-11-15', 24, 8),
(4, '2023-11-16', 14, 19),
(1, '2023-11-17', 3, 11),
(2, '2023-11-18', 14, 4),
(3, '2023-11-19', 29, 13),
(4, '2023-11-20', 17, 1),
(1, '2023-11-21', 30, 16),
(2, '2023-11-22', 14, 5),
(3, '2023-11-23', 27, 2),
(4, '2023-11-24', 4, 7),
(1, '2023-11-25', 3, 15),
(2, '2023-11-26', 10, 10),
(3, '2023-11-27', 23, 21),
(4, '2023-11-28', 26, 12),
(1, '2023-11-29', 20, 9),
(2, '2023-11-30', 15, 6);


-- Вся информация целиком

CREATE VIEW all_tables AS
    SELECT 
        iname, gname, price, purchase_id, count, pdate, cname
    FROM
        purchase
            JOIN
        customers ON customers.customer_id = purchase.customer_id
            JOIN
        items ON items.item_id = purchase.item_id
            JOIN
        item_groups ON item_groups.group_id = items.group_id;

SELECT 
    *
FROM
    all_tables;

-- Покупатели без покупок

SELECT 
    cname
FROM
    customers
        LEFT JOIN
    purchase ON customers.customer_id = purchase.customer_id
WHERE
    purchase.purchase_id IS NULL;

-- Покупатели с количеством покупок больше 1 и суммой покупок больше 2000

SELECT 
    cname AS Name,
    COUNT(purchase_id) AS Count,
    SUM(price * count) AS Sum
FROM
    all_tables
GROUP BY cname
HAVING SUM(price * count) > 2000 and COUNT(purchase_id) > 1;

-- Товары по популярности

SELECT 
    items.iname AS Item,
    IF(COUNT(purchase_id) > 1,
        'Popular',
        'Not popular') AS Popularity,
    SUM(items.price * count) AS Sum
FROM
    all_tables
        left JOIN
    items ON all_tables.iname = items.iname
GROUP BY items.iname
ORDER BY COUNT(purchase_id) DESC;


-- задание 2
-- 1. Запрос на получение информации о ресторане:
-- Получить название, адрес и контактный телефон ресторана с идентификатором 1.

SELECT 
    Name, Address, Phone
FROM
    Restaurant
WHERE
    RestaurantID = 1;

-- 2. Запрос на выборку доступных столов:
-- Получить номера и вместимость столов, доступных для бронирования в ресторане с идентификатором 2.

SELECT 
    TableID, Capacity
FROM
    Tables
        JOIN
    Restaurant ON Tables.RestaurantID = Restaurant.RestaurantID
WHERE
    Restaurant.RestaurantID = 2
        AND IsAvailable;

-- 3. Запрос на получение списка бронирований для ресторана:
-- Получить информацию о бронированиях, включая идентификатор бронирования, имя клиента, номер столика и время бронирования для столов из ресторана с идентификатором 3.

SELECT 
    ReservationID,
    Customers.Name,
    Tables.TableID,
    ReservationTime
FROM
    Reservations
        JOIN
    Customers ON Reservations.CustomerID = Customers.CustomerID
        JOIN
    Tables ON Reservations.TableID = Tables.TableID
        JOIN
    Restaurant ON Tables.RestaurantID = Restaurant.RestaurantID
WHERE
    Restaurant.RestaurantID = 3;

-- 4. Запрос на получение списка официантов для ресторана:
-- Получить идентификатор и имя официантов, работающих в ресторане с идентификатором 4.

SELECT 
    WaiterID, Name
FROM
    Waiters
WHERE
    RestaurantID = 4;

-- 5. Запрос на обновление данных о столике:
-- Изменить статус доступности столика с номером 5 на "недоступен".

UPDATE Tables 
SET 
    IsAvailable = FALSE
WHERE
    TableID = 5;

-- 6. Запрос на удаление клиента из базы данных:
-- Удалить информацию о клиенте с идентификатором 6 из базы данных.

DELETE FROM Reservations 
WHERE
    CustomerID = 6;
DELETE FROM Customers 
WHERE
    CustomerID = 6;

-- 7. Запрос на получение информации о бронировании по идентификатору:
-- Получить все данные о бронировании с идентификатором 7.

SELECT 
    Customers.CustomerID,
    Customers.Name,
    Email,
    Customers.Phone,
    ReservationTime,
    Tables.TableID,
    Capacity,
    IsAvailable,
    Restaurant.RestaurantID,
    Restaurant.Name,
    Address,
    Restaurant.Phone
FROM
    Reservations
        JOIN
    Tables ON Tables.TableID = Reservations.TableID
        JOIN
    Customers ON Customers.CustomerID = Reservations.CustomerID
        JOIN
    Restaurant ON Restaurant.RestaurantID = Tables.RestaurantID
WHERE
    ReservationID = 7;

-- 8. Запрос на подсчет количества столов в ресторане:
-- Получить общее количество столов в ресторане с идентификатором 8.

SELECT 
    COUNT(TableID)
FROM
    Tables
        JOIN
    Restaurant ON Restaurant.RestaurantID = Tables.RestaurantID
WHERE
    Restaurant.RestaurantID = 8;

-- 9. Запрос на выборку столов по вместимости:
-- Получить номера и вместимость столов, вместимость которых больше или равна 6.

SELECT 
    Restaurant.name, Tables.TableID, Capacity
FROM
    Tables
        JOIN
    Restaurant ON Restaurant.RestaurantID = Tables.RestaurantID
WHERE
    Capacity >= 6;

-- 10. Запрос на поиск информации о клиенте по имени:
-- Найти всех клиентов, имя которых содержит "John".

SELECT 
    *
FROM
    Customers
WHERE
    Name LIKE '%John%';
    
    
    
    
-- задание 3 
-- 3.	подсчитать кол-во товаров

SELECT 
    COUNT(last_id)
FROM
    items;

-- 4.	посчитать общую стоимость товаров 

SELECT 
    SUM(price)
FROM
    items;

-- 5.	посчитать кол-во товаров у которых есть фото

SELECT 
    COUNT(last_id)
FROM
    items
WHERE
    image IS NOT NULL;