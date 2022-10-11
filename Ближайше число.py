import random
x = int(input())
a = int(input())
m = 100
n = 0
arr = []
for i in range(x):
    arr.append(random.randint(0, 100))
print(arr)
for i in range(x):
    if m > abs(arr[i] - a):
        m = abs(arr[i] - a)
        n = i
print(n)
