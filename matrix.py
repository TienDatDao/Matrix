import sys
import math

class Matrix:
    def __init__(self, data):
        self.data = data
        self.row = len(data)
        self.col = len(data[0]) if self.row > 0 else 0

    def __add__(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError("Two matrices have different size")

        result_data = []

        for i in range(0, self.row):
            row = []
            for j in range(0, self.col):
                row.append(self.data[i][j] + other.data[i][j])

            result_data.append(row)

        return Matrix(result_data)

    def __sub__(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError("Two matrices have different size")

        result_data = []

        for i in range(0, self.row):
            row = []
            for j in range(0, self.col):
                row.append(self.data[i][j] - other.data[i][j])

            result_data.append(row)

        return Matrix(result_data)

    # ===========================
    def __mul__(self, other):
        if isinstance(self, type(other)):
            if self.col != other.row:
                raise ValueError("Two matrices have different size")

            result_data = []

            for i in range(0, self.row):
                row = []
                for j in range(0, other.col):
                    sum = 0
                    for p in range(0, self.col):
                        sum += self.data[i][p] * other.data[p][j]
                    row.append(sum)

                result_data.append(row)

            return Matrix(result_data)
        else:
            result_data = []

            for i in range(0, self.row):
                row = []
                for j in range(0, self.col):
                    row.append(self.data[i][j] * other)

                result_data.append(row)

            return Matrix(result_data)

    # ======================================

    def checkUpperTriangularMatrix(self):
        if self.col != self.row:
            raise ValueError("The matrix is not a square matrix")

        check = True
        for i in range(0, self.row):
            for j in range(0, j + 1):
                if self.data[i][j] != 0:
                    check = False

        return check

    def checkLowerTriangularMatrix(self):
        if self.col != self.row:
            raise ValueError("The matrix is not a square matrix")

        check = True
        for i in range(0, self.row):
            for j in range(j, self.col):
                if self.data[i][j] != 0:
                    check = False

        return check

    def checkDiagonalMatrix(self):
        if self.col != self.row:
            raise ValueError("The matrix is not a square matrix")

        check = True
        for i in range(0, self.rol):
            for j in range(0, self.col):
                if self.data[i][j] != 0 and i != j:
                    check = False

        return check

    def checkSquareMatrix(self):
        if self.col == self.row:
            return True
        else:
            return False

    def checkEqual(matrix1, matrix2):
        if matrix1.col == matrix2.col and matrix1.row == matrix2.row:
            for i in range(0, matrix1.row):
                for j in range(0, matrix1.col):
                    if matrix1.data[i][j] != matrix2.data[i][j]:
                        return False

            return True

        else:
            return False

    def identityMatrix(size):
        result_data = []
        for i in range(0, size):
            row = []
            for j in range(0, size):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)

            result_data.append(row)

        return Matrix(result_data)

    def order(self):
        if self.col != self.row:
            raise ValueError("The matrix is not a square matrix")

        return self.col

    def transposeMatrix(self):
        result_data = []

        for i in range(0, self.col):
            row = []
            for j in range(0, self.row):
                row.append(self.data[j][i])
            result_data.append(row)

        return Matrix(result_data)

    def printMatrix(self):
        for i in range(0, self.row):
            print(self.data[i])


# Just check if the code works
def main():
    # with open('matrix.txt', 'r') as file:
    #     numbers_list = file.read(list(map(int, input().split())))
    #     print(numbers_list)
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    b = Matrix([[1, 2, 3], [4, 5, 6]])
    if Matrix.checkEqual(a,b):
        print("YES")
    else:
        print("NO")
    
main()
