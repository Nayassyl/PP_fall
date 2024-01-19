import tkinter as tk
from tkinter import ttk

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


class MatrixCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Matrix Calculator")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Entry widgets for matrix dimensions and elements
        self.rows_entry = ttk.Entry(self, width=5)
        self.rows_entry.grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self, text="x").grid(row=0, column=1)
        self.cols_entry = ttk.Entry(self, width=5)
        self.cols_entry.grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(self, text="Matrix Elements:").grid(row=1, column=0, columnspan=3)

        self.matrix_text = tk.Text(self, height=5, width=30)
        self.matrix_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        # Button to perform operations
        ttk.Button(self, text="Transpose", command=self.transpose_matrix).grid(row=3, column=0, pady=5)
        ttk.Button(self, text="Determinant", command=self.calculate_determinant).grid(row=3, column=1, pady=5)
        ttk.Button(self, text="Inverse", command=self.calculate_inverse).grid(row=3, column=2, pady=5)

        # Result display
        ttk.Label(self, text="Result:").grid(row=4, column=0, columnspan=3)
        self.result_text = tk.Text(self, height=5, width=30, state=tk.DISABLED)
        self.result_text.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

    def get_matrix_from_input(self):
        rows = int(self.rows_entry.get())
        cols = int(self.cols_entry.get())
        elements_text = self.matrix_text.get("1.0", tk.END)
        elements = [float(value) for value in elements_text.split() if value.strip()]
        return Matrix(rows, cols, elements)

    def display_result(self, result):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, str(result))
        self.result_text.config(state=tk.DISABLED)

    def transpose_matrix(self):
        matrix = self.get_matrix_from_input()
        result = matrix.transpose()
        self.display_result(result)

    def calculate_determinant(self):
        matrix = self.get_matrix_from_input()
        result = matrix.determinant()
        self.display_result(result)

    def calculate_inverse(self):
        matrix = self.get_matrix_from_input()
        try:
            result = matrix.inverse_matrix()
            self.display_result(result)
        except ValueError as e:
            self.display_result(str(e))

if __name__ == "__main__":
    app = MatrixCalculator()
    app.mainloop()


