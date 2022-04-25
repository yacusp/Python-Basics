# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()),
# вычитание (__sub__()),
# умножение (__mul__()),
# деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернёт строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(self.amount + other.amount)
        else:
            print('You can add only cell to another cell!')            

    def __sub__(self, other):
        if isinstance(other, Cell):
            if self.amount - other.amount > 0:
                return Cell(self.amount - other.amount)                
            else:
                print('The procedure is impossible due to the small \n' \
                      'amount of cells in the subtracted individual!')
                return None
        else:
            print('You can subtract only cell from another cell!')

    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(self.amount * other.amount)
        else:
            print('You can multiply only cell with another cell!')

    def __truediv__(self, other):
        if isinstance(other, Cell):
            return Cell(self.amount // other.amount)
        else:
            print ('You can divide only cell by another cell!')

    def make_order(self, cells_in_row):
        return ('*' * cells_in_row + '\n') * (self.amount // cells_in_row) \
                     + '*' * (self.amount % cells_in_row) + '\n'
         

cell_1 = Cell(3)  # 3
print('Cell_1')
print(cell_1.make_order(3))

cell_2 = Cell(5)  # 5
print('Cell_2')
print(cell_2.make_order(3))

cell_3 = cell_2 + cell_1  # 8
print('Cell_3')
print(cell_3.make_order(5))

cell_4 = cell_2 * cell_3  # 40
print('Cell_4')
print(cell_4.make_order(7))

cell_5 = cell_4 - cell_3  # 32
print('Cell_5')
print(cell_5.make_order(5))

cell_6 = cell_2 - cell_3  # None
print('Cell_6')
print(cell_6, '\n')

cell_7 = cell_5 / cell_2  # 6
print('Cell_7')
print(cell_7.make_order(5))


