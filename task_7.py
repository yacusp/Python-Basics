def fact(number):
    result = 1
    for n in range(1, number + 1):
        result *= n
        yield result


user_number = int(input('Enter integer: '))

for el in fact(user_number):
    print(el)
