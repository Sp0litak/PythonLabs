class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, column, value):
        self.data[row][column] = value

    def sum_of_rows(self):
        return [sum(row) for row in self.data]

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        return Matrix(self.columns, self.rows, data=transposed_data)

    def multiply_by(self, other):
        if self.columns != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def is_symmetric(self):
        if self.rows != self.columns:
            return False
        return self.data == self.transpose().data

    def rotate_right(self):
        self.data = [list(reversed(col)) for col in zip(*self.data)]

    def flatten(self):
        return [element for row in self.data for element in row]

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        columns = len(list_of_lists[0])
        matrix = Matrix(rows, columns)
        for i in range(rows):
            for j in range(columns):
                matrix.data[i][j] = list_of_lists[i][j]
        return matrix

    def diagonal(self):
        if self.rows != self.columns:
            raise ValueError("Matrix must be square to extract diagonal.")
        return [self.data[i][i] for i in range(self.rows)]