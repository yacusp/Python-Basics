# test_input = {'название': ['компьютер', 'принтер', 'сканер'], 'цена': [20000, 6000, 2000], 'количество': [5, 2, 7], 'ед': ['шт.', 'шт.', 'шт.']}

input_dict = {}
user_input = input('Введите через пробел характеристику и список значений или \"done\" для зовершения:')

while user_input != 'done':
    user_input = user_input.split()
    input_dict.update({user_input[0]: user_input[1:]})
    #print(input_dict)
    user_input = input('Введите через пробел характеристику и список значений или \"done\" для зовершения:')

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
