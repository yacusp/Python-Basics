# my_list = []
my_list = [7, 5, 3, 3, 2]
user_input = input('Enter new number or type \"done\":')

while user_input != 'done':
    for i in range(0, len(my_list)+1):
        if i == len(my_list) or len(my_list) == 0:
            my_list.append(int(user_input))
        elif int(user_input) > my_list[i]:
            my_list.insert(i, int(user_input))
            break
    print(my_list)
    user_input = input('Enter new number or type \"done\":')
