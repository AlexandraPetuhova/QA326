#ЗАДАЧА
#вЫВЕСТИ НА ЭКРАН ФИГУРУ ИЗ ЗВЕЗДОЧЕК:
#*******
#*******
#*******
#*******
#(КВАДРАТ ИЗ N СТРОК, В КАЖДОЙ СТРОКЕ N ЗВЕЗДОЧЕК)
#N - ГАРАНТИРУЕТСЯ, ЧТО ЦЕЛОЕ ЧИСЛО

n = int(input("Введите число "))
if n > 0:
        for element in range (1, n + 1):
            print('*  ' * n)
else:
    print("Число должно быть больше нуля")

#задача
# распечатайте все числа, которые делятся на 3 от start до end(включительно) (start, end - могут быть перепутаны), start , end- гарантируется, что целые числа
start = int(input("Введите первое число "))
end = int(input("Введите второе число "))
if end < start:
    end, start = start, end
for element in range(start, end + 1):
    if element % 3 == 0:
        print(element, end=" ")

#задача
#напишите программу для черепахи, чтобы она рисовала вот так  (кол-во углов произвольное)
#лесенка

from turtle import *
while True:
    try:
        stairs = int(input("Введите количество ступенек "))
        if stairs <= 0:
            print("Число не может быть меньше 0. Попробуйте ещё раз")
        else:
            break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз")
left(180)
while True:
    for line_color in "blue", "red", "black", "yellow":
        if stairs == 0:
            exitonclick()
            break
        color(line_color)
        forward(stairs * 5)
        left(90)
        forward(stairs * 5)
        right(90)
        stairs -= 1

#задача
#напишите программу для черепахи, чтобы она рисовала вот так  (кол-во сторон произвольное)
# квадратная спиралька

from turtle import *
while True:
    try:
        sides = int(input("Введите количество сторон "))
        if sides <= 0:
            print("Число не может быть меньше 0. Попробуйте ещё раз")
        else:
            break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз")
n = 1
while True:
    for line_color in "green", "blue", "red":
        if sides == n - 1:
            exitonclick()
            break
        color(line_color)
        forward(n * 5)
        left(90)
        n += 1



#задача
#напишите программу для черепахи, чтобы она рисовала вот так  (кол-во сторон произвольное)
# заборчик

from turtle import *
while True:
    try:
        count = int(input("Введите длину забора "))
        if count <= 0:
            print("Число не может быть меньше 0. Попробуйте ещё раз")
        else:
            break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз")
while True:
    for line_color in "red", "black", "blue":
        color(line_color)
        forward(30)
        left(90)
        forward(30)
        right(90)
        forward(30)
        right(90)
        forward(30)
        left(90)
        count -= 1
        if count == 0:
            exitonclick()
            break

#задача
#Выведите на экран числа 1.2, 1.4, 1.6, ..., 2.8. Для программы необходимо использовать цикл for

start = float(input("Введите первое число "))
end = float(input("Введите второе число "))
if end < start:
    end, start = start, end
for element in range(int(start * 10 + 0.9), int(end * 10 + 1), 2):
    comma = ", "
    if element >= end * 10 - 1.99:
        comma = "."
    element = float(element) / 10
    print(element, end=comma)

#задача
#Дано:
#n - кол-во сторон (гарантируется, что число целое)
#a - сторона многоугольника
#is_fill - нужно залить фигуру (гарантируется, что будет использован только логический тип данных)
#нарисовать ПРАВИЛЬНЫЙ многоугольник по заданным характеристикам
#УСЛОЖНЕНИЕ(необязательно делать) (добавьте еще одну переменную, хочет ли пользователь, чтобы каждая сторона многоугольника была разного цвета)
from turtle import *
import random
while True:
    try:
        n = int(input("Введите количество сторон "))
        if n <= 2:
            print("Число не может быть меньше 3. Попробуйте ещё раз")
        else:
            break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз")
while True:
    try:
        a = int(input("Введите длину одной стороны "))
        if a <= 2:
            print("Число не может быть меньше 0. Попробуйте ещё раз")
        else:
            break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз")

while True:
    try:
        is_fill = bool(int(input("Нужна ли заливка? 1 - Да, 0 - Нет ")))
        break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз")
while True:
    try:
        is_diff_colors = bool(int(input("Сделать стороны разных цветов? 1 - Да, 0 - Нет ")))
        break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз")
pensize(3)
if is_fill:
    begin_fill()
for i in range(n):
    if is_diff_colors:
        line_colors = random.choice(['red', 'magenta', 'MediumOrchid', 'BlueViolet', 'blue', 'DodgerBlue', 'DarkTurquoise', 'lime green', 'GreenYellow', 'yellow', 'Gold', 'DarkOrange'])
    else:
        line_colors = ('black')
    pencolor(line_colors)
    forward(a)
    left(360 / n)
if is_fill:
    end_fill()
exitonclick()