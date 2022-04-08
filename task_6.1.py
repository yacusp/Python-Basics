# test_input = {'название': ['компьютер', 'принтер', 'сканер'], 'цена': [20000, 6000, 2000], 'количество': [5, 2, 7], 'ед': ['шт.', 'шт.', 'шт.']}

char_list = ('Название', 'Цена', 'Количество', 'Ед.')
input_dict = {}

for ch in range(0, len(char_list)):
    user_input = input(f'Введите список значений характеристики {char_list[ch]} для всех товаров через пробел:').split()
    input_dict.update({char_list[ch]: user_input})
    #print(input_dict)

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
