# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class MyComplexNumber:
    def __init__(self, input_number):
        self.__real_part = 0
        self.__imaginary_part = 0

        try:
            if not input_number.endswith('j'):
                print('It is not a complex number!')
                raise ValueError
        except ValueError:
            return

        input_number = input_number.replace(' ', '')
        input_number = input_number[:-1]

        if input_number.count('-') == 0 and input_number.count('+') == 0:
            try:
                self.__imaginary_part = int(input_number)
            except ValueError:
                print('Wrong input')
                return
        elif input_number.count('+') == 1:
            number_list = input_number.split('+')
            try:
                self.__real_part = int(number_list[0])
                self.__imaginary_part = int(number_list[1])
            except ValueError:
                print('Wrong input')
                return
        elif input_number.count('-') == 1:
            if input_number[0] == '-':
                try:
                    self.__imaginary_part = int(input_number)
                except ValueError:
                    print('Wrong input')
                    return
            else:
                number_list = input_number.split('-')
                try:
                    self.__real_part = int(number_list[0])
                    self.__imaginary_part = -1 * int(number_list[1])
                except ValueError:
                    print('Wrong input')
                    return
        elif input_number.count('-') == 2:
            number_list = input_number[1:].split('-')
            try:
                self.__real_part = -1 * int(number_list[0])
                self.__imaginary_part = -1 * int(number_list[1])
            except ValueError:
                print('Wrong input')
                return
        else:
            print('Wrong input')
            return

        if self.__imaginary_part == 0:
            print('Imaginary part can not be zero!')
            return

    @staticmethod
    def convert_to_string(real_num, imaginary_num):
        if real_num == 0:
            return str(f'{imaginary_num}j')
        elif imaginary_num > 0:
            return str(f'{real_num} + {imaginary_num}j')
        else:
            return str(f'{real_num} - {-1 * imaginary_num}j')

    def __str__(self):
        return MyComplexNumber.convert_to_string(self.__real_part, self.__imaginary_part)

    def __add__(self, other):
        new_real_part = self.__real_part + other.__real_part
        new_imaginary_part = self.__imaginary_part + other.__imaginary_part
        return MyComplexNumber(MyComplexNumber.convert_to_string(new_real_part, new_imaginary_part))

    def __sub__(self, other):
        new_real_part = self.__real_part - other.__real_part
        new_imaginary_part = self.__imaginary_part - other.__imaginary_part
        return MyComplexNumber(MyComplexNumber.convert_to_string(new_real_part, new_imaginary_part))

    def __mul__(self, other):
        new_real_part = self.__real_part * other.__real_part - self.__imaginary_part * other.__imaginary_part
        new_imaginary_part = self.__real_part * other.__imaginary_part + self.__imaginary_part * other.__real_part
        return MyComplexNumber(MyComplexNumber.convert_to_string(new_real_part, new_imaginary_part))


c_num_1 = MyComplexNumber('2j')
print(c_num_1)
c_num_2 = MyComplexNumber('-12j')
print(c_num_2)
c_num_3 = MyComplexNumber('3 + 5j')
print(c_num_3)
c_num_4 = MyComplexNumber('4 - 3j')
print(c_num_4)
c_num_5 = MyComplexNumber('-7 + 5j')
print(c_num_5)
c_num_6 = MyComplexNumber('- 11 - 7j')
print(c_num_6)

c_num_7 = c_num_3 + c_num_4  # 7 + 2j
print(c_num_7)

c_num_8 = c_num_3 * c_num_5  # -46 - 20j
print(c_num_8)

c_num_9 = c_num_7 - c_num_5
print(c_num_9)
