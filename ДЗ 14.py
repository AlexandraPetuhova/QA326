# задача
# написать функцию is_positive(num), которая возвращает True в случае, если num положительное, и False во всех остальных случаях.
# Дан список чисел (только целые числа).
# Напечатать 0 и отрицательные числа в списке применив, функцию is_positive

from random import randint

list = [0]
for i in range(randint(1, 100)):
    list.append(randint(-100, 100))
print(list)
def is_positive(num):
    if type(num) == int and num > 0:
        return True
    else:
        return False

print("0 и отрицательные числа в списке: ", end="")
for num in list:
    if not is_positive(num):
        print(num, end=" ")


# задача
# написать функцию num_to_name_week(num_day_week), которая возвращает имя дня недели(строка)
# ПРимер
# num_to_name_week(1) -> ‘Понедельник’


def num_to_name_week(num_day_week):
    try:
        num_day_week = int(num_day_week)
    except ValueError:
        num = 0
    match num_day_week:
        case 1:
            return "Понедельник"
        case 2:
            return "Вторник"
        case 3:
            return "Среда"
        case 4:
            return "Четверг"
        case 5:
            return "Пятница"
        case 6:
            return "Суббота"
        case 7:
            return "Воскресенье"
        case _:
            return "День недели не обнаружен"

day = input("Введите номер дня недели ")
print(num_to_name_week(day))


# задача
# написать функцию для вычисления периметра n-угольника(проверку на существование фигуры прописать отдельную(ые) функцию(и)), применить эту функцию(и) для вычисления периметра n-угольника

def if_exist(figure):
    if len(figure) < 3:
        return False
    for side in figure:
        figure2 = figure.copy()
        figure2.remove(side)
        try:
            if side >= sum(figure2) or side <= 0:
                return False
        except TypeError:
            return False
    return True
def list_to_int(something):
    smt2 = []
    for element in something:
        smt2.append(int(element))
    return smt2

sides = input("Введите стороны многоугольника через пробел ")
sides = sides.split()
sides = list_to_int(sides)
if if_exist(sides):
    match len(sides):
        case 3:
            word = "тре"
        case 4:
            word = "четырёх"
        case 5:
            word = "пяти"
        case 6:
            word = "шести"
        case 7:
            word = "семи"
        case 8:
            word = "восьми"
        case 9:
            word = "девяти"
        case _:
            word = "много"
    print(f"Периметр {word}угольника равен {sum(sides)}")
else:
    print("Периметр не найден")

# задача
# написать функцию для фигуры как на картинке.
# и решить задачу с применением этой функции
калейдоскоп

from turtle import *
def draw_blue():
    pencolor("blue")
    forward(50)
    left(36)
    forward(50)
    left(144)
    forward(50)
    left(180)
    forward(50)
    left(72)
    forward(50)
    left(108)
    forward(50)
    left(180)
    forward(50)
    left(108)
    forward(50)
    left(72)
    forward(50)
    penup()
    goto(0, 0)
    right(180)
    pendown()

def draw_red():
    pencolor("red")
    forward(100)
    left(72)
    forward(100)
    left(108)
    forward(100)
    left(180)
    forward(100)
    left(144)
    forward(100)
    penup()
    goto(0, 0)
    right(144)
    pendown()

speed(20)
pensize(2)
hideturtle()
for i in range(10):
    draw_blue()
    draw_red()
    left(36)
exitonclick()

# задача
# написать ОДНУ функцию для фигур как на картинке.
# и решить задачу с применением этой функции. порядок фигур не важен. Также должна быть возможность задавать произвольный размер и цвет через функцию

from turtle import *


def draw_figure(size, angles, colorr):
    hideturtle()
    color(colorr)
    begin_fill()
    for side in range(angles):
        forward(size)
        left(360 / angles)
    end_fill()
    exitonclick()

angles = int(input("Сколько углов? "))
colorr = input("Какой цвет? ")
size = int(input("Размер фигуры? "))

draw_figure(size, angles, colorr)

# Творческое задание
# Можно решить задачу как одной функцией, так и двумя и более. Главное, чтобы получился результат как на картинке. Функция должна принимать произвольный размер снежинки, произвольное кол-во сегментов  и произвольный цвет
# снежинка

from turtle import *
def draw_snowflake(size, spikes_num, snow_color):
    color(snow_color)
    pensize(2)
    hideturtle()
    for spike in range(spikes_num):
        forward(size)
        speed(-1)
        left(45)
        forward(size // 3)
        left(180)
        forward(size // 3)
        left(135)
        forward(size // 3)
        left(180)
        forward(size // 3)
        left(135)
        forward(size // 3)
        speed(6)
        penup()
        left(45)
        goto(0, 0)
        pendown()
        left(360 / spikes_num)

spikes = int(input("Сколько сегментов? "))
snow_color = input("Какой цвет? ")
size = int(input("Размер снежинки? "))
draw_snowflake(size, spikes, snow_color)
exitonclick()


# задача
# доделать задачу ниже, чтобы код соответствовал заявленным требования
# генератор даты

import random
def create_date():
    year = random.randint(1000, 9999)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days_in_month = {2: 29, 1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, 4: 30, 6: 30, 9: 30, 11: 30}
    else:
        days_in_month = {2: 28, 1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, 4: 30, 6: 30, 9: 30, 11: 30}
    month = random.randint(1, 12)
    day = random.randint(1, days_in_month[month])
    sep = random.choice(['/', '.'])
    return str(day) + sep + str(month) + sep + str(year)
print(create_date())