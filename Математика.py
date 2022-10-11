x = int(input())
Max = 0
Min = 0
s = 0
p = 1
arr = input().split()
for i in range(x):
    arr[i] = int(arr[i])
    if arr[i] > 0:
        s = s + arr[i]
    if arr[i] > arr[Max]:
        Max = i
    if arr[i] < arr[Min]:
        Min = i
if Max < Min:
    Min, Max = Max, Min
for i in range(Min + 1, Max):
    p = arr[i] * p
print(s, p)


