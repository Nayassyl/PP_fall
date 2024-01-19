
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
            self.data = [[0.0] * cols for _ in range(rows)]

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
            L.data[i][i] = 1.0
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



import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate calculator")

        # Create tabs for matrix operations
        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill=tk.BOTH, expand=True)

        # Create two frames for matrix operations
        self.matrix_operations_frame = ttk.Frame(self.tabs)
        self.two_matrix_operations_frame = ttk.Frame(self.tabs)

        # Add tabs
        self.tabs.add(self.matrix_operations_frame, text="Ultimate Matrix Operations")
        self.tabs.add(self.two_matrix_operations_frame, text="Ultimate Two Matrix Operations")

        # Initialize matrix dimensions for the first section
        self.rows_var = tk.IntVar(value=3)
        self.cols_var = tk.IntVar(value=3)

        # Initialize matrix dimensions for the second section
        self.rows_var_a = tk.IntVar(value=3)
        self.cols_var_a = tk.IntVar(value=3)
        self.rows_var_b = tk.IntVar(value=3)
        self.cols_var_b = tk.IntVar(value=3)

        # Matrix Operations Frame
        self.create_matrix_operations_frame()

        # Two Matrix Operations Frame
        self.create_two_matrix_operations_frame()

    def create_matrix_operations_frame(self):
        frame = self.matrix_operations_frame

        # Matrix Dimensions
        dimensions_frame = ttk.Frame(frame)
        dimensions_frame.pack(pady=10)
        ttk.Label(dimensions_frame, text="Rows:").grid(row=0, column=0)
        ttk.Spinbox(dimensions_frame, from_=1, to=10, textvariable=self.rows_var).grid(row=0, column=1)
        ttk.Label(dimensions_frame, text="Cols:").grid(row=0, column=2)
        ttk.Spinbox(dimensions_frame, from_=1, to=10, textvariable=self.cols_var).grid(row=0, column=3)

        # Matrix Entries
        matrix_entries_frame = ttk.Frame(frame)
        matrix_entries_frame.pack(pady=10)
        ttk.Label(matrix_entries_frame, text="Matrix A:").grid(row=0, column=0)
        matrix_a_entry = scrolledtext.ScrolledText(matrix_entries_frame, height=5, width=20)
        matrix_a_entry.grid(row=0, column=1, padx=5)

        # Result Textbox
        result_text = scrolledtext.ScrolledText(frame, height=10, width=60, wrap=tk.WORD)
        result_text.pack(pady=10)

        # Matrix Operations Buttons
        operations_frame = ttk.Frame(frame)
        operations_frame.pack(pady=10)

        def perform_operation(operation):
            try:
                rows = self.rows_var.get()
                cols = self.cols_var.get()

                matrix_a_elements = [float(val) for val in matrix_a_entry.get(1.0, tk.END).split()]

                matrix_a = Matrix(rows, cols, matrix_a_elements)

                if operation == "Transpose":
                    result_matrix = matrix_a.transpose()
                elif operation == "Determinant":
                    result_matrix = matrix_a.determinant()
                elif operation == "Inverse":
                    result_matrix = matrix_a.inverse_matrix()
                elif operation == "QR Decomposition":
                    Q, R = matrix_a.qr_decomposition()
                    result_matrix = f"Q:\n{Q}\n\nR:\n{R}"
                elif operation == "LU Decomposition":
                    L, U = matrix_a.lu_decomposition()
                    result_matrix = f"L:\n{L}\n\nU:\n{U}"
                elif operation == "Gram-Schmidt":
                    result_matrix = matrix_a.gram_schmidt()
                elif operation == "Eigenvalues/Eigenvectors":
                    eigenvalues, eigenvectors = matrix_a.qr_iteration_with_eigenvectors()
                    result_matrix = f"Eigenvalues: {eigenvalues}\n\nEigenvectors:\n{eigenvectors}"
                elif operation == "Gaussian Elimination":
                    result_matrix = matrix_a.gaussian_elimination()

                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, result_matrix)

            except Exception as e:
                messagebox.showerror("Error", str(e))

        operations = [
            "Transpose", "Determinant", "Inverse", "QR Decomposition",
            "LU Decomposition", "Gram-Schmidt", "Eigenvalues/Eigenvectors", "Gaussian Elimination"
        ]

        for operation in operations:
            ttk.Button(operations_frame, text=operation, command=lambda op=operation: perform_operation(op)).pack(side=tk.LEFT, padx=5)

    def create_two_matrix_operations_frame(self):
        frame = self.two_matrix_operations_frame

        # Matrix A Dimensions
        dimensions_frame_a = ttk.Frame(frame)
        dimensions_frame_a.pack(pady=10)
        ttk.Label(dimensions_frame_a, text="Rows A:").grid(row=0, column=0)
        ttk.Spinbox(dimensions_frame_a, from_=1, to=10, textvariable=self.rows_var_a).grid(row=0, column=1)
        ttk.Label(dimensions_frame_a, text="Cols A:").grid(row=0, column=2)
        ttk.Spinbox(dimensions_frame_a, from_=1, to=10, textvariable=self.cols_var_a).grid(row=0, column=3)

        # Matrix B Dimensions
        dimensions_frame_b = ttk.Frame(frame)
        dimensions_frame_b.pack(pady=10)
        ttk.Label(dimensions_frame_b, text="Rows B:").grid(row=0, column=0)
        ttk.Spinbox(dimensions_frame_b, from_=1, to=10, textvariable=self.rows_var_b).grid(row=0, column=1)
        ttk.Label(dimensions_frame_b, text="Cols B:").grid(row=0, column=2)
        ttk.Spinbox(dimensions_frame_b, from_=1, to=10, textvariable=self.cols_var_b).grid(row=0, column=3)

        # Matrix Entries
        matrix_entries_frame = ttk.Frame(frame)
        matrix_entries_frame.pack(pady=10)
        ttk.Label(matrix_entries_frame, text="Matrix A:").grid(row=0, column=0)
        matrix_a_entry = tk.Text(matrix_entries_frame, height=5, width=20)
        matrix_a_entry.grid(row=0, column=1, padx=5)
        ttk.Label(matrix_entries_frame, text="Matrix B:").grid(row=0, column=2)
        matrix_b_entry = tk.Text(matrix_entries_frame, height=5, width=20)
        matrix_b_entry.grid(row=0, column=3, padx=5)

        # Result Textbox
        result_text = scrolledtext.ScrolledText(frame, height=10, width=60, wrap=tk.WORD)
        result_text.pack(pady=10)

        # Matrix Operations Buttons
        operations_frame = ttk.Frame(frame)
        operations_frame.pack(pady=10)

        def perform_operation(operation):
            try:
                rows_a = self.rows_var_a.get()
                cols_a = self.cols_var_a.get()

                rows_b = self.rows_var_b.get()
                cols_b = self.cols_var_b.get()

                matrix_a_elements = [float(val) for val in matrix_a_entry.get(1.0, tk.END).split()]
                matrix_b_elements = [float(val) for val in matrix_b_entry.get(1.0, tk.END).split()]

                matrix_a = Matrix(rows_a, cols_a, matrix_a_elements)
                matrix_b = Matrix(rows_b, cols_b, matrix_b_elements)

                if operation == "Add":
                    result_matrix = matrix_a + matrix_b
                elif operation == "Subtract":
                    result_matrix = matrix_a - matrix_b
                elif operation == "Multiply":
                    result_matrix = matrix_a * matrix_b

                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, result_matrix)

            except Exception as e:
                messagebox.showerror("Error", str(e))

        operations = ["Add", "Subtract", "Multiply"]

        for operation in operations:
            ttk.Button(operations_frame, text=operation, command=lambda op=operation: perform_operation(op)).pack(side=tk.LEFT, padx=5)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()

