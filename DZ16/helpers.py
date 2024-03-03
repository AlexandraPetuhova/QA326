from random import choice

def random_word(count, content):
    eng = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K",
           "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u",
           "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    rus = ["А", "а", "Б", "б", "В", "в", "Г", "г", "Д", "д", "Е", "е", "Ё", "ё", "Ж", "ж", "З", "з", "И", "и",
           "Й", "й", "К", "к", "Л", "л", "М", "м", "Н", "н", "О", "о", "П", "п", "Р", "р", "С", "с", "Т", "т", "У",
           "у", "Ф", "ф", "Х", "х", "Ц", "ц", "Ч", "ч", "Ш", "ш", "Щ", "щ", "Ъ", "ъ", "Ы", "ы", "Ь", "ь", "Э", "э",
           "Ю", "ю", "Я", "я"]
    symbol = ["@", "!", "$", "%", "^", "&", "*", "(", "_", "+", "#", "~", "-", "=", "<", ">", "?", "/", "|", r"\\",
              '{', '}', "[", "]", ";", ":", "'", '"', "`", "´", "¬"]
    htonb = ["金", "🙂"]
    alphabet = []
    if "r" in content:
        for element in rus:
            alphabet.append(element)
    if "e" in content:
        for element in eng:
            alphabet.append(element)
    if "n" in content:
        for element in num:
            alphabet.append(element)
    if "s" in content:
        for element in symbol:
            alphabet.append(element)
    if "h" in content:
        for element in htonb:
            alphabet.append(element)
    word = []
    for i in range(count):
        word.append(choice(alphabet))
    return "".join(word)

