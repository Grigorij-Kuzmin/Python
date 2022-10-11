a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print('Можно составить треугольник')
    if a == b and b == c:
        print('Треугольник равносторонний')
    elif a == b or b == c or c == b:
        print('Треугольник равнобедренный')
    hyp = max(a, b, c)
    k1 = min(a, b, c)
    k2 = a + b + c - hyp - k1
    if hyp ** 2 == k1 ** 2 + k2 ** 2:
        print(f'Треугольник прямоугольный')
    elif hyp ** 2 > k1 ** 2 + k2 ** 2:
        print(f'Треугольник остроугольный')
    elif hyp ** 2 < k1 ** 2 + k2 ** 2:
        print(f'Треугольник тупоугольный')
else:
    print('Треугольник составить невозможно')


