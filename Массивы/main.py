# Список (Массив)
# Может содержать элементы различных типов
arr = [2, 78, 1, 'hello', False]

# Вывод массива перебором
for i in arr:
    print(f'{i} ', end='')

print()

# Вывод массива индексацией
for i in range(len(arr)):
    print(f'{arr[i]} ', end=' ')
