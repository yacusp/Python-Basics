# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

line_counter = 0
word_counter = 0
total_counter = dict()

with open('text_task_2.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line_counter += 1
        word_counter = len(line.split())
        total_counter.update({line_counter: word_counter})

print('Total lines number:', line_counter)
print('Worlds in each line: ')

for n in range(1, len(total_counter) + 1):
    print(f'Line #{n} has {total_counter[n]} words.')
