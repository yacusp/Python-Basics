# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


with open('text_task_51.txt', 'w', encoding='utf-8') as w_file:
    while True:
        line = input('Enter integers divided by space to write in file or press Enter to finish: ')
        line = line.split()
        if not line:
            break
        else:
            for num in line:
                try:
                    int(num)
                    w_file.write(num + ' ')
                except ValueError:
                    print('You should enter only integers!')

with open('text_task_51.txt', 'r', encoding='utf-8') as r_file:
    total_sum = 0
    for line in r_file:
        numbers = line.split()
        for n in numbers:
            total_sum += int(n)
    print('Total sum is:', total_sum)
