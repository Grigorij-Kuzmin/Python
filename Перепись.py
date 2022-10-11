x = int(input())
m = 0
y = 0
for i in range(1, x+1):
    values = input().split()
    V = int(values[0])
    S = int(values[1])
    if S == 1 and V > m:
        m = V
        y = i
print(y)