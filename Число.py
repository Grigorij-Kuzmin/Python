x = int(input())
arr = []
while x != 0:
    arr.append(x % 10)
    x = x // 10
arr.sort(reverse=True)
print(arr)
arr.sort()


