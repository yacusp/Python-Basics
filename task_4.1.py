# Программа принимает действительное положительное число x и целое отрицательное число
# y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
# my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
# числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
# помощью оператора **.

def my_func(x, y):
    try:
        x = int(x)
        y = int(y)
        if x < 0 or y > 0:
            print('First number should be positive and second should be negative!')

        else:
            return x**y

    except ValueError:
        print("You should enter only numbers.")


user_x = input('Enter positive number: ')
user_y = input('Enter negative number: ')

print(f'Result is: {my_func(user_x, user_y)}')
