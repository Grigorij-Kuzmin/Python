matrix = []
n = int(input())
hasEror = False
for i in range(n ** 2):
    values = input().split()
    matrix.append([])
    for c in range(n ** 2):
        if int(values[c]) >= 1 and int(values[c]) <= n ** 2:
            matrix[i].append(int(values[c]))
        else:
            hasEror = True
if hasEror == False:
    for i in range(len(matrix)):
        tmpcol = []
        tmprow = []
        for j in range(len(matrix[i])):
            if matrix[i][j] not in tmpcol:
                tmpcol.append(matrix[i][j])
            else:
                hasEror = True
            if matrix[j][i] not in tmprow:
                tmprow.append(matrix[j][i])
            else:
                hasEror = True
    def chekSquare(matrix, x, y, n):
        jmp = []
        for i in range(x, n):
            for j in range(y, n):
                if matrix[i][j] not in jmp:
                    jmp.append(matrix[i][j])
                else:
                    return False
        return True


if hasEror == False:
    for i in range(0, n ** 2, n):
        for j in range(0, n ** 2, n):
           if not chekSquare(matrix, i, j, n):
               hasEror = True
if hasEror == True:
    print('Incorrect')
else: print('Correct')
