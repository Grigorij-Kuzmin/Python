values = input().split()
n = int(values[0])
k = int(values[1])
numbers = []
for i in range(1,n + 1):
    numbers.append(str(i))
numbers.sort()
print(numbers.index(str(k)) + 1)


