startSum = int(input())
percent = int(input())
targetSum = float(input())
i = 0
percent = percent / 100
while  startSum < targetSum:
    i += 1
    startSum += startSum * percent
    print(i)
    print(startSum)
print(f'Количество месяцев = {i}')
print(f'Итоговая сумма = {startSum:.2f}')