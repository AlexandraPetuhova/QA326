# Творческое задание (его тоже можно сделать как самостоятельную задачу) **сложная**

board = []
line = []
for line1 in range(4):
    for square in range(8):
        if square % 2 == 0:
            # line.append("⬜")
            line.append("□")
        else:
            # line.append("⬛")
            line.append("■")
    # line = ''.join(line)
    board.append(line)
    line = list(''.join(line[1:8])+str(line[0]))
    board.append(line)
    line = []
while True:
    queen = input("Введите координаты ферзя ")
    queen = queen.split()
    queen = ''.join(queen)
    try:
        x = int(queen[0])
        y = int(queen[1])
        if 0 < x < 9 and 0 < y < 9:
            break
    except ValueError:
        print("Попробуйте ещё раз")
        continue
for line1 in range(8):
    for square in range(8):
        if line1 == x - 1 or square == y - 1:
            board[line1][square] = "*"
        for i in range(8):
            if line1 == x - 1 - i and square == y - 1 - i:
                board[line1][square] = "*"
            elif line1 == x - 1 + i and square == y - 1 - i:
                board[line1][square] = "*"
            elif line1 == x - 1 + i and square == y - 1 + i:
                board[line1][square] = "*"
            elif line1 == x - 1 - i and square == y - 1 + i:
                board[line1][square] = "*"
board[x-1][y-1] = "♕"
print(*board, sep="\n")




# задача
# Дана произвольная строка создать строку, в которой содержаться только цифры из исходной строки
#
# ПРимер
# ввод
# АА”АА324А К*К№5 10 79
#
# вывод
# 32451079
#
import random, functools
random_string = list(input("Введите строку "))
new_string = list(filter(lambda x: x.isdigit(), random_string))
print(f"Новая строка: {''.join(new_string)}")


# задача
# Дан список чисел (можно создать любым способом, но приветствуется через лямбду функцию и random).
# Необходимо создать новый список чисел, которые будут составлять 70% от исходного числа. Для создания такого списка использовать функцию map().
# Необходимо посчитать разницу между суммами исходного списка и преобразованного
# ПРИМЕР
# ввод
# 100, 50, 30 (сумма 180)
# 70, 35, 21 (сумма 126)
#
# вывод
# 54

import random, functools
numlist1 = [(lambda x: random.randint(0, 1000))(x) for x in range(10)]
print(numlist1)
numlist2 = list(map(lambda x: round(x / 100 * 70, 3), numlist1))
print(numlist2)
numlist1 = functools.reduce(lambda x, y: x+y, numlist1)
numlist2 = round(functools.reduce(lambda x, y: x+y, numlist2), 2)
print(f"Разница между суммами исходного списка и преобразованного равна {numlist1 - numlist2}")




#задача
#
#Дан список чисел (можно создать любым способом, но приветствуется через лямбду функцию и random).
#Создать новый список при помощи filter(), отобрать значения по маске 3*3? , где * - любое кол-во цифр, ? - одна цифра
#Вычислить при помощи reduce() произведение нового списка
#Пример работы маски
#даны числа
#31139
#339
#1339
#33
#вывод
#31139
#339

import random, functools, re
data = [(lambda x: random.randint(300, 4000))(x) for x in range(50)]
print(data)
exp = r"3\d*3\d"
data2 = list(filter(lambda x: re.fullmatch(exp, str(x)), data))
print(data2)
mult = functools.reduce(lambda x, y: x * y, data2)
print(f"Произведение нового списка равно {mult}")



# задача
# Дана строка, состоящая из символов A, B и C. Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.


import random, functools
abc = ["A", "B",  "C"]
string = [(lambda x: random.choice(abc))(x) for x in range(50)]
print("".join(string))
string2 = ""
string3 = []
for i in range(len(string)-1):
    if string[i] != string[i+1]:
        string2 = string2 + string[i]
    else:
        string2 = string2 + string[i]
        string3.append(string2)
        string2 = ""
if string[-2] == string[-1]:
    string3.append(string[-1])
else:
    string2 = string2 + string[-1]
    string3.append(string2)
string = list(map(lambda x: len(x), string3))
print(f"Максимальное количество идущих подряд символов, среди которых каждые два соседних различны - {max(string)}")



#Задание 5
#Дана строка, состоящая из символов X, Y, и Z. Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.

import random, functools
xyz = ["X", "Y",  "Z"]
string = [(lambda x: random.choice(xyz))(x) for x in range(50)]
string = "".join(string)
print(string)
separator = "XZZY"
string = string.split(separator)
string = list(map(lambda x: len(x), string))
print(f"Максимальное количество идущих подряд символов, среди которых нет подстроки XZZY - {max(string)}")