# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator

translator = Translator()

with open('text_task_4_input.txt', 'r', encoding='utf-8') as reding_file, \
        open('text_task_4_output.txt', 'w', encoding='utf-8') as final_file:
    for line in reding_file:
        line_list = line.split('—')
        print(line_list)
        translated = translator.translate(line_list[0], src='en', dest='ru')
        final_file.write(translated.text + '—' + line_list[1])
