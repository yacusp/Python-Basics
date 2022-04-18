# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

try:
    script_name, work_hours, salary, bonus = argv

except ValueError:
    print("You should enter three values divided by space in order: worked hours, salary per hour and bonus sum.")

try:
    work_hours = int(work_hours)
    salary = int(salary)
    bonus = int(bonus)
    income = work_hours * salary + bonus
    print(f'Total income is: {income}.')

except ValueError:
    print("You should enter only integers.")
