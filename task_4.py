# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_task_4_input.txt', 'r', encoding='utf-8') as reding_file, \
        open('text_task_4_output.txt', 'w', encoding='utf-8') as final_file:
    for line in reding_file:
        line_list = line.split('—')
        for i in range(0, len(line_list)):
            line_list[i] = line_list[i].strip()
        final_file.write(f'{my_num_dict[line_list[0]]} — {line_list[1]}\n')
