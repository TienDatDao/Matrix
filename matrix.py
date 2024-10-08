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

        return result_data

    def __sub__(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError("Two matrices have different size")
        
        result_data = []
        
        for i in range(0, self.row):
            row = []
            for j in range(0, self.col):
                row.append(self.data[i][j] - other.data[i][j])
            
            result_data.append(row)

        return result_data

    def __mul__(self, other):
        if self.col != other.row:
            raise ValueError("Two matrices have different size")
        
        result_data = []

        for i in range(0, self.row):
            row = []
            for j in range(0, other.col):
                sum = 0
                for p in range(0, self.col):
                    sum += self.data[i][p]*other.data[p][j]
                row.append(sum)

            result_data.append(row)

        return result_data
    
# Just check if the code works
def main():
    a = Matrix([[1],[2],[3],[4]])
    b = Matrix([[1,2,3,4]])
    c = a*b
    for i in range(0,len(c)):
        print(c[i])

main()