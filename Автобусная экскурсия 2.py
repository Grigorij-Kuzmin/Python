N = int(input())
b = 0
a = -1
for i in range(1, N+1):
    values = input().split().append(input())
    x = int(values[i])
    if x <= 437:
        a = i
        break
if a != -1:
    print(f'crash {a}')
else:
    print('No crash')