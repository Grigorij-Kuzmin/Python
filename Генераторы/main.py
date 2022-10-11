matr = [[0 for i in range(10)] for j in range(10)]

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # < - выравнивание по левому краю
            # 3d - на каждое целое число (d) отводится 3 позиции
            print(f'{matrix[i][j]:<3d}', end='')
        print()

printMatrix(matr)