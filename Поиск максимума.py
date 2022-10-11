n = int(input())
max = -99999999
findex = 0
for i in range(n):
    x = int(input())
    if x > max:
        max = x
        findex += 1
print(max)