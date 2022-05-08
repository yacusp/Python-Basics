# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivision(Exception):
    pass


while True:

    dividend = input('Enter dividend or enter \"stop\" to finish: ')
    if dividend == 'stop':
        break
    try:
        dividend = float(dividend)
    except ValueError:
        print('It is not a number.')
        continue

    divisor = input('Enter divisor or enter \"stop\" to finish: ')
    if divisor == 'stop':
        break
    try:
        divisor = float(divisor)
    except ValueError:
        print('It is not a number.')
        continue

    try:
        if divisor == 0:
            raise MyZeroDivision('Division by zero is not possible!')
        else:
            print(dividend / divisor)
    except MyZeroDivision as err:
        print(err)
