def IsPerfect(x):
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i
    if s == x:
        return True
    return False


n = int(input())
x = 0
while n != 0:
    x += 1
    if IsPerfect(x):
        n -= 1
        print(x)




