# ЗАДАЧА
# Дано:
# ●	3 стороны треугольника
# Проверить существует ли треугольник

a = int(input("Введите первую сторону треугольника "))
b = int(input("Введите вторую сторону треугольника "))
c = int(input("Введите третью сторону треугольника "))
if a > 0 and b > 0 and c > 0 and a < b + c and b < a + c and c < a + b:
    print("Такой треугольник существует")
else:
    print("Такого треугольника не существует")

# ЗАДАЧА
# Дано:
# ●	из чего переводим: часов, минут, секунд (что-то одно на выбор пользователя)
# ●	во что переводим: часов, минут, секунд (что-то одно на выбор пользователя)
# ●	кол-во переводимых единиц
# реализовать интерфейс для перевода из (часов, минут, секунд) в (часов, минут, секунд)

from_what = input("Из чего переводим: часы, минуты, секунды? ")
to_what = input("Во что переводим: часы, минуты, секунды? ")
count = int(input("Сколько? "))
match from_what:
    case "часы":
        if count % 10 == 2 or count % 10 == 3 or count % 10 == 4 and count // 10 != 1:
            russian = "часа"
        elif count % 10 == 1 and count // 10 != 1:
            russian = "час"
        else:
            russian = "часов"
        match to_what:
            case "часы":
                answer = count
                if answer % 10 == 2 or answer % 10 == 3 or answer % 10 == 4 and answer // 10 != 1:
                    russian2 = "часа"
                elif answer % 10 == 1 and answer // 10 != 1:
                    russian2 = "час"
                else:
                    russian2 = "часов"
                print(f"{count} {russian} это {answer} {russian2}", "Зачем вы переводите часы в часы?", sep='\n')
            case "минуты":
                answer = count * 60
                if answer % 10 == 2 or answer % 10 == 3 or answer % 10 == 4 and answer // 10 != 1:
                    russian2 = "минуты"
                elif answer % 10 == 1 and answer // 10 != 1:
                    russian2 = "минута"
                else:
                    russian2 = "минут"
                print(f"{count} {russian} это {answer} {russian2}.")
            case "секунды":
                answer = count * 60 * 60
                if answer % 10 == 2 or answer % 10 == 3 or answer % 10 == 4 and answer // 10 != 1:
                    russian2 = "секунды"
                elif answer % 10 == 1 and answer // 10 != 1:
                    russian2 = "секунда"
                else:
                    russian2 = "секунд"
                print(f"{count} {russian} это {answer} {russian2}.")
            case _:
                print("Вы ввели неправильное значение")
    case "минуты":
        if count % 10 == 2 or count % 10 == 3 or count % 10 == 4 and count // 10 != 1:
                russian = "минуты"
        elif count % 10 == 1 and count // 10 != 1:
                russian = "минута"
        else:
                russian = "минут"
        match to_what:
            case "часы":
                answer = count / 60
                if answer % 10 == 2 or answer % 10 == 3 or answer % 10 == 4 and answer // 10 != 1:
                    russian2 = "часа"
                    answer = int(answer)
                elif answer % 10 == 1 and answer // 10 != 1:
                    russian2 = "час"
                    answer = int(answer)
                else:
                    russian2 = "часов"
                print(f"{count} {russian} это {answer} {russian2}")
            case "минуты":
                answer = count
                if answer % 10 == 2 or answer % 10 == 3 or answer % 10 == 4 and answer // 10 != 1:
                    russian2 = "минуты"
                elif answer % 10 == 1 and answer // 10 != 1:
                    russian2 = "минута"
                else:
                    russian2 = "минут"
                print(f"{count} {russian} это {answer} {russian2}.", "Зачем вы переводите минуты в минуты?", sep='\n')
            case "секунды":
                answer = count * 60
                if answer % 10 == 2 or answer % 10 == 3 or answer % 10 == 4 and answer // 10 != 1:
                    russian2 = "секунды"
                elif answer % 10 == 1 and answer // 10 != 1:
                    russian2 = "секунда"
                else:
                    russian2 = "секунд"
                print(f"{count} {russian} это {answer} {russian2}.")
            case _:
                print("Вы ввели неправильное значение")
    case "секунды":
        if count % 10 == 2 or count % 10 == 3 or count % 10 == 4 and count // 10 != 1:
            russian = "секунды"
        elif count % 10 == 1 and count // 10 != 1:
            russian = "секунда"
        else:
            russian = "секунд"
        match to_what:
            case "часы":
                answer = count / 60 / 60
                if answer % 10 == 2 or answer % 10 == 3 or answer % 10 == 4 and answer // 10 != 1:
                    russian2 = "часа"
                    answer = int(answer)
                elif answer % 10 == 1 and answer // 10 != 1:
                    russian2 = "час"
                    answer = int(answer)
                else:
                    russian2 = "часов"
                print(f"{count} {russian} это {answer} {russian2}")
            case "минуты":
                answer = count / 60
                if answer % 10 == 2 or answer % 10 == 3 or answer % 10 == 4 and answer // 10 != 1:
                    russian2 = "минуты"
                    answer = int(answer)
                elif answer % 10 == 1 and answer // 10 != 1:
                    russian2 = "минута"
                    answer = int(answer)
                else:
                    russian2 = "минут"
                print(f"{count} {russian} это {answer} {russian2}.")
            case "секунды":
                answer = count
                if answer % 10 == 2 or answer % 10 == 3 or answer % 10 == 4 and answer // 10 != 1:
                    russian2 = "секунды"
                elif answer % 10 == 1 and answer // 10 != 1:
                    russian2 = "секунда"
                else:
                    russian2 = "секунд"
                print(f"{count} {russian} это {answer} {russian2}.", "Зачем вы переводите секунды в секунды?", sep='\n')
            case _:
                print("Вы ввели неправильное значение")
    case _:
        print("Вы ввели неправильное значение")

