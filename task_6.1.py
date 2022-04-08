user_input = input('Введите названия товаров через пробел:').split()
input_dict = {'Название': user_input}
print(input_dict)

user_input = input('Введите цену товаров через пробел:').split()
input_dict.update({'Цена': user_input})
print(input_dict)

user_input = input('Введите количество товаров через пробел:').split()
input_dict.update({'Количество': user_input})
print(input_dict)

user_input = input('Введите единицы измерения товаров через пробел:').split()
input_dict.update({'ед.': user_input})
print(input_dict)

final_list = []
key_list = list(input_dict.keys())
temp_dict = {}

for t in range(0, len(input_dict.get(key_list[0]))):
    for key in range(0, len(key_list)):
        temp_list = input_dict.get(key_list[key])
        new_dict = {key_list[key]: temp_list[t]}
        temp_dict.update(new_dict)
    temp_tuple = (t+1, temp_dict.copy())
    final_list.append(temp_tuple)
    temp_dict.clear()

print(final_list)
