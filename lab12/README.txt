Клас Matrix
Конструктор (__init__ метод)

    Атрибути:
        rows: Кількість рядків у матриці.
        columns: Кількість стовпців у матриці.
        data: Двовимірний список, що представляє матрицю, ініціалізований нулями.

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

Метод add_element

    Призначення: Встановлює значення конкретного елемента у матриці.
    Параметри:
        row: Індекс рядка елемента.
        column: Індекс стовпця елемента.
        value: Значення, яке потрібно встановити у позиції (row, column).

    def add_element(self, row, column, value):
        self.data[row][column] = value


Метод sum_of_rows

    Призначення: Обчислює суму елементів у кожному рядку матриці і повертає список сум.

 def sum_of_rows(self):
        return [sum(row) for row in self.data]

Метод transpose

    Призначення: Транспонує матрицю (обмінює рядки і стовпці) і повертає новий об'єкт Matrix.

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        return Matrix(self.columns, self.rows, data=transposed_data)

Метод multiply_by

    Призначення: Перемножує поточну матрицю на іншу матрицю other і повертає нову матрицю-результат.
    Виняток: Піднімає ValueError, якщо кількість стовпців поточної матриці не дорівнює кількості рядків матриці other.

    def multiply_by(self, other):
        if self.columns != other.rows:
            raise ValueError("Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці.")
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

Метод is_symmetric

    Призначення: Перевіряє, чи є матриця симетричною (кількість рядків дорівнює кількості стовпців і дані матриці рівні транспонованим даним).

    def is_symmetric(self):
        if self.rows != self.columns:
            return False
        return self.data == self.transpose().data

Метод rotate_right

    Призначення: Повертає матрицю на 90 градусів за годинниковою стрілкою.
    def rotate_right(self):
        self.data = [list(reversed(col)) for col in zip(*self.data)]

Метод flatten

    Призначення: Перетворює двовимірний список у одновимірний.

def flatten(self):
        return [element for row in self.data for element in row]

Статичний метод from_list

    Призначення: Створює об'єкт Matrix зі списку списків.

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        columns = len(list_of_lists[0])
        matrix = Matrix(rows, columns)
        for i in range(rows):
            for j in range(columns):
                matrix.data[i][j] = list_of_lists[i][j]
        return matrix

Метод diagonal

    Призначення: Витягує діагональні елементи з квадратної матриці.

    def diagonal(self):
        if self.rows != self.columns:
            raise ValueError("Матриця повинна бути квадратною для витягування діагоналі.")
        return [self.data[i][i] for i in range(self.rows)]



