def digitCount(x):
    s = 0
    while x != 0:
        x = x // 10
        s += 1
    return s


def IsArm(x):
    sum = 0
    deg = digitCount(x)
    y = x
    while x != 0:
        sum += (x % 10) ** deg
        x = x // 10
    if sum == y:
        return True
    return False


n = int(input())
x = 0
while n != 0:
    x += 1
    if IsArm(x):
        n -= 1
        print(x, end=' ')


