test_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result_list = [test_list[i] for i in range(0, len(test_list)) if test_list.count(test_list[i]) == 1]

print(result_list)
