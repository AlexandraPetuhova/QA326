# задача
# Дана строка, в которой буква h встречается минимум два раза. Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.

line = input("Введите строку, в которой буква h встречается минимум два раза ")
while True:
    if line.count("h") >= 2:
        break
    else:
        line = input("Количество букв \"h\" должно быть 2 и больше. Попробуйте ещё раз. ")
line = line[line.find("h") + 1:line.rfind("h")]
print(f"Новая строка: {line}")

# задача
# Посчитайте кол-во чисел в произвольной строке (число - это набор цифр, перед число и после числа ставятся пробелы)

# line = "sdrg92 34 rsgwe243 42 52nus 425n"
line = input("Введите произвольную строку")
line = list(line.split())
num_count = 0
for item in line:
    if item.isdigit():
        num_count += 1
print(f"\nКоличество чисел в строке - {num_count}")

# задача
# Посчитайте кол-во букв в произвольной строке

# line = "sdrg92 34 rsgwe243 42 52nus 425n"
line = input("Введите произвольную строку")
num_count = 0
for item in line:
    if item.isalpha():
        num_count += 1
print(f"\nКоличество букв в строке - {num_count}")

# задача
# Пользователь вводит положительное целое число. Зашифровать каждую цифру серией из букв (конкретный принцип составления серии букв разработать самостоятельно).

while True:
    try:
        line = int(input("Введите положительное целое число "))
        if line < 0:
            print("Число не может быть меньше 0. Попробуйте ещё раз")
        else:
            break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз")
cipher = {'1': '!', '2': '"', '3': '£', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}
line_ciphered = ""
for letter in str(line):
    line_ciphered = line_ciphered + cipher[letter]
print(f"Готовый шифр - {line_ciphered}")

# задача
# есть словарь для шифрования, а также произвольная строка
# Реализовать интерфейс для  шифрования и дешифрования
# пример словаря
# d = {"1": "!", "2": "@", "3": "#"}

cipher = {'1': '!', '2': '"', '3': '£', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}
word = input("Введите слово или шифр ")
word_ciphered = ""
if word[0] in cipher:
    for letter in word:
        word_ciphered = word_ciphered + cipher[letter]
    print(f"Готовый шифр - {word_ciphered}")
elif word[0] in cipher.values():
    for letter in word:
        for number, symbol in cipher.items():
            if letter == symbol:
                word_ciphered = word_ciphered + number
    print(f"Расшифровка - {word_ciphered}")
else:
    print("Расшифровка невозможна")

# задача
# Дана произвольная многострочная строка.
# ●	Сначала выведите третий символ этой строки.
# ●	Во второй строке выведите предпоследний символ этой строки.
# ●	В третьей строке выведите первые пять символов этой строки.
# ●	В четвертой строке выведите всю строку, кроме последних двух символов.
# ●	В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
# ●	В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# ●	В седьмой строке выведите все символы в обратном порядке.
# ●	В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# ●	В девятой строке выведите длину данной строки.


line = """Тестирование программного обеспечения - это метод проверки соответствия фактического программного продукта ожидаемым требованиям, который также необходим, чтобы убедиться, что продукт не содержит дефектов. Если в программном обеспечении есть ошибки или дефекты, они могут быть обнаружены на раннем этапе производства ПО и устранены до его поставки в продакшн.
Правильно протестированный программный продукт обеспечивает надежность, безопасность и высокую производительность, что в дальнейшем приводит к экономии времени, денег и удовлетворенности клиентов.
Тестирование важно, потому что ошибки в программном обеспечении могут дорого обойтись производителю. Они могут привести к серьезным финансовым потерям и даже человеческим жертвам.
Testing (Тестирование) – самый “нижний”, первый уровень, проверка создаваемого программного продукта на соответствие требованиям к этому продукту.
По факту это реактивная работа (выдали – проверил – описал дефекты – исправили), которая может помочь исправить дефекты в уже созданном программном обеспечении, но не более того.
Основная задача тестирования – выявить и зафиксировать дефекты.
QC (Quality Control, контроль качества) – второй уровень, включающий в себя тестирование, но не ограничивающийся им. Quality Control обеспечивает не только проверку продукта на соответствие требованиям, но и соответствие заранее согласованному уровню качества продукта и готовность к выпуску продукта в продакшен.
Основная задача контроля качества – предоставить объективную картину того, что происходит с качеством продукта на разных этапах разработки.
QA (Quality Assurance, обеспечение качества) – третий уровень, который включает в себя мероприятия на всех этапах разработки (и, по-хорошему, использования) продукта для обеспечения согласованного уровня качества продукта. Это уже проактивная работа, т.к. основная задача  обеспечения качества – это выстроить систему, которая будет превентивно работать на качество продукта, чтобы при тестировании количество дефектов было минимальным.
В зависимости от специфики проекта сюда может включаться тестирование документации, ревью кода на соответствие стандартам, внедрение каких-то методик по работе с качеством, коммуникационные активности и прочее.
"""
# print(line)
paragraphs = {}
line2 = line
for paragraph in range(1, line.count("\n") + 1):
    paragraphs[paragraph] = line2.find("\n")
    line2 = line2.replace("\n", "*", 1)
print(f"\nТретий символ первой строки - \"{line[2]}\"")
print(f"Предпоследний символ второй строки - \"{line[paragraphs[1]:paragraphs[2]][-2]}\"")
print(f"Первые пять символов третьей строки - \"{line[paragraphs[2] + 1:paragraphs[3]][:5]}\"")
print(f"Четвёртая строка, кроме последних двух символов - \"{line[paragraphs[3] + 1:paragraphs[4]][:-2]}\"")
print(f"Все символы с четными индексами пятой строки - \"{line[paragraphs[4] + 1:paragraphs[5]][::2]}\"")
print(f"Все символы с нечетными индексами шестой строки - \"{line[paragraphs[5] + 1:paragraphs[6]][1::2]}\"")
print(f"Все символы седьмой строки в обратном порядке - \"{line[paragraphs[6] + 1:paragraphs[7]][::-1]}\"")
print(f"Все символы восьмой строки в обратном порядке через один - \"{line[paragraphs[7] + 1:paragraphs[8]][::-2]}\"")
print(f"Длина девятой строки - \"{len(line[paragraphs[8] + 1:paragraphs[9]])}\"")