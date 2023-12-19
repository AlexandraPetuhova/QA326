CREATE DATABASE homework;
USE homework;
-- Есть бд “школа”
-- необходимо спроектировать таблицы “Предмет” и “Преподаватели”

CREATE TABLE IF NOT EXISTS teachers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    t_name VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS classes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    c_name VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS teachers_classes (
    id_teacher INT NOT NULL,
    id_class INT NOT NULL,
    FOREIGN KEY (id_teacher)
        REFERENCES teachers (id),
    FOREIGN KEY (id_class)
        REFERENCES classes (id)
);

INSERT INTO teachers (t_name) VALUES
("Анна Иванова"), ("Иван Петров"), 
("Мария Смирнова"), ("Алексей Козлов"), 
("Екатерина Мороз"), ("Дмитрий Павлов"), 
("Ольга Николаева"), ("Павел Соколов"), 
("Наталья Иванова"), ("Михаил Семенов");

INSERT INTO classes (c_name) VALUES
("Русский Язык"), ("Литература"), 
("Математика"), ("История"), 
("Иностранный Язык"), ("Физика"), 
("Химия"), ("Биология"), ("ОБЖ"), 
("Обществознание"), ("География"), 
("Физкультура"), ("Информатика");

INSERT INTO teachers_classes VALUES
(1, 1), (5, 9), (2, 7),
(8, 12), (3, 5), (10, 8),
(1, 13), (6, 4), (9, 11),
(4, 6), (7, 2), (7, 3);

-- все предметы и преподаватели
SELECT 
    c_name, t_name
FROM
    teachers,
    classes,
    teachers_classes
WHERE
    teachers.id = teachers_classes.id_teacher
        AND classes.id = teachers_classes.id_class;
        
-- выбрать всех преподавателей, которые ведут историю
SELECT 
    t_name
FROM
    teachers,
    classes,
    teachers_classes
WHERE
    teachers.id = teachers_classes.id_teacher
        AND classes.id = teachers_classes.id_class
        AND c_name = 'История';

-- выбрать все предметы, начинающиеся на "И"
SELECT 
    c_name
FROM
    classes
WHERE
    c_name LIKE 'И%';

-- выбрать все предметы, которые ведёт Ольга Николаева
SELECT 
    c_name
FROM
    teachers,
    classes,
    teachers_classes
WHERE
    teachers.id = teachers_classes.id_teacher
        AND classes.id = teachers_classes.id_class
        AND teachers.t_name = 'Ольга Николаева';



-- Есть бд “МАГАЗИН”
-- необходимо спроектировать таблицы “ПОСТАВЩИКИ” и “ТОВАРЫ”

