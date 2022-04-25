# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, input_list):
        self.list = input_list
        self.rows = len(self.list)
        self.columns = len(self.list[0])
        self.number_of_digits = 0

        # defining length of longest element
        for row in range(0, len(self.list)):
            for el in self.list[row]:
                if self.number_of_digits < len(str(el)):
                    self.number_of_digits = len(str(el))

            if self.columns < len(self.list[row]):
                self.columns = len(self.list[row])

        # making matrix rectangular if it is not
        for line in range(0, len(self.list)):
            if len(self.list[line]) < self.columns:
                for i in range(0, self.columns - len(self.list[line])):
                    self.list[line].append(0)

    def __str__(self):
        string_to_return = str()
        interval = self.number_of_digits + 4
        for row in self.list:
            for el in row:
                string_to_return += str(el).center(interval)
            string_to_return += '\n'
        return string_to_return

    def __add__(self, other):
        if self.columns != other.columns or self.rows != other.rows:
            print('You can add matrices only with the same size!')
        else:
            list_to_return = []
            for row_ind in range(0, self.rows):
                row_list = []
                for el_ind in range(0, self.columns):
                    row_list.append(self.list[row_ind][el_ind] + other.list[row_ind][el_ind])
                list_to_return.append(row_list)
            return Matrix(list_to_return)


matrix_1 = Matrix([[11, 14, 13, 14], [21, -22, 23], [31, 32], [1, 2, 3, 4]])

print(matrix_1)

matrix_2 = Matrix([[11, 12, 13, 14], [21, 2], [31, 32, 33], [41, 42, 43, 44]])

print(matrix_2)

matrix_3 = matrix_2 + matrix_1

print(matrix_3)

matrix_4 = matrix_3 + matrix_1 + matrix_2

print(matrix_4)
