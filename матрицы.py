x = int(input())
matr = [[0 for i in range(x)]for j in range(x)]


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:<3d}', end=' ')
        print()


def fill1(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j or i + j == len(matrix[i]) - 1:
                matrix[i][j] = 0
            if i < j and i + j < len(matrix[i]) - 1:
                matrix[i][j] = 1
            if i > j and i + j < len(matrix[i]) - 1:
                matrix[i][j] = 4
            if i < j and i + j > len(matrix[i]) - 1:
                matrix[i][j] = 2
            if i > j and i + j > len(matrix[i]) - 1:
                matrix[i][j] = 3



def fill2(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = (i + j) % 2


def fill3(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i]) - i):
            matrix[i][j] = i
            matrix[j][i] = i
            matrix[len(matrix[j]) - i - 1][j] = i
            matrix[j][len(matrix[j]) - i - 1] = i

fill3(matr)
printMatrix(matr)

