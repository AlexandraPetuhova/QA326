# задача
# Дана пицца 8 кусочков. Доступны команды:
# 1. print(‘Взять кусок’)
# 2. print(‘съесть кусок’)
# написать программу, симулующую поедание кусочков пиццы (По желанию можно анимацию убывание кусочков пиццы добавить)

pizza = 8
while pizza > 0:
    print('Взять кусок')
    print('съесть кусок')
    pizza -= 1
    print("Кусков осталось:", end = " ")
    y = u"\U0001F355"
    print(y * pizza)

# задача
# Выведите столбец чисел от 1 до 100, используя цикл while

n = 1
while n <= 100:
    print(n)
    n += 1


# задача
# Дано число n. Вывести степени этого числа с 1 по 10
# пример
# n=2
# 2^1=2
# 2^2=4
# …
# 2^9=512
# 2^10 = 1024

n = int(input("Введите число "))
i = 1
while i <= 10:
    print(n, "^", i, "=", n**i)
    i += 1

# задача
# написать программу для черепашки (звёздочка)

from turtle import *
i = 1
while i <= 11:
    i += 1
    forward(300)
    left(180 / 11 + 180)


# задача
# написать программу для черепашки (квадраты в рекурсии)

from turtle import *
i = 1
while i <= 11:
    for u in range(4):
        forward(i * 30 + 50)
        left(90)
    penup()
    right(90)
    forward(15)
    right(90)
    forward(15)
    right(180)
    pendown()
    i += 1


# задача
# Дана пицца 16 кусочков. Доступны команды:
# 1.print(‘Взять кусок’)
# 2. print(‘съесть кусок’)
# 3. print(‘положить кусок обратно’)
# написать программу, симулующую поедание кусочков пиццы, в программе обязательно должно присутствовать команда №3 два раза. Проверять условием, если пиццы в руках нет.

pizza = 16
hands = 2
print("""Что будем делать с пиццой?
Чтобы взять кусок пиццы, нажмите 1
Чтобы положить кусок на место, нажмите 2
Чтобы съесть кусок пиццы, нажмите 3
""")
image = u"\U0001F355"
while pizza > 0:
    action = input()
    match(action):
        case "1":
            if hands == 0:
                print("У вас больше нет рук!")
            else:
                hands -= 1
        case "2":
            if hands == 2:
                print("Сначала возьмите пиццу")
            else:
                hands += 1
        case "3":
            if hands == 2:
                print("Сначала возьмите пиццу")
            else:
                hands += 1
                pizza -= 1
                if pizza != 0:
                    print(f"Пиццы осталость: {image * pizza}")
                else:
                    print("Пицца закончилась :( ")
        case _:
            print("Вы проиграли")




# задача
# Выведите столбец чисел от start (определяется пользователем) до end, используя цикл while. Найти произведение чисел

start = int(input('С какого числа начать? '))
end = int(input("На каком закончить? "))
num_list = [start]
if start <= end:
    while start < end:
        print(start, end=', ')
        start += 1
        num_list.insert(1, start)
    print(end)
elif start > end:
    while start > end:
        print(start, end=', ')
        start -= 1
        num_list.insert(1, start)
    print(end)
import math

print(f'Произведение всех чисел равно {math.prod(num_list)}')

# Черепашка Инь-Ян

from turtle import *
penup()
setpos(0,200)
pendown()
fillcolor("black")
begin_fill()
circle(-90, 180)
circle(90, 180)
circle(180, 180)
end_fill()
circle(180, 180)
penup()
setpos(0,100)
pendown()
begin_fill()
circle(20,)
end_fill()
fillcolor("white")
penup()
setpos(0,-100)
pendown()
begin_fill()
circle(20,)
end_fill()
import time
time.sleep(5)
