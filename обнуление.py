import random
x = int(input())
Max = 0
Min = 0
arr = []
for i in range(x):
    arr.append(random.randint(0, 100))
print(arr)
for i in range(x):
    if arr[Max] < arr[i]:
        Max = i
    if arr[Min] > arr[i]:
        Min = i
if Min > Max:
    Min, Max = Max, Min
for i in range(Min + 1, Max):
    arr[i] = 0
print(arr)
