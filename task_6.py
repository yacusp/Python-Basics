# test_input = {'название': ['компьютер', 'принтер', 'сканер'], 'цена': [20000, 6000, 2000], 'количество': [5, 2, 7], 'ед': ['шт.', 'шт.', 'шт.']}
test_input = {'название': ['компьютер', 'принтер', 'сканер'], 'цена': [20000, 6000, 2000], 'производитель': ['Тайвань', 'Китай', 'Япония'], 'количество': [5, 2, 7], 'ед': ['шт.', 'шт.', 'шт.']}

final_list = []
key_list = list(test_input.keys())
temp_dict = {}

for t in range(0, len(test_input.get(key_list[0]))):
    for key in range(0, len(key_list)):
        temp_list = test_input.get(key_list[key])
        new_dict = {key_list[key]: temp_list[t]}
        temp_dict.update(new_dict)
    temp_tuple = (t+1, temp_dict.copy())
    final_list.append(temp_tuple)
    temp_dict.clear()

print(final_list)
