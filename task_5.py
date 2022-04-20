# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

final_sum = 0

with open('text_task_5.txt', 'w', encoding='utf-8') as file:
    while True:
        line = input('Enter integers divided by space to write in file or press Enter to finish: ')
        line = line.split()
        if not line:
            break
        else:
            for num in line:
                try:
                    final_sum += int(num)
                    file.write(num + ' ')
                except ValueError:
                    print('You should enter only integers!')

print('Total sum is:', final_sum)
