# Рекурсия - явление, когда функция вызывает саму себя

# Сумма числел от 1 до n
def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)


# Вывести последовательность чисел от 1 до n
def seq(n):
    if n > 0:
        seq(n - 1)
        print(n, end=' ')


print(sum(10))
seq(10)
