#задача
#Дана произвольная строка
#Написать регулярное выражение для поиска в строке серии и номера паспорта
#Допускается только запись паспорта из предложенных ниже :
#00 00 000000
#или 00 00 000 000
#или 00-00-000-000
#или 00-00-000000
#на месте 0 может стоять любая цифра
#Программа должны вывести кол-во валидных значений и показать их в консоле

import re
# test_string = """00 00 000000
# или 00 00 000 000
# или 00-00-000-000
# или 00-00-000000
# или 080 00 00 000
# или 00*00*000*000
# или 00-00-00-0000
# """
test_string = input("Введите произвольную строку ")
reg_ex = r"\d{2}[ -]\d{2}[ -]\d{3}[ -]{0,1}\d{3}"
result = re.findall(reg_ex, test_string)
print(f"\nНайдено совпадений: {len(result)}")
if len(result):
    print("Результаты: ", end="")
    print(*result, sep=", ")


#задача
#Дана строка с произвольная строка
#написать регулярное выражение для определения номера автомобиля.
#Допускается только такая запись номера автомобиля А000АА
#А-любая буква(латиница)
#0-любая цифра
#Программа должны вывести кол-во валидных значений и показать их в консоле


import re
test_string = input("Введите произвольную строку ")
reg_ex = r"[A-Z]\d{3}[A-Z]{2}"
result = re.findall(reg_ex, test_string)
print(f"\nНайдено совпадений: {len(result)}")
if len(result):
    print("Результаты: ", end="")
    print(*result, sep=", ")

#задача
#Написать регулярное выражение для определения валидных логинов.
#Валидными считаются те логины, которые удовлетворяют следующим условиям:
#содержится минимум 1 букву латинского алфавита и не содержится буквы других алфавитов
#содержит  минимум 2 цифры
#в конце имени обязательно нужно указывать “login”
#примеры валидных значений
#	n12login
#	name22login
#	2name2login
#и т.д.


import re
test_string = input("Введите произвольную строку ")
# test_string = """n1j2glogin
# nKe22login
# 2name2login
# 2name2logini
# n1login
# 22login
# 2nЛeЮ2login
# """
reg_ex = r"(?=\w*\d)(?=\w*\d)(?=\w*[a-z]){1,}\w+login\b"
result = re.findall(reg_ex, test_string)
final_result = result.copy()
for i in result:
    if len(re.findall(r"\d", i)) < 2 or len(re.findall(r"[a-z]", i)) < 6 or len(re.findall(r"[А-Яа-я\W]", i)) > 0:
        final_result.remove(i)
print(f"\nНайдено совпадений: {len(final_result)}")
if len(final_result):
    print("Результаты: ", end="")
    print(*final_result, sep=", ")


#задача
#используя модуль turtle и создав функцию рисования квадрата, решите следующую задачу:
#сеточка

from turtle import *
num = int(input("Какой размер сетки? "))
speed(20)
def draw_square():
    for i in range(4):
        forward(50)
        left(90)
for i in range(num):
    for j in range(num):
        draw_square()
        forward(50)
    left(180)
    forward(num * 50)
    if i != num-1:
        left(90)
        forward(50)
        left(90)
exitonclick()

#задача
#создать функцию для генерации списка случайными числами

from random import randint
def create_random_list():
    list = []
    for i in range(randint(-100, 100)):
        list.append(randint(-100, 100))
    return list

print(create_random_list())

#задача
#используя модуль turtle и создав функцию рисования квадрата, решите следующую задачу:
#все треугольники одинакового размера. Для треугольника можно использовать функцию из классной работы.

from turtle import *
def draw_triangle():
    for i in range(3):
        forward(100)
        left(120)
    forward(100)
num = int(input("Сколько сторон? "))
for i in range(num):
    draw_triangle()
    right(360 / num)
exitonclick()


#задача
#используя модуль turtle и создав функцию рисования шестиугольника, решите следующую задачу:

from turtle import *
def draw_hexagone():
    for i in range(6):
        forward(50)
        left(60)
draw_hexagone()
forward(100)
draw_hexagone()
left(180)
draw_hexagone()