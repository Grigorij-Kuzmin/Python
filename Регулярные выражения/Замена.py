import re

str = "There are many variations of passages of Lorem Ipsum available, " \
      "but the majority have suffered alteration in some form, by injected " \
      "humour, or randomised words which look even slightly believable. "

# Все слова короче 5 букв заменить на звёздочки

for i in range(1, 5):
      str = re.sub(f'\\b[\\w\']{{{i}}}\\b', '*'*i, str)

print(str)

'''
Цензура
В файле nasty.txt в каждой строке содержится строка для поиска в тексте.
В файле input.txt текст для обработки.
Необходимо заменить все вхождения данных строк в текст на их цензуру: слово => с***о
1. СлОвО => С***О
Вывести отредактированный текст на экран
'''