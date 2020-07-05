menu = ['Exit', 'Add matrices', 'Multiply matrix by a constant',
    'Multiply matrices', 'Transpose matrix', 'Calculate a determinant', 'Inverse matrix']
transposeMenu = ['Main diagonal', 'Side diagonal', 'Vertical line', 'Horizontal line']


def printmenu():
    for i,item in enumerate(menu[1:]):
        print(f'{i+1}. {item}')
    print("0. Exit")

def readMatrix(pos):
    firstInput = ["Enter size of matrix: ", "Enter size of first matrix: ", "Enter size of second matrix: "]
    secondInput = ["Enter matrix:", "Enter first matrix:", "Enter second matrix:"]
    row, column = input(firstInput[pos]).split()
    print(secondInput[pos])
    matrixstr = [input().split() for row in range(int(row))]
    try:
        matrix = [[int(entry) for entry in row] for row in matrixstr]
    except:
        matrix = [[float(entry) for entry in row] for row in matrixstr]
    return (matrix)

def printMatrix(matrix):
    print("The result is:")
    for row in matrix:
        for entry in row:
            print(entry, end = " ")
        print()
    print()

def addMatrix(matrixA, matrixB):
    if len(matrixA) != len(matrixB) or len(matrixA[0]) != len(matrixB[0]):
        return False
    else:
        matrixC = [[(matrixA[i][j] + matrixB[i][j]) for j in range(len(matrixB[0]))] for i in range(len(matrixB))]
        return matrixC

def mulMatrix(matrix, scalar):
    return [[scalar * matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

def matrixAddition():
    matrixA = readMatrix(1)
    matrixB = readMatrix(2)
    matrixC = addMatrix(matrixA, matrixB)
    if matrixC == False:
        print("The operation cannot be performed.")
    else:
        printMatrix(matrixC)

def matrixScalarMultiplication():
    matrixA = readMatrix(0)
    mul = input("Enter constant: ")
    try:
        mul = int(mul)
    except:
        mul = float(mul)
    printMatrix(mulMatrix(matrixA, mul))

def matrixMultiplication():
    matrixA = readMatrix(1)
    matrixB = readMatrix(2)
    rowA, rowB = len(matrixA), len(matrixB)
    columnA, columnB = len(matrixA[0]), len(matrixB[0])
    if columnA == rowB:
        matrixC = [[0 for entry in range(columnB)] for row in range(rowA)]
        for i in range(rowA):
            for j in range(columnB):
                for k in range(columnA):
                    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
        printMatrix(matrixC)
    else:
        print("The operation cannot be performed.")
def mainTranspose(matrixA):
    row, column = len(matrixA), len(matrixA[0])
    matrixB = [[matrixA[i][j] for i in range(row)] for j in range(column)]
    printMatrix(matrixB)

def sideTranspose(matrix):
    row, column = len(matrix), len(matrix[0])
    matrixB = [[matrix[i][j] for i in range(row - 1, -1, -1)]
        for j in range(column - 1, -1, -1)]
    printMatrix(matrixB)

def verticalTranspose(matrix):
    row, column = len(matrix), len(matrix[0])
    linesplit = column // 2
    for i in range(row):
        for j in range(linesplit):
            matrix[i][j], matrix[i][column - j - 1] = matrix[i][column - j - 1], matrix[i][j]
    printMatrix(matrix)

def horizontalTranspose(matrix):
    matrix.reverse()
    printMatrix(matrix)

def matrixDeterminant(matrix):
    row, column = len(matrix), len(matrix[0])
    if row != column:
        return "The operation cannot be performed."
    elif row == 0:
        return 0
    elif row == 1:
        return matrix[0][0]
    elif row == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for i in range(column):
            minor = [[matrix[k][j] for j in range(column) if j != i] for k in range(1, row)]
            determinant += matrix[0][i] * ((-1) ** (i)) * matrixDeterminant(minor)
        return determinant

def matrixInverse(matrix):
    row, column = len(matrix), len(matrix[0])
    det = matrixDeterminant(matrix)
    if (det != 0):
        adj = [[0 for col in range(column)] for r in range(row)]
        for i in range(row):
            for j in range(column):
                minor = [[matrix[k][l] for l in range(column) if l != j] for k in range(row) if k != i]
                adj[i][j] = ((-1) ** (i + j)) * matrixDeterminant(minor)
        scalar = 1 / det
        adjt = [list(b) for b in zip(*adj)]
        inverse = mulMatrix(adjt, scalar)
        printMatrix(inverse)
    else:
        print("This matrix doesn't have an inverse.")

transfunctions = [mainTranspose, sideTranspose, verticalTranspose, horizontalTranspose]

while True:
    printmenu()
    choice = int(input("Your choice: "))
    if choice == 1:
        matrixAddition()
    elif choice == 2:
        matrixScalarMultiplication()
    elif choice == 3:
        matrixMultiplication()
    elif choice == 4:
        for i,item in enumerate(transposeMenu):
            print(f'{i+1}. {item}')
        tchoice = int(input("Your choice: "))
        tmatrix = readMatrix(0)
        transfunctions[tchoice - 1](tmatrix)
    elif choice == 5:
        tmatrix = readMatrix(0)
        det = matrixDeterminant(tmatrix)
        print(f'The result is:\n{det}\n')
    elif choice == 6:
        tmatrix = readMatrix(0)
        matrixInverse(tmatrix)
    elif choice == 0:
        break
