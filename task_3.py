# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов

def my_func(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        if a >= c and b >= c:
            return a + b
        elif a >= b and c >= b:
            return a + c
        else:
            return b + c
    except ValueError:
        print("You should enter only numbers.")


user_a = input('Enter \'a\' number: ')
user_b = input('Enter \'b\' number: ')
user_c = input('Enter \'c\' number: ')

print(f'Sum of two biggest numbers is: {my_func(user_a, user_b, user_c)}')
