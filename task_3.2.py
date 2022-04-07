user_input = int(input('Введите число от 1 до 12:'))
month_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень', 4: 'Зима'}
print(f'Время года: {month_dict[(user_input)//3]}')
