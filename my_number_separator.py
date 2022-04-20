# Returns list of numbers from the string
# At least one space should be between different numbers

def take_out_numbers(income_string):
    def is_number(symbol):
        try:
            int(symbol)
            return True
        except ValueError:
            return False

    word_list = income_string.split()

    final_list = []

    for word in word_list:
        number_is_integer = True
        current_string_number = str()
        for i in range(0, len(word)):
            if is_number(word[i]):
                current_string_number += word[i]
            elif word[i] == '.' and i < len(word) - 1:
                if is_number(word[i + 1]):
                    number_is_integer = False
                    current_string_number += word[i]

            if i == len(word) - 1 and current_string_number:
                if number_is_integer:
                    final_list.append(int(current_string_number))
                else:
                    final_list.append(float(current_string_number))

    return final_list


#test_string_1 = '.07 1kj 2 lk3lk 4 5.1 ret 65gt. 3.14pi.  .08h . .09jh jhki.8.kj'
#print(take_out_numbers(test_string_1))
