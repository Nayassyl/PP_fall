import math
class Matrix:
    def __init__(self, rows, cols, elements=None):
        self.rows = rows
        self.cols = cols
        if elements:
            if len(elements) != rows * cols:
                raise ValueError("Number of elements does not match matrix dimensions.")
            self.data = [elements[i * cols:(i + 1) * cols] for i in range(rows)]
        else:
            self.data = [[0] * cols for _ in range(rows)]

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for addition.")
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for subtraction.")
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            result.data = [[self.data[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
            return result
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix.")
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
            return result
        else:
            raise ValueError("Unsupported operand type for multiplication.")

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        result.data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return result
    
    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Determinant can only be calculated for square matrices.")
        else:
            if self.rows == 1:
                return self.data[0][0]
            elif self.rows == 2:
                return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
            else:
                det = 0
                for j in range(self.cols):
                    minor_matrix = self.get_minor_matrix(0, j)
                    det += ((-1) ** j) * self.data[0][j] * minor_matrix.determinant()
                return det

    def get_minor_matrix(self, row, col):
        minor_data = [row[:col] + row[col + 1:] for row in (self.data[:row] + self.data[row + 1:])]
        return Matrix(self.rows - 1, self.cols - 1, [element for row in minor_data for element in row])
    def adjugate_matrix(self):
        if self.rows != self.cols:
            raise ValueError("Adjugate matrix can only be calculated for square matrices.")
        else:
            co_matrix = Matrix(self.rows, self.cols)
            for row in range(self.rows):
                for col in range(self.cols):
                    co_matrix.data[row][col] = ((-1) ** (row + col) * self.get_minor_matrix(row, col).determinant())
            return co_matrix.transpose()
    
    def cofactor_matrix(self):
        if self.rows != self.cols:
            raise ValueError("Cofactor matrix can only be calculated for square matrices.")
        else:
            co_matrix = Matrix(self.rows, self.cols)
            for row in range(self.rows):
                for col in range(self.cols):
                    co_matrix.data[row][col] = ((-1) ** (row + col) * self.get_minor_matrix(row, col).determinant())
            return co_matrix
    
    def inverse_matrix(self):
        if self.rows != self.cols:
            raise ValueError("Inverse matrix can only be calculated for square matrices.")
        elif self.determinant() == 0:
            raise ValueError("Inverse matrix does not exist, determinant equal to zero.")
        else:
            inverse = self.adjugate_matrix()
            return inverse * (1 / self.determinant())
    
    def sle(self, vector):
        v = Matrix(len(vector), 1, vector)
        return self.inverse_matrix() * v

    def lu_decomposition(self):
        if self.rows != self.cols:
            raise ValueError("LU decomposition can only be calculated for square matrices.")
        
        L = Matrix(self.rows, self.cols)
        U = Matrix(self.rows, self.cols)
        
        for i in range(self.rows):
            # Upper triangular matrix (U)
            for j in range(i, self.cols):
                U.data[i][j] = self.data[i][j] - sum(L.data[i][k] * U.data[k][j] for k in range(i))
            
            # Lower triangular matrix (L)
            L.data[i][i] = 1  # Diagonal elements of L are always 1
            for j in range(i + 1, self.rows):
                L.data[j][i] = (self.data[j][i] - sum(L.data[j][k] * U.data[k][i] for k in range(i))) / U.data[i][i]
        
        return L, U
    
    def gram_schmidt(self):
        vectors = self.transpose()
        # return vectors.data
        for vector in vectors.data:
            if all(elem == 0 for elem in vector):
                raise ValueError("Matrix elements should be nonzero")
        result = [vectors.data[0]]
        for i in range(1, len(vectors.data)):
            orthogonalized = vectors.data[i].copy()
            for j in range(i): 
                projection = sum(vectors.data[i][k] * result[j][k] for k in range(len(vectors.data[i])))/sum(result[j][k] * result[j][k] for k in range(len(vectors.data[i]))) 
                orthogonalized = [x - projection * y for x, y in zip(orthogonalized, result[j])] 
            if not all(coord == 0 for coord in orthogonalized): 
                result.append(orthogonalized) 
        ress = Matrix(vectors.rows, vectors.cols)
        ress.data = [[coord / math.sqrt(sum(c**2 for c in vector)) for coord in vector] for vector in result] 
        return ress.transpose()
    
    def qr_decomposition(self):
        q = self.gram_schmidt()
        r = q.transpose() * self
        return q, r
    def qr_iteration(self):
        itlim = 1000
        ress = self
        for i in range(itlim):
            q, r = ress.qr_decomposition()
            ress = r * q
        eigenvalues = [round(ress.data[i][i], 1) for i in range(ress.rows)]
        return eigenvalues
    
    def gaussian_elimination(self):
            # Perform Gaussian elimination to reduce the matrix to reduced row echelon form
            # (This is a simplified method and may not be suitable for all matrices)
            matrix_copy = Matrix(self.rows, self.cols, [element for row in self.data for element in row])

            for i in range(min(self.rows, self.cols)):
                # Find the pivot element
                pivot_row = max(range(i, self.rows), key=lambda j: abs(matrix_copy.data[j][i]))

                # Swap rows if necessary
                if pivot_row != i:
                    matrix_copy.data[i], matrix_copy.data[pivot_row] = matrix_copy.data[pivot_row], matrix_copy.data[i]

                # Make the pivot element 1
                pivot = matrix_copy.data[i][i]
                matrix_copy.data[i] = [element / pivot for element in matrix_copy.data[i]]

                # Eliminate other elements in the column
                for j in range(self.rows):
                    if j != i:
                        factor = matrix_copy.data[j][i]
                        matrix_copy.data[j] = [element - factor * matrix_copy.data[i][idx] for idx, element in enumerate(matrix_copy.data[j])]

            return matrix_copy




m = Matrix(4,4,[2,1,3,3,2,1,-1,1, 2, -1, 3, -3, 2,-1, -1, -1])
print(m.qr_iteration())


