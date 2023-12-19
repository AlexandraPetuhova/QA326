CREATE DATABASE IF NOT EXISTS homework3;
USE homework3;

-- Спроектировать бд “банк”
-- необходимо спроектировать таблицы “счета” и “клиенты”

CREATE TABLE IF NOT EXISTS clients (
    c_name VARCHAR(30),
    id INT PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE IF NOT EXISTS accounts (
    id_client INT,
    opening_date DATE,
    money INT,
    FOREIGN KEY (id_client)
        REFERENCES clients (id)
);
        
INSERT INTO clients (c_name) VALUES
("Иванов А.С."), 
("Петров О.Л."), 
("Смирнова Е.П."), 
("Козлова Н.И."), 
("Михайлов К.Д."), 
("Федорова Л.М."), 
("Соколов Г.В."), 
("Новикова Е.А."), 
("Павлов И.В."), 
("Морозов Д.Ю.");

INSERT INTO accounts() VALUES
(3, "2017-11-25", 18000),
(8, "2023-12-31", -5000),
(2, "2021-10-15", 27000),
(5, "2023-12-05", 3500),
(7, "2023-12-18", -12000),
(1, "2021-11-03", 8000),
(6, "2023-12-30", -7000),
(5, "2023-10-22", 42000),
(9, "2017-12-08", -2500),
(10, "2023-12-29", 15000),
(3, "2020-11-25", -10000),
(2, "2023-12-20", 2000),
(8, "2017-10-01", 12000),
(1, "2023-11-10", -8000),
(6, "2023-12-15", 6000);

-- 1.1. показать всех счета и их клиентов (пользователей счетов)
SELECT 
    c_name, money
FROM
    clients,
    accounts
WHERE
    clients.id = accounts.id_client;
    
-- 1.2. Показать всех счета и их клиентов, остаток на счете положительный
SELECT 
    c_name, money
FROM
    clients,
    accounts
WHERE
    clients.id = accounts.id_client and money > 0;

-- 1.3. показать счета открытые за 2017 год и их клиентов
SELECT 
    c_name, opening_date
FROM
    clients,
    accounts
WHERE
    clients.id = accounts.id_client and year(opening_date) = 2017;
    
-- 1.4 Показать всех клиентов у которых нет счетов
SELECT DISTINCT
    c_name
FROM
    clients,
    accounts
WHERE
    clients.id NOT IN (SELECT id_client FROM accounts);
    
-- Спроектировать  бд “Ремонт_авто”
-- необходимо спроектировать таблицы “Записи” и “авто”  (в один слот может быть записано только одно авто)

CREATE TABLE IF NOT EXISTS cars (
    c_name VARCHAR(30),
    release_date DATE,
    id INT PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE IF NOT EXISTS appointments (
    id_car INT,
    app_date DATE,
    FOREIGN KEY (id_car)
        REFERENCES cars (id)
);

INSERT INTO cars (c_name, release_date) VALUES
("Лада", "2017-12-01"),
("BMW", "2018-05-15"),
("Toyota", "2019-02-28"),
("Audi", "2020-09-10"),
("Mercedes-Benz", "2021-03-20"),
("Ford", "2016-11-12"),
("Honda", "2017-08-05"),
("Chevrolet", "2018-07-30"),
("Nissan", "2019-12-18"),
("Hyundai", "2020-06-25");

INSERT INTO appointments() VALUES
(3, "2023-12-06"),
(8, "2023-12-07"),
(2, "2023-12-08"),
(5, "2023-12-09"),
(7, "2023-12-10"),
(1, "2023-12-11"),
(6, "2023-12-12"),
(4, "2023-12-13"),
(9, "2023-12-14"),
(10, "2023-12-15"),
(3, "2023-12-16"),
(2, "2023-12-17"),
(8, "2023-12-18"),
(1, "2023-12-19"),
(6, "2023-12-20");

-- 1.1. показать всех записи и их авто
SELECT 
    c_name, app_date
FROM
    cars,
    appointments
WHERE
    cars.id = id_car;

-- 1.2. Показать всех авто с маркой “lada” и в какие даты они записаны
SELECT 
    c_name, app_date
FROM
    cars,
    appointments
WHERE
    cars.id = id_car and c_name = "Лада";

-- 1.3. Показать всех авто года выпуска 2017 и старше и их записи
SELECT 
    c_name, app_date, release_date
FROM
    cars,
    appointments
WHERE
    cars.id = id_car and year(release_date) <= 2017;

-- 1.4. Показать всех записи за текущий месяц и их авто
SELECT 
    c_name, app_date
FROM
    cars,
    appointments
WHERE
    cars.id = id_car
        and month(app_date) = month(now())
        and year(app_date) = year(now());
        
        
-- Спроектировать бд “школы”
-- необходимо спроектировать таблицы “школа” и “ученики”


CREATE TABLE IF NOT EXISTS schools (
    sc_name VARCHAR(30),
    id INT PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE IF NOT EXISTS students (
    id_school INT,
    st_name VARCHAR(60),
    age INT,
    FOREIGN KEY (id_school)
        REFERENCES schools (id)
);

INSERT INTO schools(sc_name) VALUES
("Первая"),
("Вторая"),
("Третья");

INSERT INTO students() VALUES
(2, "Петров Александр Сергеевич", 12),
(1, "Иванова Елена Николаевна", 9),
(3, "Смирнов Владимир Игоревич", 15),
(2, "Козлова Анна Петровна", 8),
(1, "Соколов Дмитрий Александрович", 11),
(3, "Морозова Ольга Викторовна", 14),
(2, "Новиков Игорь Валентинович", 10),
(1, "Кузнецова Лариса Станиславовна", 13),
(3, "Федоров Артем Владимирович", 7),
(2, "Борисова Татьяна Александровна", 16),
(1, "Иванов Сергей Иванович", 6),
(3, "Лебедев Иван Викторович", 17),
(2, "Павлова Екатерина Андреевна", 8),
(1, "Антонов Андрей Игоревич", 15),
(3, "Григорьева Юлия Дмитриевна", 10);

-- 1.1. показать всех школы и их учеников
SELECT 
    sc_name, st_name
FROM
    students,
    schools
WHERE
    schools.id = id_school;
    
-- 1.2. Показать всех учеников  с фамилией “Иванов” и школы, в которых они учатся
SELECT 
    sc_name, st_name
FROM
    students,
    schools
WHERE
    schools.id = id_school
    and st_name like "Иванов %";

-- 1.3. Показать всех  учеников с именем “Иван” или именем “Лариса” и школы, в которых они учатся
SELECT 
    sc_name, st_name
FROM
    students,
    schools
WHERE
    schools.id = id_school
    and st_name like "% Иван %" 
    or schools.id = id_school
    and st_name like "% Лариса %";
    
-- 1.4. Показать всех учеников в возрасте от 10 до 15 лет включительно и школы, в которых они учатся
SELECT 
    sc_name, st_name, age
FROM
    students,
    schools
WHERE
    schools.id = id_school
    and age >= 10 and age <= 15;
    

-- Спроектировать  бд “отели”
-- необходимо спроектировать таблицы “бронирование” и “пользователи”

CREATE TABLE IF NOT EXISTS clients (
    c_name VARCHAR(30),
    birthday DATE,
    id INT PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE IF NOT EXISTS reservations (
    id_client INT,
    res_date DATE,
    money INT,
    FOREIGN KEY (id_client)
        REFERENCES clients (id));
        
INSERT INTO clients (c_name, birthday) VALUES
("Иванов А.П.", "2000-10-31"),
("Петров Б.И.", "1995-07-15"),
("Смирнов В.С.", "1989-04-22"),
("Козлова Е.М.", "1980-12-05"),
("Морозов Ф.Д.", "1998-08-18"),
("Соколов Г.И.", "1993-03-11"),
("Новиков А.К.", "2005-06-27"),
("Павлова Л.В.", "1987-09-09"),
("Исаев И.С.", "1976-01-14"),
("Антонов Д.А.", "1990-11-26");

INSERT INTO reservations () VALUES
(3, "2023-12-30", 5000),
(8, "2024-01-15", 3200),
(2, "2022-11-20", 4200),
(5, "2024-02-03", 6000),
(7, "2023-12-30", 3500),
(1, "2023-10-31", 4800),
(6, "2024-03-12", 2800),
(4, "2022-11-10", 5300),
(9, "2024-04-27", 7000),
(10, "2023-12-30", 4200),
(3, "2024-01-01", 4600),
(2, "2023-12-05", 3900),
(8, "2024-05-18", 6200),
(1, "2023-11-15", 5000),
(6, "2024-06-08", 5400);

-- 1.1. показать все бронирования и их пользователей
SELECT 
    c_name, res_date
FROM
    reservations,
    clients
WHERE
    clients.id = id_client;

-- 1.2. Показать оказать все бронирования стоимость которых равна 5000 и их пользователей с фамилией Иванов
SELECT 
    c_name, res_date
FROM
    reservations,
    clients
WHERE
    clients.id = id_client
    and c_name like "Иванов %" and money = 5000;

-- 1.3. Показать всех пользователей, у которых их дата заезда совпадает с днем рождения
SELECT 
    c_name, res_date, birthday
FROM
    reservations,
    clients
WHERE
    clients.id = id_client and month(res_date) = month(birthday) and day(res_date) = day(birthday);

-- 1.4. Показать оказать все бронирования и их пользователей за ноябрь 2022 года
SELECT 
    c_name, res_date
FROM
    reservations,
    clients
WHERE
    clients.id = id_client and month(res_date) = 11 and year (res_date) = 2022;