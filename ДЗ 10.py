# # задача
# # Найдите количество различных элементов данного массива.

massiv = []
element = input("Введите элемент массива ")
massiv.append(element)
print("Для окончания ввода элементов введите 0")
while True:
    element = input("Ещё один? ")
    if element == "0":
        break
    massiv.append(element)
for k in massiv:
    new_massiv = set(massiv)
print(f"Количество различных элементов данного массива: {len(new_massiv)}")

 # то же, но для многомерного массива

massiv = [[1, 2, 3, 43, 75, -34, 5, 2],
          ["Пётр", "Геннадий", "Магазин Пятёрочка"],
          [34, 56, "EGwekgnw", {43, "rewrgweg", (3, 23, 54, "Комсомол"), "Геннадий"}, 8], -98]
new_massiv = set()
def count_elements(m):
    try:
        for n in m:
            if type(n) == list or type(n) == tuple or type(n) == set:
                count_elements(n)
            else:
                new_massiv.add(n)
    except:
        pass
count_elements(massiv)
print(new_massiv)
print(f"Количество различных элементов данного массива: {len(new_massiv)}")


# задача
# Найти наиболее часто встречающийся элемент в массиве целых чисел.

from random import randint
massiv = list(randint(-100, 100) for i in range(0, randint(1, 20)))
print(massiv)
# massiv = [1, 1, 4, 4, 2, 2, 2, 3, 3, 3]
count = 1
commons = set()
for element in massiv:
    if massiv.count(element) > count:
        count = massiv.count(element)
        common = element
        commons.clear()
    elif massiv.count(element) == count and massiv.count(element) != 1 and element != common:
        commons.add(element)
        commons.add(common)
if commons:
    print("Наиболее часто встречающиеся элементы это: ", end='')
    print(*sorted(commons), sep=', ')
else:
    try:
        if common:
            print(f"Наиболее часто встречающийся элемент это {common}")
    except:
        print("Элементы не повторяются")

# задача
# В данном массиве найти два наименьших элемента.

from random import randint
massiv = list(randint(-100, 100) for i in range(0, randint(1, 20)))
print(massiv)
if len(massiv) >= 2:
    print("Наименьшие элементы массива это ", end="")
    print(sorted(set(massiv))[1], sorted(set(massiv))[0], sep=" и ")
else:
    print("В массиве нету столько элементов")

# задача
# В данном массиве найдите наибольшую серию подряд идущих элементов, расположенных по возрастанию.

from random import randint
massiv = list(randint(-100, 100) for i in range(0, randint(1, 20)))
print(massiv)
new_list = []
range_ = set()
for count in range(0, len(massiv) - 1):
    if massiv[count] < massiv[count + 1]:
        range_.add(massiv[count])
        range_.add(massiv[count + 1])
    else:
        new_list.append(sorted(range_))
        range_= set()
        continue
if range_:
    new_list.append(sorted(range_))
new_list = sorted(new_list, key=len)
if len(new_list[-1]) > len(new_list[-2]):
    print("Наибольшая серия подряд идущих элементов, расположенных по возрастанию, это", end=' ')
    print(*new_list[-1], sep=', ')
else:
    answer = []
    for i in new_list:
        if len(i) == len(new_list[-1]):
            answer.append(i)
    print("Наибольшие серии подряд идущих элементов, расположенных по возрастанию, это", end=' ')
    print(*answer, sep=', ')


# задача
# Поменять местами наибольший и наименьший элементы массива

from random import randint
massiv = list(randint(0, 100) for i in range(0, randint(1, 20)))
print(massiv)
new_massive = massiv.copy()
new_massive[new_massive.index(max(new_massive))] = min(massiv)
new_massive[new_massive.index(min(new_massive))] = max(massiv)
print(f"Новый массив: {new_massive}")


# задача
# напечатать прямоугольник (заданы длина, ширина и символ) при помощи цикла for

while True:
    try:
        width = int(input("Введите ширину "))
        if width <= 0:
            print("Число не может быть меньше 0. Попробуйте ещё раз")
        else:
            break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз")
while True:
    try:
        length = int(input("Введите длину "))
        if length <= 0:
            print("Число не может быть меньше 0. Попробуйте ещё раз")
        else:
            break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз")
symbol = input("Введите символ ")
for i in range(width):
    print(symbol * length)

# задача
# напечатать полый прямоугольник (заданы длина, ширина и символ) при помощи цикла for

while True:
    try:
        width = int(input("Введите ширину "))
        if width <= 0:
            print("Число не может быть меньше 0. Попробуйте ещё раз")
        else:
            break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз")
while True:
    try:
        length = int(input("Введите длину "))
        if length <= 0:
            print("Число не может быть меньше 0. Попробуйте ещё раз")
        else:
            break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз")
symbol = input("Введите символ ")
massiv = [[1] * width] * length
for index, list_ in enumerate(massiv):
    for index2, element in enumerate(list_):
        if index == 0 or index == length - 1:
            print(symbol, end=' ')
        else:
            if index2 == 0 or index2 == width - 1:
                print(symbol, end=' ')
            else:
                print("  ", end='')
    print('')

# задача
# напечатать квадрат (заданы длина и символ) при помощи цикла for  по образцу
#
# *	*	*	*	*
# *	*		*	*
# *		*		*
# *	*		*	*
# *	*	*	*	*

while True:
    try:
        length = int(input("Введите длину "))
        if length <= 0:
            print("Число не может быть меньше 0. Попробуйте ещё раз")
        else:
            break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз")
symbol = input("Введите символ ")
massiv = [[1] * length] * length
middle = length // 2
for index, list_ in enumerate(massiv):
    for index2, element in enumerate(list_):
        if index in [middle - 1, middle + 1] and index2 == middle:
            print("  ", end='')
        elif index2 in [middle - 1, middle + 1] and index == middle:
            print("  ", end='')
        else:
            print(symbol, end=' ')
    print('')
