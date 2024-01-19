
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



import tkinter as tk
from tkinter import messagebox, scrolledtext

class MatrixGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Operations")

        self.create_widgets()

    def create_widgets(self):
        # First Section: Single Matrix Operations
        single_matrix_frame = tk.Frame(self.root, padx=10, pady=10)
        single_matrix_frame.pack(side=tk.LEFT, padx=10)

        tk.Label(single_matrix_frame, text="Enter Matrix Elements:").pack()
        tk.Label(single_matrix_frame, text="Rows:").pack()
        self.matrix_rows_entry_single = tk.Entry(single_matrix_frame, width=5)
        self.matrix_rows_entry_single.pack(pady=5)
        tk.Label(single_matrix_frame, text="Columns:").pack()
        self.matrix_cols_entry_single = tk.Entry(single_matrix_frame, width=5)
        self.matrix_cols_entry_single.pack(pady=5)
        tk.Label(single_matrix_frame, text="(rows x columns)").pack()
        self.matrix_entry_single = scrolledtext.ScrolledText(single_matrix_frame, width=30, height=5)
        self.matrix_entry_single.pack(pady=5)

        tk.Button(single_matrix_frame, text="Transpose", command=self.transpose_matrix_single).pack()
        tk.Button(single_matrix_frame, text="Determinant", command=self.calculate_determinant_single).pack()
        tk.Button(single_matrix_frame, text="Inverse", command=self.calculate_inverse_single).pack()

        # Result Box for Single Matrix Operations
        self.result_box_single = scrolledtext.ScrolledText(single_matrix_frame, width=40, height=8)
        self.result_box_single.pack(pady=10)

        # Second Section: Two Matrices Operations
        two_matrices_frame = tk.Frame(self.root, padx=10, pady=10)
        two_matrices_frame.pack(side=tk.RIGHT, padx=10)

        tk.Label(two_matrices_frame, text="Enter Matrix A Elements:").pack()
        tk.Label(two_matrices_frame, text="Rows:").pack()
        self.matrix_rows_entry_a = tk.Entry(two_matrices_frame, width=5)
        self.matrix_rows_entry_a.pack(pady=5)
        tk.Label(two_matrices_frame, text="Columns:").pack()
        self.matrix_cols_entry_a = tk.Entry(two_matrices_frame, width=5)
        self.matrix_cols_entry_a.pack(pady=5)
        tk.Label(two_matrices_frame, text="(rows x columns)").pack()
        self.matrix_entry_a = scrolledtext.ScrolledText(two_matrices_frame, width=30, height=5)
        self.matrix_entry_a.pack(pady=5)

        tk.Label(two_matrices_frame, text="Enter Matrix B Elements:").pack()
        tk.Label(two_matrices_frame, text="Rows:").pack()
        self.matrix_rows_entry_b = tk.Entry(two_matrices_frame, width=5)
        self.matrix_rows_entry_b.pack(pady=5)
        tk.Label(two_matrices_frame, text="Columns:").pack()
        self.matrix_cols_entry_b = tk.Entry(two_matrices_frame, width=5)
        self.matrix_cols_entry_b.pack(pady=5)
        tk.Label(two_matrices_frame, text="(rows x columns)").pack()
        self.matrix_entry_b = scrolledtext.ScrolledText(two_matrices_frame, width=30, height=5)
        self.matrix_entry_b.pack(pady=5)

        tk.Button(two_matrices_frame, text="Add", command=self.add_matrices).pack()
        tk.Button(two_matrices_frame, text="Subtract", command=self.subtract_matrices).pack()
        tk.Button(two_matrices_frame, text="Multiply", command=self.multiply_matrices).pack()

        # Result Box for Two Matrices Operations
        self.result_box_two_matrices = scrolledtext.ScrolledText(two_matrices_frame, width=40, height=8)
        self.result_box_two_matrices.pack(pady=10)

    def get_matrix_from_entry(self, entry_rows, entry_cols, entry):
        rows = int(entry_rows.get())
        cols = int(entry_cols.get())
        elements = entry.get("1.0", tk.END).split()
        try:
            elements = [float(element) for element in elements]
        except ValueError:
            messagebox.showerror("Error", "Invalid matrix elements. Please enter numeric values.")
            return None
        if len(elements) != rows * cols:
            messagebox.showerror("Error", "Number of elements does not match matrix dimensions.")
            return None
        return Matrix(rows, cols, elements)

    def display_result_single(self, result):
        self.result_box_single.config(state=tk.NORMAL)
        self.result_box_single.delete("1.0", tk.END)
        self.result_box_single.insert(tk.END, result)
        self.result_box_single.config(state=tk.DISABLED)

    def display_result_two_matrices(self, result):
        self.result_box_two_matrices.config(state=tk.NORMAL)
        self.result_box_two_matrices.delete("1.0", tk.END)
        self.result_box_two_matrices.insert(tk.END, result)
        self.result_box_two_matrices.config(state=tk.DISABLED)

    def transpose_matrix_single(self):
        matrix = self.get_matrix_from_entry(self.matrix_rows_entry_single, self.matrix_cols_entry_single, self.matrix_entry_single)
        if matrix:
            result = matrix.transpose()
            self.display_result_single(f"Result:\n{result}")

    def calculate_determinant_single(self):
        matrix = self.get_matrix_from_entry(self.matrix_rows_entry_single, self.matrix_cols_entry_single, self.matrix_entry_single)
        if matrix:
            determinant = matrix.determinant()
            self.display_result_single(f"Determinant: {determinant}")

    def calculate_inverse_single(self):
        matrix = self.get_matrix_from_entry(self.matrix_rows_entry_single, self.matrix_cols_entry_single, self.matrix_entry_single)
        if matrix:
            try:
                inverse = matrix.inverse_matrix()
                self.display_result_single(f"Inverse Matrix:\n{inverse}")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def add_matrices(self):
        matrix_a = self.get_matrix_from_entry(self.matrix_rows_entry_a, self.matrix_cols_entry_a, self.matrix_entry_a)
        matrix_b = self.get_matrix_from_entry(self.matrix_rows_entry_b, self.matrix_cols_entry_b, self.matrix_entry_b)

        if matrix_a and matrix_b:
            try:
                result = matrix_a + matrix_b
                self.display_result_two_matrices(f"Result:\n{result}")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def subtract_matrices(self):
        matrix_a = self.get_matrix_from_entry(self.matrix_rows_entry_a, self.matrix_cols_entry_a, self.matrix_entry_a)
        matrix_b = self.get_matrix_from_entry(self.matrix_rows_entry_b, self.matrix_cols_entry_b, self.matrix_entry_b)

        if matrix_a and matrix_b:
            try:
                result = matrix_a - matrix_b
                self.display_result_two_matrices(f"Result:\n{result}")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def multiply_matrices(self):
        matrix_a = self.get_matrix_from_entry(self.matrix_rows_entry_a, self.matrix_cols_entry_a, self.matrix_entry_a)
        matrix_b = self.get_matrix_from_entry(self.matrix_rows_entry_b, self.matrix_cols_entry_b, self.matrix_entry_b)

        if matrix_a and matrix_b:
            try:
                result = matrix_a * matrix_b
                self.display_result_two_matrices(f"Result:\n{result}")
            except ValueError as e:
                messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixGUI(root)
    root.mainloop()
