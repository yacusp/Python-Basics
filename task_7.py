#  7. Создать вручную и заполнить несколькими строками текстовый файл,
#  в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
import my_number_separator

firms_dict = dict()
successful_firms_counter = 0
total_firms_income = 0
final_list = []

with open('text_task_7.txt', 'r', encoding='utf-8') as read_file, \
        open('save_task_7.json', 'w', encoding='utf-8') as write_file:
    for line in read_file:
        line_numbers = my_number_separator.take_out_numbers(line)
        line = line.split()
        income = line_numbers[-2] - line_numbers[-1]
        firm_name = line[0]
        firms_dict.update({firm_name: income})

        if income > 0:
            successful_firms_counter += 1
            total_firms_income += income

    average_profit = total_firms_income / successful_firms_counter
    final_list = [firms_dict, {"average_profit": average_profit}]

    json.dump(final_list, write_file)

with open('save_task_7.json', 'r', encoding='utf-8') as file:
    print(json.load(file))
