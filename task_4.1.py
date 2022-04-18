test_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

repeated_numbers = set()
unique_numbers = set()

for el in test_list:
    if el in repeated_numbers:
        continue
    elif el in unique_numbers:
        unique_numbers.discard(el)
        repeated_numbers.add(el)
    else:
        unique_numbers.add(el)

result_list = [number for number in test_list if number in unique_numbers]
print(result_list)
