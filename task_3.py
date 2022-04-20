# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

import my_number_separator

with open('text_task_3.txt', 'r', encoding='utf-8') as file:
    employee_counter = 0
    salary_counter = 0
    print('Employees with salary less than 20000:')

    for line in file:
        if my_number_separator.take_out_numbers(line)[0] < 20000:
            print(line.split()[0])
            employee_counter += 1
            salary_counter += my_number_separator.take_out_numbers(line)[0]

    print(f'\nAverage salary: {(salary_counter / employee_counter):.2f}')
