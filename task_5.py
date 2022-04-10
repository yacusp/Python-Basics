# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
# добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

def infinite_sum():
    total_sum = 0
    in_progress = True

    while in_progress:
        user_input = input('Enter numbers divided by space or enter \"done\" to finish: ').split()

        for el in user_input:
            if el == 'done':
                in_progress = False
                print('Calculation is over.')
            else:
                total_sum += int(el)

        print('Total sum is:', total_sum)


infinite_sum()
