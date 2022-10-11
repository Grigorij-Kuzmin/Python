from random import randint

n = int(input())
s = 0
arr = []
for i in range(n):
    arr.append(randint(0, 10))
arr.sort()
print(arr)
for i in range(n - 1):
    if arr[i] != arr[i + 1]:
        s += 1
print(s + 1)