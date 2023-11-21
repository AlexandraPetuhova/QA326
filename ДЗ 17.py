# задача
# Сделайте функцию, которая параметром будет принимать букву и проверять, это буква кириллицы или латиницы.

import re

def alpha_check(letter):
    if len(re.findall(r"[A-z]", letter)) >= 1 and len(re.findall(r"[А-я]", letter)) >= 1:
        print("Это смесь разных алфавитов")
    elif len(re.findall(r"[A-z]", letter)) >= 1:
        print("Это латинница")
    elif len(re.findall(r"[А-я]", letter)) >= 1:
        print("Это кириллица")
    else:
        print("Что-то пошло не так. Возможно, это не буква.")


# задача
# Сделайте функцию, которая будет возвращать дату следующей масленицы, которая празднуется в последнее воскресенье зимы.

from datetime import date
import re


def next_maslenitsa():
    start = date.today()
    year = int(''.join(re.findall(r"\d{4}", str(start))))
    month = int(''.join(re.findall(r"\-\d{2}\-", str(start)))[1:3])
    if month > 2:
        year += 1
    for day in range(30, 1, -1):
        try:
            february = date(year, 2, day)
            if february.weekday() == 6:
                break
        except:
            pass
    return february


print(f"Следующая масленица будет {next_maslenitsa()}")

# задача
# Напишите функцию, которая будет принимать произвольную строку и возвращать номер телефона вида 79370000000, если телефона в строке нет функцию должна вернуть 0

import re, functools


def find_phone(text):
    phone = re.findall(r"\b\d{11}\b", text)
    phone = list(map(lambda x: int(x), phone))
    if len(phone) == 0:
        return 0
    elif len(phone) == 1:
        phone = phone[0]
    return phone


# задача
# Напишите функцию, которая будет принимать, числа (могут быть разного кол-во) и находить среднее арифметическое для данного набора

import functools


def avarage_num(*nums):
    len_num = len(nums)
    sum = functools.reduce(lambda x, y: (x + y), nums)
    return sum / len_num
