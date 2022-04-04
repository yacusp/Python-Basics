# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Enter a positive integer: '))
biggest_number = number % 10

while number >= 10:
    number = number // 10
    last_number = number % 10
    if last_number > biggest_number:
        biggest_number = last_number

print('The biggest number is:', biggest_number)
