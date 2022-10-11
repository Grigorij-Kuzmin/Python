n = int(input())
c = 0
d = 0
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        c += 1
    else:
        d += 1
print(f'Четных чисел {c}')
print(f'Нечетных чисел {d}')