# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text


def int_func(word):
    return word[0].upper() + word[1:]


print(int_func(input('Enter some word: ')))

