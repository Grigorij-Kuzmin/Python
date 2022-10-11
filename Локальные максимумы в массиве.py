import random
x = int(input())
arr = []
for i in range(x):
    arr.append(random.randint(0, 100))
print(arr)
for i in range(1, x - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        print(i)