from itertools import cycle

test_list = ['I', 'Love', 'Python']
stop_number = 9

for el in cycle(test_list):
    print(el)
    stop_number -= 1
    if stop_number <= 0:
        break
