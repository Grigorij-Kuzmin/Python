n = int(input())
c = 0
firstindex = 0
lastindex = 0
max = -999999999
for i in range(n):
    c = int(input())
    if c > max:
        max = c
        firstindex = i
    if c == max:
        lastindex = i
print(firstindex)
print(lastindex)


