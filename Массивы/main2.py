from random import randint

arr = []
# randint получает случайное число в диапазоне
# append добавление элемента в конец массива
for i in range(10):
    arr.append(randint(0, 100))
print(arr)