# ЗАДАЧА
# дорешать задачу используя конструкции match case
# код: https://github.com/makarova1507ana/qa_326/blob/main/%D0%B4%D0%BB%D1%8F%20%D0%B4%D0%B7%20%D1%84%D0%B0%D0%B9%D0%BB%D1%8B/match_case.py
#-------------------------ЗАДАЧА-----------------------------#
# Перевод Из мм в м, из м в км (и наоборот)

start = input("Из чего переводим? ")
end = input("Во что переводим? ")
l = int(input("Сколько? "))
if l >= 0:
    match start:
        case 'm':
            match end:
                case 'mm':
                    print(l * 1000)
                case 'km':
                    print(l / 1000)
                case _:
                    print("Неверное значение")
        case 'mm':
            match end:
                case 'm':
                    print(l / 1000)
                case 'km':
                    print(l / 1000000)
                case _:
                    print("Неверное значение")
        case 'km':
            match end:
                case 'm':
                    print(l * 1000)
                case 'mm':
                    print(l * 1000000)
                case _:
                    print("Неверное значение")
        case _:
            print("Неверное значение")
else:
    print("Расстояние не может быть отрицательным")
#
# ЗАДАЧА
# Найти ошибки в решении, записать их. Приложить “код до” и  “код после” с указанием что было исправлено
# код:
# https://github.com/makarova1507ana/qa_326/blob/main/%D0%B4%D0%BB%D1%8F%20%D0%B4%D0%B7%20%D1%84%D0%B0%D0%B9%D0%BB%D1%8B/search_mistake.py
#-------------------------ЗАДАЧА ПОИСК ОШИБОК-----------------------------#
# калькулятор
# доступны операции умножить и поделить
#Код ДО:
#
num1 = 5
operation = '*'
num2 = 6
if operation == '*':
    print(num1/num2) #не тот знак
if operation == '/': #нужен elif
    print(num1/num2)
else:
    print("нет такой операции")

#Код После:

num1 = int(input("Введите первое число "))
num2 = int(input("Введите второе число "))
operation = input("Какая операция (* или /)? ")
if operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print("нет такой операции")

# ЗАДАЧА
# Топливо и черепаха
# черепахе выдается какое-то кол-во чернил, а также фигуру, которая она должна нарисовать (круг или квадрат), а также площадь фигуры
# Определите, хватит ли черепахе чернил
# Если чернил не хватает попросите пользователя дозаправить ее чернила

from turtle import *
import random
fuel = int(input("Заправте черепаху "))
col = ['black', 'red', 'purple', 'orange', 'green', 'pink', 'yellow', 'blue']
proceed = True
while proceed:
    figure = input("Какую фигуру будем рисовать? ").lower()
    size = int(input("Какого размера фигура? "))
    match(figure):
        case "квадрат":
            color(random.choice(col))
            if fuel >= size * size:
                begin_fill()
                for i in range(4):
                    forward(size)
                    right(90)
                end_fill()
                penup()
                x = random.randint(10, 360)
                right(x)
                forward(x)
                pendown()
                fuel = fuel - (size * size)
            else:
                print("Чернил не хватает!")
                fuel = fuel + int(input("Дозаправте черепаху "))
        case "круг":
            color(random.choice(col))
            if fuel >= 3.14 * size * size:
                begin_fill()
                circle(size)
                end_fill()
                penup()
                x = random.randint(10, 360)
                right(x)
                forward(x)
                pendown()
                fuel = fuel - 3.14 * size * size
            else:
                print("Чернил не хватает!")
                fuel = fuel + int(input("Дозаправте черепаху "))
        case _:
            print("Черепашка не умеет рисовать такие фигуры :(")
    x = input("Продолжить? ")
    if x != "да":
        proceed = False


# ЗАДАЧА
#Дано
# * кол-во цифр в пароле (не делать проверку на отрицательность)
# * кол-во малых букв в пароле (не делать проверку на отрицательность)
# * кол-во заглавных букв в пароле (не делать проверку на отрицательность)
# * кол-во запрещенных символов в пароле (не делать проверку на отрицательность)
# Для использования пароля необходимо:
# * минимум 1 цифру, 1 малую букву, 1 заглавную букву
# * в пароле не должно быть запрещенных символов
# * минимальная длина пароля 6 символов
# Написать можно ли использовать такой пароль

numbers = int(input("Количество цифр в пароле "))
small_letters = int(input("Количество малых букв в пароле "))
big_letters = int(input("Количество заглавных букв в пароле "))
bad_simbols = int(input("Количество запрещенных символов в пароле "))
if small_letters >= 1 and big_letters >= 1 and numbers >= 1 and bad_simbols == 0 and small_letters + big_letters + numbers >= 6:
    print("Пароль можно использовать")
else:
    print("Пароль нельзя использовать")














