class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}

    @staticmethod
    def from_file(file_path):
        matrix = None
        with open(file_path, 'r') as file:
            lines = file.readlines()
            rows = int(lines[0].split('=')[1])
            cols = int(lines[1].split('=')[1])
            matrix = SparseMatrix(rows, cols)
            for line in lines[2:]:
                row, col, value = map(int, line.strip()[1:-1].split(','))
                matrix.set_element(row, col, value)
        return matrix

    def get_element(self, row, col):
        if row in self.data and col in self.data[row]:
            return self.data[row][col]
        return 0

    def set_element(self, row, col, value):
        if row not in self.data:
            self.data[row] = {}
        self.data[row][col] = value

    def add(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = SparseMatrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.set_element(row, col, self.get_element(row, col) + matrix.get_element(row, col))
        return result

    def subtract(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        result = SparseMatrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.set_element(row, col, self.get_element(row, col) - matrix.get_element(row, col))
        return result

    def multiply(self, matrix):
        if self.cols != matrix.rows:
            raise ValueError("Number of columns in first matrix must equal number of rows in second matrix")
        result = SparseMatrix(self.rows, matrix.cols)
        for i in range(self.rows):
            for j in range(matrix.cols):
                for k in range(self.cols):
                    result.set_element(i, j, result.get_element(i, j) + self.get_element(i, k) * matrix.get_element(k, j))
        return result

    def __str__(self):
        result = f'rows={self.rows}\ncols={self.cols}\n'
        for row in range(self.rows):
            for col in range(self.cols):
                if self.get_element(row, col) != 0:
                    result += f'({row}, {col}, {self.get_element(row, col)})\n'
        return result