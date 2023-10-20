# задача
# # # дан  список
# # # запрещено использовать sort, max, map преобразовывать список в другие типы тоже нельзя
# # # найти минимальный элемент в списке

from random import randint, uniform
list = []
for i in range(randint(0, 10)):
    list.append(uniform(-100, 100))
for i in range(randint(0, 10)):
    list.append(randint(-100, 100))
min_el = list[0]
if list:
    print(list)
    for element in list:
        if float(element) < float(min_el):
            min_el = element
    print(f"Минимальный элемент в списке это {min_el}")
else:
    print("Список пустой")


# задача
# # # дан  список
# # # запрещено использовать sort, max, count, map преобразовывать список в другие типы тоже нельзя
# # # найти элемент(ы) в списке, который повторяется дважды и более раз

from random import randint, uniform
list = []
for i in range(randint(0, 10)):
    list.append(uniform(-10, 10))
for i in range(randint(0, 20)):
    list.append(randint(-10, 10))
if list:
    print(list)
    repeat = []
    for index, element in enumerate(list):
        for index2, element2 in enumerate(list):
            if index != index2 and element == element2:
                if element not in repeat:
                    repeat.append(element)
    if repeat:
        print("Повторяющиеся элементы списка: ", end="")
        for i in range(len(repeat)-1):
            print(repeat[i], end=', ')
        print(repeat[-1])
    else:
        print("Элементы не повторяются")
else:
    print("Список пустой")

# задача
# # # дан  список
# # запрещено использовать sort, max, count, sum, map
# # # сформировать новый список, с положительными числами

from random import randint, uniform
list = []
for i in range(randint(0, 10)):
    list.append(uniform(-100, 100))
for i in range(randint(0, 10)):
    list.append(randint(-100, 100))
new_list = []
if list:
    print(list)
    for element in list:
        if element > 0:
            new_list.append(element)
    print(f"Новый список: {new_list}")
else:
    print("Список пустой")


# задача
# # # дан  список
# # запрещено использовать sort, max, count, sum, map
# # # удалить из этого списка все отрицательные элементы

from random import randint, uniform

list = []
for i in range(randint(0, 10)):
    list.append(uniform(-100, 100))
for i in range(randint(0, 10)):
    list.append(randint(-100, 100))
if list:
    print(list)
    for element in list:
        if element < 0:
            list.remove(element)
    print(f"Новый список: {list}")
else:
    print("Список пустой")

# задача
# # # дан  список
# # # найти все элементы в этом списке, из которых извлекается квадратный корень в виде целого числа (4, 16 и т.д.)


from random import randint, uniform
from math import sqrt
list = []
for i in range(randint(0, 1)):
    list.append(uniform(-100, 100))
for i in range(randint(0, 20)):
    list.append(randint(-100, 100))
list_sqrt = []
if list:
    print(list)
    for element in list:
        if type(element) == int and element >= 0:
            if sqrt(element) % 1 == 0:
                list_sqrt.append(element)
    if list_sqrt:
        print("Числа, из которых извлекается квадратный корень в виде целого числа:", end=" ")
        print(*list_sqrt, sep=", ")
    else:
        print("Чисел, из которых извлекается квадратный корень в виде целого числа, нет.")
else:
    print("Список пустой")


# задача
# # # дан  список
# # # найти  все элементы в этом списке , у которых индекс и значение совпадают. Исходный список нельзя менять

from random import randint, uniform

list = []
for i in range(randint(0, 20)):
    list.append(randint(-10, 10))
for i in range(randint(0, 10)):
    list.append(uniform(-10, 10))
new_list = []
if list:
    print(list)
    for index, element in enumerate(list):
        if index == element:
            new_list.append(element)
    if new_list:
        print("Элементы списка, у которых индекс и значение совпадают:", end=' ')
        print(*new_list, sep=', ')
    else:
        print("Элементов списка, у которых индекс и значение совпадают, не обнаружено")
else:
    print("Список пустой")

# задача
# # # дан  список
# # # запрещено использовать sort, max, count, sum, map , преобразовывать список в другие типы тоже нельзя
# # # найти произведение всех элементов в этом списке


from random import randint, uniform

list = []
for i in range(randint(0, 10)):
    list.append(uniform(-100, 100))
for i in range(randint(0, 10)):
    list.append(randint(-100, 100))
multiplication = 1
if list:
    print(list)
    for element in list:
        multiplication = multiplication * element
    print(f"Произведение всех элементов в списке равно {multiplication}")
else:
    print("Список пустой")
