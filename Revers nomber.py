x = int(input())
s = 0
while x != 0:
    s = x % 10 + s * 10
    x = x // 10
print(s)