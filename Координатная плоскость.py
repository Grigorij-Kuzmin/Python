x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('Первая четверть')
if x < 0 and y > 0:
    print ('Вторая четверть')
if x < 0 and y < 0:
    print('Третья четверть')
if x > 0 and y < 0:
    print('Четвертая четверть')
if x == 0 or y == 0:
    print('Точка лежит на оси')




