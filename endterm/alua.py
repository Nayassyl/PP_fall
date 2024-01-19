
from tkinter import ttk, messagebox
import tkinter as tk


class Matrix:
    def __init__(self, rows, cols, elems=None):
        self.rows = rows
        self.cols = cols
        if elems:
            if len(elems) != rows * cols:
                raise ValueError(
                    "Number of elements does not match matrix dimensions.")
            self.data = [elems[i * cols:(i + 1) * cols]
                         for i in range(rows)]
        else:
            self.data = [[0.0] * cols for _ in range(rows)]

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for addition.")
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] + other.data[i][j]
                        for j in range(self.cols)] for i in range(self.rows)]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for subtraction.")
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] - other.data[i][j]
                        for j in range(self.cols)] for i in range(self.rows)]
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            result.data = [
                [self.data[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
            return result
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError(
                    "Number of columns in the first matrix must match the number of rows in the second matrix.")
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    result.data[i][j] = sum(
                        self.data[i][k] * other.data[k][j] for k in range(self.cols))
            return result
        else:
            raise ValueError("Unsupported operand type for multiplication.")

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        result.data = [[self.data[j][i]
                        for j in range(self.rows)] for i in range(self.cols)]
        return result

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError(
                "Determinant can only be calculated for square matrices.")
        else:
            if self.rows == 1:
                return self.data[0][0]
            elif self.rows == 2:
                return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
            else:
                det = 0
                for j in range(self.cols):
                    minor_matrix = self.get_minor_matrix(0, j)
                    det += ((-1) ** j) * \
                        self.data[0][j] * minor_matrix.determinant()
                return det

    def get_minor_matrix(self, row, col):
        minor_data = [row[:col] + row[col + 1:]
                      for row in (self.data[:row] + self.data[row + 1:])]
        return Matrix(self.rows - 1, self.cols - 1, [element for row in minor_data for element in row])

    def adjugate_matrix(self):
        if self.rows != self.cols:
            raise ValueError(
                "Adjugate matrix can only be calculated for square matrices.")
        else:
            co_matrix = Matrix(self.rows, self.cols)
            for row in range(self.rows):
                for col in range(self.cols):
                    co_matrix.data[row][col] = (
                        (-1) ** (row + col) * self.get_minor_matrix(row, col).determinant())
            return co_matrix.transpose()

    def cofactor_matrix(self):
        if self.rows != self.cols:
            raise ValueError(
                "Cofactor matrix can only be calculated for square matrices.")
        else:
            co_matrix = Matrix(self.rows, self.cols)
            for row in range(self.rows):
                for col in range(self.cols):
                    co_matrix.data[row][col] = (
                        (-1) ** (row + col) * self.get_minor_matrix(row, col).determinant())
            return co_matrix

    def inverse_matrix(self):
        if self.rows != self.cols:
            raise ValueError(
                "Inverse matrix can only be calculated for square matrices.")
        elif self.determinant() == 0:
            raise ValueError(
                "Inverse matrix does not exist, determinant equal to zero.")
        else:
            inverse = self.adjugate_matrix()
            return inverse * (1 / self.determinant())

    def sle(self, vector):
        v = Matrix(len(vector), 1, vector)
        return self.inverse_matrix() * v

    def lu_decomposition(self):
        if self.rows != self.cols:
            raise ValueError(
                "LU decomposition can only be calculated for square matrices.")

        L = Matrix(self.rows, self.cols)
        U = Matrix(self.rows, self.cols)

        for i in range(self.rows):
            # Upper triangular matrix (U)
            for j in range(i, self.cols):
                U.data[i][j] = float(
                    self.data[i][j] - sum(L.data[i][k] * U.data[k][j] for k in range(i)))

            # Lower triangular matrix (L)
            L.data[i][i] = 1.0  # Diagonal elems of L are always 1
            for j in range(i + 1, self.rows):
                L.data[j][i] = float(
                    self.data[j][i] - sum(L.data[j][k] * U.data[k][i] for k in range(i))) / U.data[i][i]

        return L, U


class MatrixApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Matrix Operations")

        # Matrix A
        self.label_a = tk.Label(master, text="Matrix A:")
        self.label_a.grid(row=0, column=0, padx=5, pady=5)
        self.entry_a = tk.Text(master, height=4, width=10)
        self.entry_a.grid(row=0, column=1, padx=5, pady=5)

        # Number of rows and columns for Matrix A
        self.label_rows_a = tk.Label(master, text="Rows:")
        self.label_rows_a.grid(row=1, column=0, padx=5, pady=5)
        self.rows_var_a = tk.IntVar(value=2)
        self.entry_rows_a = ttk.Spinbox(
            master, from_=1, to=10, textvariable=self.rows_var_a)
        self.entry_rows_a.grid(row=1, column=1, padx=5, pady=5)

        self.label_cols_a = tk.Label(master, text="Columns:")
        self.label_cols_a.grid(row=2, column=0, padx=5, pady=5)
        self.cols_var_a = tk.IntVar(value=2)
        self.entry_cols_a = ttk.Spinbox(
            master, from_=1, to=10, textvariable=self.cols_var_a)
        self.entry_cols_a.grid(row=2, column=1, padx=5, pady=5)

        # Result
        self.label_result = tk.Label(master, text="Result:")
        self.label_result.grid(row=3, column=0, padx=5, pady=5)
        self.entry_result = tk.Text(master, height=8, width=20, wrap=tk.WORD)
        self.entry_result.grid(row=3, column=1, padx=5, pady=5)

        # Operation buttons
        self.transpose_button = tk.Button(
            master, text="Transpose", command=self.perform_transpose)
        self.transpose_button.grid(row=4, column=0, padx=5, pady=5)
        self.inverse_button = tk.Button(
            master, text="Inverse", command=self.perform_inverse)
        self.inverse_button.grid(row=4, column=1, padx=5, pady=5)
        self.determinant_button = tk.Button(
            master, text="Determinant", command=self.perform_determinant)
        self.determinant_button.grid(row=5, column=0, padx=5, pady=5)
        self.lu_decomposition_button = tk.Button(
            master, text="LU Decomposition", command=self.perform_lu_decomposition)
        self.lu_decomposition_button.grid(row=5, column=1, padx=5, pady=5)

    def get_matrix_from_entry(self, entry, rows, cols):
        matrix_str = entry.get("1.0", tk.END)
        try:
            matrix_data = [list(map(float, row.split()))
                           for row in matrix_str.split('\n') if row]
            return Matrix(rows, cols, elems=[element for row in matrix_data for element in row])
        except ValueError:
            messagebox.showerror("Error", "Invalid matrix input")

    def perform_transpose(self):
        rows_a = self.rows_var_a.get()
        cols_a = self.cols_var_a.get()
        matrix_a = self.get_matrix_from_entry(self.entry_a, rows_a, cols_a)

        result_matrix = matrix_a.transpose()
        self.display_result(result_matrix)

    def perform_inverse(self):
        rows_a = self.rows_var_a.get()
        cols_a = self.cols_var_a.get()
        matrix_a = self.get_matrix_from_entry(self.entry_a, rows_a, cols_a)

        try:
            result_matrix = matrix_a.inverse_matrix()
            self.display_result(result_matrix)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def perform_determinant(self):
        rows_a = self.rows_var_a.get()
        cols_a = self.cols_var_a.get()
        matrix_a = self.get_matrix_from_entry(self.entry_a, rows_a, cols_a)

        try:
            result = matrix_a.determinant()
            self.entry_result.config(state="normal")
            self.entry_result.delete(1.0, tk.END)
            self.entry_result.insert(tk.END, f"Determinant: {result}")
            self.entry_result.config(state="disabled")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def perform_lu_decomposition(self):
        rows_a = self.rows_var_a.get()
        cols_a = self.cols_var_a.get()
        matrix_a = self.get_matrix_from_entry(self.entry_a, rows_a, cols_a)

        try:
            L, U = matrix_a.lu_decomposition()
            self.entry_result.config(state="normal")
            self.entry_result.delete(1.0, tk.END)
            self.entry_result.insert(tk.END, f"L:\n{L}\n\nU:\n{U}")
            self.entry_result.config(state="disabled")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def display_result(self, matrix):
        self.entry_result.config(state="normal")
        self.entry_result.delete(1.0, tk.END)
        self.entry_result.insert(tk.END, matrix.__repr__())
        self.entry_result.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()
