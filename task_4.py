# test list
# test_string = 'test text 0123456789abc'
# user_list = test_string.split()

# creating list from user input
user_list = input('Enter words divided by space:').split()

for ind, el in enumerate(user_list):
    print(ind+1, el[0:10])
