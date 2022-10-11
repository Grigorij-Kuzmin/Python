n = 0
m = 0
k = 0
s = 0
values = input().split()
for i in range(3):
    values[i] = int(values[i])
n, m, k = values
matrix = [['.' for i in range(m)] for j in range(n)]
for i in range(k):
    values = input().split()
    x = int(values[0]) - 1
    y = int(values[1]) - 1
    matrix[x][y] = '*'
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '.':
            s = 0
            if i + 1 < n and matrix[i + 1][j] == '*':
                s += 1
            if i - 1 > 0 and matrix[i - 1][j] == '*':
                s += 1
            if j + 1 < m and matrix[i][j + 1] == '*':
                s += 1
            if j - 1 > 0 and matrix[i][j - 1] == '*':
                s += 1
            if j - 1 > 0 and i - 1 > 0 and matrix[i - 1][j - 1] == '*':
                s += 1
            if j + 1 < m and i + 1 < n and matrix[i + 1][j + 1] == '*':
                s += 1
            if j - 1 > 0 and i + 1 < n and matrix[i + 1][j - 1] == '*':
                s += 1
            if j + 1 < m and i - 1 > 0 and matrix[i - 1][j + 1] == '*':
                s += 1
            if s != 0:
                matrix[i][j] = s
for i in range(n):
    for j in range(m):









