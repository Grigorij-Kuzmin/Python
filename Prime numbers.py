def IsSimple(x):
    for i in range(2, x):
       if x % i == 0:
           return False
    return True


N = int(input())
x = 0
while N != 0:
    x += 1
    if IsSimple(x):
        N -= 1
        print(x)




