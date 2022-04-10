# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
# пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
# исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
# написанную ранее функцию int_func().

def int_func(word):
    return word[0].upper() + word[1:]


user_input = input('Enter line of words divided by space: ').split()
final_line = str()

for w in user_input:
    final_line = final_line + int_func(w) + ' '

print(final_line)
