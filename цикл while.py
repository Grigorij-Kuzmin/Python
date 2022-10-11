x = int(input())
a = x - 1
max = 0
c = 1
while x != 0:
    if x > a:
        c += 1
    if x < a and c > max:
        max = c
        c = 1
    a = x
    x = int(input())
if c > max:
    max = c
print(max)





