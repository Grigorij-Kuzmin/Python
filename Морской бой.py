matrix = []
s = 0
n = 0
values = input().split()
for i in range(2):
    values[i] = int(values[i])
for i in range(values[0]):
    str = input()
    matrix.append([])
    for c in str:
        matrix[i].append(c)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '.':
            s = 0
            if i + 1 < len(matrix) and matrix[i + 1][j] == '*':
                s += 1
            if i - 1 >= 0 and matrix[i - 1][j] == '*':
                s += 1
            if j + 1 < len(matrix[i]) and matrix[i][j + 1] == '*':
                s += 1
            if j - 1 >= 0 and matrix[i][j - 1] == '*':
                s += 1
            if s == 0:
                n += 1
print(n)

