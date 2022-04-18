from itertools import count

start_number = int(input('Enter start integer: '))
stop_number = int(input('Enter start integer: '))

for el in count(start_number, 1):
    print(el)
    if el >= stop_number:
        break
