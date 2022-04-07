# test list
# user_list = ['text', None, 42, True, [1, 2.3, 'st'], False, 3.1415, 'df', 54]

# creating list from user input
user_list = input('Enter elements divided by space:').split()

# switching every two elements
for n in range(0, len(user_list)-1, 2):
    temp = user_list[n]
    user_list[n] = user_list[n+1]
    user_list[n+1] = temp

# result
print(user_list)
