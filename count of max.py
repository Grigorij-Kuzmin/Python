n = int(input())
c = 0
b = 0
max = 0
for i in range(n):
    c = int(input())
    if c > max:
        max = c
        b = 0
    if c == max:
        b += 1
print(max)
print(b)