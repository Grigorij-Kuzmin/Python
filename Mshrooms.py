n = int(input())
if n % 100 >= 11 and n % 100 <= 14:
    print ('Грибов')
elif n % 10 == 1:
    print('Гриб')
elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
    print('Гриба')
else:
    print ('Грибов')