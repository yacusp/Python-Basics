# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль

def division(a, b):
    try:
        a = int(a)
        b = int(b)
        return a / b
    except ZeroDivisionError:
        print("You can't divide by zero.")
    except ValueError:
        print("You should enter only numbers.")


print('Division result:', division(input('Enter a number:'), input('Enter b number:')))
