class Matrix:
    #initialize matrix with specified dimensions and optional initial elements
    def __init__(self, rows, cols, elements=None):
        self.rows = rows
        self.cols = cols
        if elements:
            if len(elements) != rows * cols:
                raise ValueError("Number of elements does not match matrix dimensions.")
            #if initial elements are provided,append elements in matrix 
            self.data = [elements[i * cols:(i + 1) * cols] for i in range(rows)]
        else:
            #if no initial elements, initialize the matrix with zeros
            self.data = [[0] * cols for _ in range(rows)]

    def __repr__(self):
        #provide a string representation of the matrix for printing
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        #add two matrices
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for addition.")
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result

    def __sub__(self, other):
        #subtract one matrix from another
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for subtraction.")
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result

    def __mul__(self, other):
        #multiply matrix by a scalar or another matrix
        if isinstance(other, (int, float)):
            #multiply by a scalar
            result = Matrix(self.rows, self.cols)
            result.data = [[self.data[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
            return result
        elif isinstance(other, Matrix):
            #multiply by another matrix
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
        #transpose matrix (swap rows and columns)
        result = Matrix(self.cols, self.rows)
        result.data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return result

    def determinant(self):
        #calculate determinant
        if self.rows != self.cols:
            raise ValueError("Determinant can only be calculated for square matrices.")
        else:
            if self.rows == 1:
                return self.data[0][0]
            elif self.rows == 2:
                return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
            else:
                det = 0
                #recursion to calculate the determinant for larger matrices
                for j in range(self.cols):
                    minor_matrix = self.get_minor_matrix(0, j)
                    det += ((-1) ** j) * self.data[0][j] * minor_matrix.determinant()
                return det

    def get_minor_matrix(self, row, col):
        #extract minor matrix by excluding specified row and column
        minor_data = [row[:col] + row[col + 1:] for row in (self.data[:row] + self.data[row + 1:])]
        return Matrix(self.rows - 1, self.cols - 1, [element for row in minor_data for element in row])
    
    def adjugate_matrix(self):
        #calculate adjugate
        if self.rows != self.cols:
            raise ValueError("Adjugate matrix can only be calculated for square matrices.")
        else:
            co_matrix = Matrix(self.rows, self.cols)
            for row in range(self.rows):
                for col in range(self.cols):
                    #minor matrix determinant to calculate the cofactor
                    co_matrix.data[row][col] = ((-1) ** (row + col) * self.get_minor_matrix(row, col).determinant())
            #transpose cofactor matrix to obtain adjugate matrix
            return co_matrix.transpose()
    
    def cofactor_matrix(self):
        #calculate cofactor
        if self.rows != self.cols:
            raise ValueError("Cofactor matrix can only be calculated for square matrices.")
        else:
            co_matrix = Matrix(self.rows, self.cols)
            for row in range(self.rows):
                for col in range(self.cols):
                    #minor matrix determinant to calculate cofactor
                    co_matrix.data[row][col] = ((-1) ** (row + col) * self.get_minor_matrix(row, col).determinant())
            return co_matrix
    
    def inverse_matrix(self):
        #calculate inverse
        if self.rows != self.cols:
            raise ValueError("Inverse matrix can only be calculated for square matrices.")
        elif self.determinant() == 0:
            raise ValueError("Inverse matrix does not exist, determinant equal to zero.")
        else:
            #inverse matrix is adjugate matrix divided by determinant
            inverse = self.adjugate_matrix()
            return inverse * (1 / self.determinant())
    
    def sle(self, vector):
        #solve a system of linear equations using inverse matrix
        if len(vector) != self.rows:
            raise ValueError("Dimensions do not match.")
        else:
            v = Matrix(len(vector), 1, vector)
            #multiply the inverse matrix by the column vector
            return self.inverse_matrix() * v

    def lu_decomposition(self):
        if self.rows != self.cols:
            raise ValueError("LU decomposition can only be calculated for square matrices.")
        #шnitialize matrices for L(lower triangular) and U(upper triangular)
        L = Matrix(self.rows, self.cols)
        U = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            #upper triangular matrix(U)
            for j in range(i, self.cols):
                #U[i][j] is element at row i, column j in upper triangular matrix
                #subtract sum of products of corresponding elements from L and U
                U.data[i][j] = self.data[i][j] - sum(L.data[i][k] * U.data[k][j] for k in range(i))
            
            #lower triangular matrix (L)
            #diagonal elements of L are always 1
            L.data[i][i] = 1
            for j in range(i + 1, self.rows):
                #L[j][i] is element at row j, column i in lower triangular matrix
                #subtract sum of products of corresponding elements from L and U
                #divide result by diagonal element of U at position (i, i)
                L.data[j][i] = (self.data[j][i] - sum(L.data[j][k] * U.data[k][i] for k in range(i))) / U.data[i][i]
        return L, U
    
    def gram_schmidt(self):
        #transpose matrix to work with column vectors
        vectors = self.transpose()
        #check if any vector has all elements equal to zero
        for vector in vectors.data:
            if all(elem == 0 for elem in vector):
                raise ValueError("Matrix elements should be nonzero")
        #initialize list to store orthogonalized vectors 
        #first vector with no changes
        result = [vectors.data[0]]
        #iterate through the vectors and orthogonalize them
        for i in range(1, len(vectors.data)):
            orthogonalized = vectors.data[i].copy()
            #orthogonalize the current vector with respect to previous vectors
            for j in range(i):
                #calculate the projection factor
                projection_factor = sum(vectors.data[i][k] * result[j][k] for k in range(len(vectors.data[i]))) / sum(result[j][k] * result[j][k] for k in range(len(result[j])))
                #calculate the projection of the current vector onto the subspace spanned by previous vectors
                projection = [projection_factor * coord for coord in result[j]]
                #subtract the projection from the current vector
                orthogonalized = [x - y for x, y in zip(orthogonalized, projection)]
            #check if the orthogonalized vector is not a zero vector
            if any(abs(coord) > 1e-10 for coord in orthogonalized):
                result.append(orthogonalized)
        #create a matrix from the orthogonalized vectors
        ress = Matrix(len(result), len(result[0]))
        #normalize the orthogonalized vectors
        ress.data = [[coord / (sum(c**2 for c in vector))**0.5 for coord in vector] for vector in result]
        #transpose the result to obtain the final orthogonalized matrix(ONB)
        return ress.transpose()
    
    def qr_decomposition(self):
        #perform qr decomposition using the Gram-Schmidt orthogonalization
        q = self.gram_schmidt()
        #r matrix is obtained by multiplying the transpose of q with the original matrix
        r = q.transpose() * self
        #return the orthogonalized matrix q and the upper triangular matrix r
        return q, r
    
    def qr_iteration_with_eigenvectors(self, max_iterations=5, tolerance=1e-10):
        #initialize the matrix for QR iteration
        m = self
        #initialize the matrix to store eigenvectors
        eigenvectors = Matrix.identity(self.rows)
        #perform qr iteration for a specified number of iterations or until convergence
        for _ in range(max_iterations):
            #perform QR decomposition
            q, r = m.qr_decomposition()
            #update the matrix for the next iteration
            m = r * q
            #update the matrix of eigenvectors
            eigenvectors = eigenvectors * q
            """print(eigenvectors)
            print("\n")"""
            #calculate the sum of off-diagonal elements for convergence check
            off_diag_sum = sum(abs(m.data[i][j]) for i in range(m.rows) for j in range(m.cols) if i != j)
            #check for convergence based on the off-diagonal sum
            if off_diag_sum < tolerance:
                break
        #extract eigenvalues from the diagonal of the resulting matrix
        eigenvalues = [round(m.data[i][i], 1) for i in range(m.rows)]
        #return the eigenvalues and eigenvectors
        return eigenvalues, eigenvectors
    
    @staticmethod
    def identity(size):
        # Static method to create an identity matrix
        identity_matrix = Matrix(size, size)
        for i in range(size):
            identity_matrix.data[i][i] = 1
        return identity_matrix
    
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
    








#test
m = Matrix(3, 3, [1, 2, 3,
                  4, 5, 6,
                  7, 8, 9])
m1 = Matrix(3,3,[1,0,2,
                 0,2,0,
                 0,-1,1])
m2 = Matrix(4,4,[52,30,49,28,
                 30,50,8,44,
                 49,8,46,16,
                 28,44,16,22])
eigenvalues, eigenvectors = m2.qr_iteration_with_eigenvectors()
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
