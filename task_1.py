# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('text_task_1.txt', 'w', encoding='utf-8') as file:
    while True:
        line = input('Enter line to write in file or press Enter to finish: ')
        if not line:
            break
        else:
            file.write(line + '\n')