CREATE TABLE IF NOT EXISTS goods (
    id INT PRIMARY KEY AUTO_INCREMENT,
    g_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS suppliers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    s_name VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS goods_suppl (
    id_suppliers INT NOT NULL,
    id_goods INT NOT NULL,
    FOREIGN KEY (id_suppliers)
        REFERENCES suppliers (id),
    FOREIGN KEY (id_goods)
        REFERENCES goods (id)
);

INSERT INTO suppliers (s_name) VALUES
("Глобальные Электроники Inc."), 
("ТехноПродукт ООО"), 
("Мировые Инновации Ltd."), 
("ЭкоСервис Поставки Групп"), 
("ПромТехМагазин LLC"), 
("Индустриальные Решения Corp."), 
("ЭлитСтройМатериалы Ltd."), 
("Гармония Продуктов и Услуг"), 
("ЭкоТехника Россия ОАО"), 
("Мега-Транспортные Поставки LLC");

INSERT INTO goods (g_name) VALUES
("Ноутбук HP Spectre x360"), 
("Смартфон iPhone 13 Pro"), 
("4K телевизор Samsung QLED"), 
("Фотоаппарат Canon EOS R5"), 
("Наушники Sony WH-1000XM4"), 
("Электрический чайник Bosch TWK7203"), 
("Кофемашина De'Longhi Magnifica"), 
("Спортивные кроссовки Nike Air Max 270"), 
("Стиральная машина LG Inverter Direct Drive"), 
("Смарт-часы Apple Watch Series 7"), 
("Акустическая гитара Yamaha FG800"), 
("Умный домашний хаб Google Nest Hub"), 
("Робот-пылесос iRobot Roomba 980");


INSERT INTO goods_suppl VALUES
(1, 1), (5, 9), (2, 7),
(8, 12), (3, 5), (10, 8),
(1, 13), (6, 4), (9, 11),
(4, 6), (7, 2), (7, 3);

-- все товары и поставщики
SELECT 
    s_name, g_name
FROM
    goods,
    suppliers,
    goods_suppl
WHERE
    suppliers.id = goods_suppl.id_suppliers
        AND goods.id = goods_suppl.id_goods;
        
-- выбрать всех поставщиков, начинающихся на "Э", и их товары
SELECT 
    s_name, g_name
FROM
    goods,
    suppliers,
    goods_suppl
WHERE
    suppliers.id = goods_suppl.id_suppliers
        AND goods.id = goods_suppl.id_goods
        AND s_name LIKE 'Э%';

-- выбрать всех поставщиков наушников
SELECT 
    s_name, g_name
FROM
    goods,
    suppliers,
    goods_suppl
WHERE
    suppliers.id = goods_suppl.id_suppliers
        AND goods.id = goods_suppl.id_goods
        AND g_name LIKE 'Наушник%';



-- Есть бд “КИНОТЕАТР”
-- необходимо спроектировать таблицы “ФИЛЬМЫ” и “ЗАЛ”


CREATE TABLE IF NOT EXISTS halls (
    id INT PRIMARY KEY AUTO_INCREMENT,
    h_name VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS movies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    m_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS halls_movies (
    id_halls INT NOT NULL,
    id_movies INT NOT NULL,
    FOREIGN KEY (id_halls)
        REFERENCES halls (id),
    FOREIGN KEY (id_movies)
        REFERENCES movies (id)
);

INSERT INTO halls (h_name) VALUES
("Кинозвезда"), 
("Мегаплекс"), 
("Артхаус");

INSERT INTO movies (m_name) VALUES
("Матрица: Воскрешение"), 
("Отряд самоубийц 2: Миссия навылет"), 
("Дюна"), 
("007: Не время умирать"), 
("Чёрная вдова"), 
("Главный герой"), 
("Лига справедливости Зака Снайдера"), 
("Круэлла"), 
("Смерть на Ниле"), 
("Вечные");


INSERT INTO halls_movies VALUES
(1, 1), (1, 9), (2, 7),
(2, 2), (3, 5), (1, 8),
(1, 3), (3, 4), (2, 10),
(3, 6), (2, 5), (2, 8);

-- все залы и фильмы
SELECT 
    h_name, m_name
FROM
    movies,
    halls,
    halls_movies
WHERE
    halls.id = halls_movies.id_halls
        AND movies.id = halls_movies.id_movies;

-- выбрать все фильмы второго зала
SELECT 
    m_name
FROM
    movies,
    halls_movies
WHERE
    movies.id = halls_movies.id_movies
        AND id_halls = 2;

-- Есть бд “ИГРА ФЕРМА”
-- необходимо спроектировать таблицы “ОГОРОД” и “ПРОДУКТ”(который будут выращивать в огороде)

CREATE TABLE IF NOT EXISTS product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    p_name VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS garden (
    id INT PRIMARY KEY AUTO_INCREMENT,
    g_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS product_garden (
    id_garden INT NOT NULL,
    id_product INT NOT NULL,
    FOREIGN KEY (id_garden)
        REFERENCES garden (id),
    FOREIGN KEY (id_product)
        REFERENCES product (id)
);

INSERT INTO product (p_name) VALUES
("Картошка"), 
("Капуста"), 
("Помидоры"), 
("Огурцы"), 
("Арбузы"), 
("Редиска"), 
("Морковка"), 
("Клубника"), 
("Земляника"), 
("Брокколи");

INSERT INTO garden (g_name) VALUES
("Огород 1"), 
("Огород 2"), 
("Теплица");

INSERT INTO product_garden VALUES
(1, 1), (1, 9), (2, 7),
(2, 2), (3, 5), (1, 8),
(1, 3), (3, 4), (2, 10),
(3, 6), (2, 5), (2, 8);

-- все овощи и фрукты
SELECT 
    g_name, p_name
FROM
    garden,
    product,
    product_garden
WHERE
    product.id = product_garden.id_product
        AND garden.id = product_garden.id_garden;

-- выбрать всё что растёт в теплице
SELECT 
    p_name
FROM
    product,
    product_garden
WHERE
    product.id = product_garden.id_product
        AND id_garden = 3;