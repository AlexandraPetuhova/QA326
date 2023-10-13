#задача
## распечатайте все числа (должны быть только положительные), которые делятся на 3 без остатка от start до end(включительно) (start, end - могут быть перепутаны), start , end- гарантируется, что целые числа
#Найти в этом списке самое маленькое число, которое делится на три без остатка

start = int(input("Введите первое число "))
end = int(input("Введите второе число "))

if start > 0 and end > 0:
    if end < start:
        end, start = start, end
    x = True
    for element in range(start, end + 1):
        if element % 3 == 0:
            if x:
                print(f"Самое маленькое число, кратное трём, это {element} \nОстальные кратные трём:")
                x = False
            print(element, end=" ")
else:
    print("Допускаются только положительные числа")

#задача
#(квадрат из n строк, в каждой строке n звездочек)
#n - гарантируется, что целое число
#
#Вывести на экран фигуру n*n (только для нечетного n) из звездочек:
#*   .   *   .   *
#.   *   *   *   .
#*   *   *   *   *
#.   *   *   *   .
#*   .   *   .   *

n = int(input("Введите размер звёздочки "))
if n > 0 and n % 2 == 1:
    for element in range(1, n + 1):
        center = int((n - 1) / 2 + 1)
        if element == center:
            print(" * " * n)
            continue
        elif element < center:
            n1 = center - 1 - (center - element)
            n2 = center - element
        elif center < element:
            n1 = n - element
            n2 = center - 1 - (n - element)
        print(f"{'   ' * n1}*{'   ' * n2}*{'   ' * n2}*{'   ' * n1}")
elif n <= 0:
    print("Допускаются только положительные числа")
elif n % 2 != 1:
    print("Число должно быть нечётным")
else:
    print("Введены недопустимые данные")


#задача
#Дан список элементов 1, 3, 22, 7, 12, 8, 2 (могут быть какие-то другие значения, ввод данных делать не нужно)
#1. показать каждый элемент, последняя цифра которого 2
#2. показать произведение чисел, последняя цифра которого 2


elements_list = 1, 3, 22, 7, 12, 8, 2
x = 1
for elements in elements_list:
    if elements % 10 == 2:
        x = x * elements
        print(elements, end=" ")
print(f"\nПроизведение чисел, последняя цифра которого 2, равно {x}")



#задача
#Игра угадай число от 1 до 100
#реализовать подсказки (число введенное больше или меньше)
#сделать проверку на ввод числа для пользователя (может быть абсолютно любой символ)
import random
computer = random.randint(1, 100)
for i in range(7):
    try:
        person = int(input("Введите число "))
        if person < 0:
            print("Число не может быть меньше 0")
            continue
        elif person == computer:
            print("Угадали!")
            break
        elif computer < person:
            print("Меньше")
            continue
        else:
            print("Больше")
            continue
    except ValueError:
        print("Неверные данные")
        continue
if person != computer:
    print("Попытки закончились")




#задача
#для черепахи
#цветной пунктир

from turtle import *
while True:
    for line_color in "blue", "red", "black":
        color(line_color)
        forward(30)
        penup()
        forward(5)
        pendown()
