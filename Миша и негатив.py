def getmatrix(row, col):
    matrix = []
    for i in range(values[0]):
        str = input()
        matrix.append([])
        for c in str:
            matrix[i].append(c)
    return matrix


matrix = []
s = 0
values = input().split()
for i in range(2):
    values[i] = int(values[i])
matrix = getmatrix(values[0], values[1])
input()
matrix_neg = []
matrix_neg = getmatrix(values[0], values[1])
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == matrix_neg[i][j]:
            s += 1
print(s)








