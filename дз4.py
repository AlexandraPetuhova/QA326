# задача 1
# даны 3 числа, распечатать в порядке возрастания

x = int(input('Введите число '))
y = int(input('Введите число '))
z = int(input('Введите число '))
if x <= y and x <= z:
    if y <= z:
        print(x, y, z)
    else:
        print(x, z, y)
elif y <= x and y <= z:
    if x <= z:
        print(y, x, z)
    else:
        print(y, z, x)
elif z <= y and z <= x:
    if y <= x:
        print(z, y, x)
    else:
        print(z, x, y)

# задача 2
# Написать программу для следующей задачи
# работают 3 сотрудника, у них есть оклад в размере 300.
# Если сотрудник выполнит 50 и более продаж, то получит премию в размере 30% от оклада, если более 75, то получит премию в размере 65% от оклада, а если 100, то - 100% от оклада

salary = 300
bonus = int(input('Сколько продаж у сотрудника? '))
if bonus >= 100:
    salary = salary * 2
elif bonus >= 75:
    salary = salary / 100 * 65 + salary
elif bonus >= 50:
    salary = salary / 100 * 30 + salary
print(f'В этом месяце сотрудник получит {salary}')


# задача 3
# Игра камень ножницы бумага с компьютером
# (камень побеждает ножницы / ножницы побеждает бумагу / бумага побеждает камень)
# Игрок делает ход и затем компьютер делает ход
# Вывести кто победил.

import random
person = input('Введите свой ответ ').lower()
choice = ["камень", "ножницы", "бумага"]
computer = random.choice(choice)
print(f'Выбор компьютера: {computer}')
if person == "камень" or person == "ножницы" or person == "бумага":
    if person == computer:
        print('Ничья')
    else:
        if person == "камень" and computer == "бумага":
            print("Компьютер победил")
        elif person == "ножницы" and computer == "камень":
            print("Компьютер победил")
        elif person == "бумага" and computer == "ножницы":
            print("Компьютер победил")
        else:
            print("Человек победил")

# задача 4
# Пользователь с клавиатуры вводит количество часов.
# Если полученное значение находится в диапазоне от 0 до 5 нужно вывести надпись Good Night, если в диапазоне от 6 до 13 Good Morning, если в диапазоне от 13 до 17 Good Day, если в диапазоне от 17 до 0 Good Evening.

hour_count = int(input('Введите время '))
if hour_count >= 0 and hour_count <= 5:
    print('Good Night')
elif hour_count >= 6 and hour_count <= 13:
    print('Good Morning')
elif hour_count > 13 and hour_count <= 17:
    print('Good Day')
elif hour_count > 17 and hour_count < 0:
    print('Good Evening')
else:
    print('Время введено некорректно')

# ДОПОЛНИТЕЛЬНЫЕ ЗАДАЧИ
# задача 1
# даны 4 числа
# найти числа, которые не повторяются (set  использовать нельзя)

a = input('Введите число ')
b = input('Введите число ')
c = input('Введите число ')
d = input('Введите число ')
print(a)
if a != b:
    print(b)
if a != c and b != c:
    print(c)
if d != a and d != b and d != c:
    print(d)

# задача 2
# определить является ли год високосным

year = int(input('Введите год '))
if year > 1000 and year < 3000:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Год високосный')
    else:
        print('Год не високосный')
else:
    print("Данные введены неверно")