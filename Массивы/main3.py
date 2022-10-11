# Чтение чисел в одной строке
# 45 13 54 78 11 12 45
# max = 78

'''
values = input().split()
for i in range(len(values)):
    values[i] = int(values[i])
'''

# map функция, применяющая другую функцию к кажому элементу массива
# list преобразование в список
values = list(map(int, input().split()))

print(max(values))